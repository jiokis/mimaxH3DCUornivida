#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""参考音乐分析：提取风格与动机特征（供 H3 配乐提示词参考）
用法: analyze_music.py <flac路径>
输出：时长/速度/调式/配器特征/动态弧线/节奏与动机特征
"""
import sys, numpy as np, soundfile as sf

path = sys.argv[1]
info = sf.info(path)
sr = info.samplerate
dur = info.duration
print("=== 基本信息 ===")
print(f"  文件: {path.split('/')[-1]}")
print(f"  采样率 {sr} Hz / 声道 {info.channels} / 时长 {dur:.1f}s ({dur/60:.2f}分)")

# 读取（若太长，降采样读取以省内存）
max_sec = 300
frames = int(min(dur, max_sec) * sr)
data, sr = sf.read(path, frames=frames, always_2d=True)
mono = data.mean(axis=1)
print(f"  分析长度 {len(mono)/sr:.1f}s")

hop = 1024
win = 2048
n_frames = (len(mono) - win) // hop
print(f"\n=== 帧数 {n_frames}（hop={hop}）===")

# 逐帧特征
rms = np.zeros(n_frames); centroid = np.zeros(n_frames); rolloff = np.zeros(n_frames)
lowE = np.zeros(n_frames); midE = np.zeros(n_frames); highE = np.zeros(n_frames)
flux = np.zeros(n_frames)
window = np.hanning(win)
freqs = np.fft.rfftfreq(win, 1/sr)
prev_spec = None
for i in range(n_frames):
    seg = mono[i*hop:i*hop+win] * window
    spec = np.abs(np.fft.rfft(seg))
    rms[i] = np.sqrt(np.mean(seg**2))
    s = spec.sum() + 1e-9
    centroid[i] = (freqs * spec).sum() / s
    cum = np.cumsum(spec); rolloff[i] = freqs[np.searchsorted(cum, 0.85*cum[-1])]
    lowE[i] = spec[(freqs>=20)&(freqs<250)].sum()/s
    midE[i] = spec[(freqs>=250)&(freqs<2000)].sum()/s
    highE[i] = spec[(freqs>=2000)].sum()/s
    if prev_spec is not None:
        flux[i] = np.maximum(spec - prev_spec, 0).sum()
    prev_spec = spec

t = np.arange(n_frames) * hop / sr
print("\n=== 动态弧线（RMS，分 10 段）===")
seg_n = max(1, n_frames//10)
for k in range(10):
    a, b = k*seg_n, min((k+1)*seg_n, n_frames)
    if a >= b: break
    db = 20*np.log10(rms[a:b].mean()+1e-9)
    bar = "█" * int(max(0, (db+60)/2))
    print(f"  {k*10:3d}-{(k+1)*10:3d}%  {db:6.1f} dB  {bar}")
print(f"  峰值 {20*np.log10(rms.max()+1e-9):.1f} dB  最低 {20*np.log10(rms.min()+1e-9):.1f} dB")

print("\n=== 频谱平衡（全曲均值）===")
print(f"  低频(<250Hz)  {lowE.mean()*100:5.1f}%")
print(f"  中频(250-2k)  {midE.mean()*100:5.1f}%")
print(f"  高频(>2kHz)   {highE.mean()*100:5.1f}%")
print(f"  谱质心 {centroid.mean():.0f} Hz（越低越暗/厚，越高越亮/尖）")
print(f"  谱滚降(85%) {rolloff.mean():.0f} Hz")

# 速度估计：onset flux 自相关
print("\n=== 速度与节奏 ===")
f = flux - flux.mean()
ac = np.correlate(f, f, mode='full')[len(f)-1:]
ac = ac / (ac[0]+1e-9)
lo = int(0.3*sr/hop)   # 200 BPM 上限
hi = int(2.5*sr/hop)   # 24 BPM 下限
if hi < len(ac):
    seg = ac[lo:hi]
    peaks = [(i+lo, seg[i]) for i in range(1, len(seg)-1)
             if seg[i] > seg[i-1] and seg[i] > seg[i+1] and seg[i] > 0.15]
    peaks.sort(key=lambda x: -x[1])
    shown = 0
    for lag, v in peaks[:6]:
        bpm = 60*sr/hop/lag
        if 30 <= bpm <= 220:
            print(f"  候选周期 {lag*hop/sr:.3f}s → {bpm:.1f} BPM（强度 {v:.2f}）")
            shown += 1
        if shown >= 4: break
    if shown == 0:
        print("  未检出强周期（自由速度/无稳定节拍）")
onset_rate = (flux > flux.mean()*1.5).sum() / (n_frames*hop/sr)
print(f"  起音密度 {onset_rate:.2f} 次/秒（越高越密集/急促）")

# 调式估计（简化：用低频段能量分布 + 半音级能量）
print("\n=== 调式倾向（色度估计）===")
chroma = np.zeros(12)
for i in range(0, n_frames, 4):
    seg = mono[i*hop:i*hop+win] * window
    spec = np.abs(np.fft.rfft(seg))
    for name, pc in zip(freqs, (np.round(12*np.log2(freqs/440.0+1e-9)).astype(int) % 12)):
        pass
    # 简化：按半音累加 80-2000Hz
    for k in range(1, len(spec)):
        fq = freqs[k]
        if 80 <= fq <= 2000:
            pc = int(round(12*np.log2(fq/440.0))) % 12
            chroma[pc] += spec[k]
chroma = chroma / (chroma.sum()+1e-9)
names = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
order = np.argsort(-chroma)
print("  最强音级:", " ".join(f"{names[i]}({chroma[i]*100:.1f}%)" for i in order[:5]))

sample = 20*np.log10(rms.mean()+1e-9)
print(f"\n=== 结论速览 ===")
print(f"  时长 {dur:.0f}s / 平均电平 {sample:.1f} dB / 动态范围 {20*np.log10(rms.max()/(rms.min()+1e-9)):.1f} dB")
print(f"  频谱：低{lowE.mean()*100:.0f}% 中{midE.mean()*100:.0f}% 高{highE.mean()*100:.0f}% / 质心 {centroid.mean():.0f}Hz")
print(f"  节奏：起音密度 {onset_rate:.2f}/s")
