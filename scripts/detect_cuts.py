#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""切点检测模块：三信号融合 + 切点对齐（替代单 scene 检测）
用法: detect_cuts.py <video> <ffmpeg> [scene_thresh] [min_gap]
输出: JSON 切点列表（帧号），供 run_theme.sh 切段。

信号:
  A. scene 像素差     (select=gt(scene,T),showinfo)
  B. 帧间差分峰值     (相邻帧 SAD，窗口峰值)
  C. 音频 RMS 突变    (astats RMS，滑动窗口 >2σ 突变)

融合: 三信号 ±3 帧内一致 → 高置信；两信号 → 中置信；单信号 → 丢弃
对齐: 每个候选切点 ±5 帧内找帧差最小帧（画面最稳定=纯镜头内容，非过渡帧）
"""
import subprocess, json, sys, re, os

def run(ff, cmd):
    r = subprocess.run(f'{ff} {cmd}', shell=True, capture_output=True, text=True)
    return r.stdout

def scene_detect(v, ff, thresh):
    out = run(ff, f'-hide_banner -i "{v}" -vf "select=gt(scene\\,{thresh}),showinfo" -an -f null -')
    pts = re.findall(r'pts_time:([0-9.]+)', out)
    return [int(round(float(p) * 24)) for p in pts]

def framdiff_peaks(v, ff, window=5, ratio=0.4):
    """帧间差分峰值：逐帧 SAD，取局部窗口峰值（超过邻域均值 ratio 倍）"""
    out = run(ff, f'-hide_banner -i "{v}" -vf "select=gt(scene\\,0.05),signalstats,metadata=print" -an -f null -')
    # 用 signalstats 的 YAVG 差值近似帧间变化
    yavgs = [float(x) for x in re.findall(r'YAVG:([0-9.]+)', out)]
    if len(yavgs) < window * 2 + 1:
        return []
    diffs = [abs(yavgs[i] - yavgs[i-1]) for i in range(1, len(yavgs))]
    cuts = []
    for i in range(window, len(diffs) - window):
        local_mean = sum(diffs[i-window:i+window]) / (2 * window)
        if diffs[i] > local_mean * (1 + ratio) and diffs[i] > 8:  # 明显突变
            cuts.append(i)
    return cuts

def audio_rms_breaks(v, ff, window_frames=12, sigma=2.0):
    """音频 RMS 突变：H3 AV 联合生成，镜头切换必伴随音景变化"""
    out = run(ff, f'-hide_banner -i "{v}" -af "astats=metadata=1:reset=0,ametadata=print:key=lavfi.astats.Overall.RMS_level" -f null -')
    rms = []
    for x in re.findall(r'RMS_level=(-?[0-9.]+)', out):
        try: rms.append(float(x))
        except ValueError: pass
    if len(rms) < 20:
        return []
    # 每 12 帧（0.5s）取一窗口均值，找突变
    windows = [sum(rms[i:i+window_frames])/window_frames for i in range(0, len(rms)-window_frames, window_frames)]
    mean = sum(windows)/len(windows)
    std = (sum((w-mean)**2 for w in windows)/len(windows))**0.5 or 1
    cuts = []
    for i, w in enumerate(windows):
        if abs(w - mean) > sigma * std:
            cuts.append(int(i * window_frames + window_frames/2))
    return cuts

def fuse(a, b, c, tol=3):
    """三信号融合：±tol 帧内一致计数"""
    all_cuts = sorted(set(a + b + c))
    merged = []
    for cut in all_cuts:
        votes = sum(1 for src in (a, b, c) if any(abs(x - cut) <= tol for x in src))
        if votes >= 2:  # 至少两信号
            merged.append(cut)
    return sorted(set(merged))

def snap_to_stable(cuts, v, ff, radius=5):
    """切点对齐：±radius 帧内找帧差最小帧（画面最稳定=纯镜头内容）"""
    # 用 YAVG 变化近似帧差（在 base 上重扫）
    out = run(ff, f'-hide_banner -i "{v}" -vf "select=gt(scene\\,0.05),signalstats,metadata=print" -an -f null -')
    yavgs = [float(x) for x in re.findall(r'YAVG:([0-9.]+)', out)]
    snapped = []
    for c in cuts:
        best, best_diff = c, 1e9
        for f in range(max(1, c-radius), min(len(yavgs)-1, c+radius+1)):
            d = abs(yavgs[f] - yavgs[f-1]) + abs(yavgs[f+1] - yavgs[f])
            if d < best_diff:
                best, best_diff = f, d
        snapped.append(best)
    return sorted(set(snapped))

if __name__ == "__main__":
    v = sys.argv[1]
    ff = sys.argv[2] if len(sys.argv) > 2 else "ffmpeg"
    thresh = float(sys.argv[3]) if len(sys.argv) > 3 else 0.15
    min_gap = int(sys.argv[4]) if len(sys.argv) > 4 else 24
    a = scene_detect(v, ff, thresh)
    b = framdiff_peaks(v, ff)
    c = audio_rms_breaks(v, ff)
    fused = fuse(a, b, c)
    # 最小间隔过滤
    final = []
    for cut in sorted(fused):
        if final and cut - final[-1] < min_gap:
            continue
        final.append(cut)
    # 对齐到稳定帧
    final = snap_to_stable(final, v, ff)
    print(json.dumps({"scene": a, "framdiff": b, "audio": c,
                      "fused": fused, "final": final, "n_shots": len(final)+1}))
