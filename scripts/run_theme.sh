#!/bin/bash
# 单主题流水线（假设 ComfyUI 已在运行，共享进程）
# 用法: run_theme.sh <tag> <frames> <seed>
#   base(480p,20步) → 场景检测切段 → 二采(1728x960,4步) → 拼接
set -u
TAG=${1:?tag}; FRAMES=${2:-226}; SEED=${3:-20261030}
B=${H3BASE:-/root/private_data/h3}
PY=/usr/local/bin/python3.11
S=$B/scripts
L=$B/logs
C=$B/ComfyUI
R=$B/reports
O=$C/output/video
IN=$C/input
mkdir -p $R/frames $IN $L $O
REP=$R/series_${TAG}_$(date +%Y%m%d_%H%M).txt
say(){ echo "$@" | tee -a $REP; }
say "==================== 主题 $TAG · ${FRAMES}帧 · seed=$SEED $(date) ===================="

FF=$(ls $B/pylibs/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-* 2>/dev/null | head -1)
[ -z "$FF" ] && FF=$(command -v ffmpeg 2>/dev/null)
[ -z "$FF" ] && { say "!! 无 ffmpeg"; exit 1; }
PROMPT=$S/prompts/series_${TAG}.txt
[ -s "$PROMPT" ] || { say "!! 缺提示词 $PROMPT"; exit 1; }

# ---------- 1) base 480p ----------
# base 有效判定：文件 >1MB（48B 半写坏文件不算），防止 SaveVideo 未完成被 -s 误判跳过
BASE_OK=0
if [ -s $O/${TAG}_base_00001_.mp4 ]; then
  SZ=$(stat -c%s $O/${TAG}_base_00001_.mp4 2>/dev/null || echo 0)
  if [ "$SZ" -gt 1000000 ]; then BASE_OK=1; fi
fi
if [ "$BASE_OK" = "1" ]; then
  say "base 已存在（${SZ}B），跳过"
else
  [ -e $O/${TAG}_base_00001_.mp4 ] && { say "!! base 是坏文件（${SZ}B），删除重生成"; rm -f $O/${TAG}_base_00001_.mp4; }
  say "########## base $TAG : 864x480 / ${FRAMES}帧 / 20步 / simple ##########"
  timeout 10800 $PY $S/h3_gen_wire.py $PROMPT video/${TAG}_base \
    20 $FRAMES $SEED simple max furina_single 864 480 dotted >> $REP 2>&1
  say "base 退出码=$?"
  # 生成后强校验：<1MB 视为失败
  SZ2=$(stat -c%s $O/${TAG}_base_00001_.mp4 2>/dev/null || echo 0)
  if [ "${SZ2:-0}" -lt 1000000 ]; then
    say "!! base 生成后仍为坏文件（${SZ2}B），本主题放弃，避免下游空跑"
    exit 1
  fi
fi

# ---------- 2) 切段 ----------
say ""
say "########## 切段 ##########"
$PY - "$FF" "$O" "$IN" "$TAG" <<'PY' 2>&1 | tee -a $REP
import subprocess, sys, os, av
ff, O, IN, TAG = sys.argv[1:5]
FPS = 24.0
def run(c): return subprocess.run(c, shell=True, capture_output=True, text=True)
def grid_floor(L):
    k = (L - 5) // 17
    return 5 + 17 * max(1, k)
def grid_nearest(L):
    # 就近网格（5+17k），比 floor 丢帧少一半；最小 22
    if L < 17:
        return max(17, L)
    k = round((L - 5) / 17)
    g = 5 + 17 * k
    return max(22, g)
v = f"{O}/{TAG}_base_00001_.mp4"
if not os.path.exists(v):
    print(f"!! 缺 {v}"); sys.exit(1)
n = av.open(v).streams.video[0].frames
r = run(f'{ff} -hide_banner -i {v} -vf "select=gt(scene\\,0.15),showinfo" -an -f null - 2>&1 | grep -oE "pts_time:[0-9.]+"')
cuts = sorted(set(int(float(x.split(":")[1]) * FPS + 0.5) for x in r.stdout.split() if x.startswith("pts_time")))
cuts = [c for c in cuts if 20 < c < n - 20]
# 伪切点过滤：间隔 < MIN_GAP 帧的密集切点合并（闪电/光效闪烁会被误检为切点）
MIN_GAP = 24  # 至少 1 秒一段
merged = []
for c in cuts:
    if merged and c - merged[-1] < MIN_GAP:
        merged[-1] = c  # 并入前一个切点（取靠后的）
    else:
        merged.append(c)
if merged != cuts:
    print(f"!! 过滤伪切点: {cuts} -> {merged}")
cuts = merged
# 暗场景兜底：检出段数过少（<3段）时按 ~73 帧网格均分，避免单大段触发二采帧数悬崖
if len(cuts) + 1 < 3:
    target = max(2, min(6, (n + 72) // 73))
    step = n / target
    cuts = [int(round(step * k)) for k in range(1, target)]
    cuts = [c for c in cuts if 20 < c < n - 20]
    print(f"!! 暗场景兜底切段：均分 {len(cuts)+1} 段（step={step:.1f}帧）")
print(f"总帧 {n}  检出切点 {cuts}")

# ★ 切段算法（就近网格 + 最小段保护 + 余量传递）：每段取就近网格帧数，
# <39 帧的碎段并入前一段；累计起点随之偏移，最后一段吸收剩余帧，
# 保证 Σ段帧数 ≈ base 帧数（不再向下取整丢 2-3 秒），15s 不再变 12s。
b = [0] + cuts + [n]
segs = []
for i in range(len(b) - 1):
    L = b[i + 1] - b[i]
    segs.append(grid_nearest(L))
# 最小段保护：<39 帧的碎段并入前一段（避免 0.9s 碎段，快切也不至于太碎）
MIN_SEG = 39
merged2 = []
for gl in segs:
    if gl < MIN_SEG and merged2:
        merged2[-1] += gl
    else:
        merged2.append(gl)
segs = merged2
# 大段安全化：>124 帧的段缩到 124（960p 二采安全上限；skill 实测 124帧=192s/it，192帧=1504s/it）
# 不拆（拆了余数会碎段）；缩到 124 丢的帧由拼接 tpad 补回。124 = 5+17×7 是合法网格。
MAX_SEG = 124
segs = [MAX_SEG if gl > MAX_SEG else gl for gl in segs]
# 拆分/缩段后碎段再并入
merged3 = []
for gl in segs:
    if gl < MIN_SEG and merged3:
        merged3[-1] += gl
    else:
        merged3.append(gl)
segs = merged3
# 余量传递：段起点 = 上一段实际终点；最后一段吸收剩余到总帧 = n
b2 = [0]
for gl in segs:
    b2.append(b2[-1] + gl)
if b2[-1] > n:
    segs[-1] -= (b2[-1] - n); b2[-1] = n
elif b2[-1] < n:
    segs[-1] += (n - b2[-1]); b2[-1] = n
# 最后一段就近网格修正（允许轻微超/欠，拼接时 tpad 兜底；且不超 MAX_SEG 安全上限）
if len(segs) > 1:
    segs[-1] = grid_nearest(segs[-1])
    if segs[-1] > MAX_SEG:
        segs[-1] = MAX_SEG
b2 = [0]
for gl in segs:
    b2.append(b2[-1] + gl)
if b2[-1] > n:
    segs[-1] -= (b2[-1] - n); b2[-1] = n
print(f"切段后总帧 {sum(segs)}（base {n}，误差 {sum(segs)-n:+d} 帧 = {(sum(segs)-n)/FPS:+.3f}s）")
total = 0
for i, gl in enumerate(segs):
    st = b2[i]
    out = f"{IN}/{TAG}seg{i+1}.mp4"
    # 用 -t 精确时长切（音视频等长，修掉 -frames:v 只截视频导致音画不同步的隐患）
    run(f'{ff} -v error -ss {st/FPS:.6f} -i {v} -t {gl/FPS:.6f} -c:v libx264 -crf 14 -c:a aac -y {out}')
    rr = run(f'{ff} -hide_banner -i {out} 2>&1 | grep -oE "[0-9]+x[0-9]+" | head -1')
    print(f"   段{i+1}: 起 {st:4d} 长 {gl:3d} ({gl/24:.3f}s)  {rr.stdout.strip()}")
    total += 1
print(f"共切出 {total} 段，总帧 {sum(segs)} = {(sum(segs)/FPS):.3f}s")
PY

# ---------- 3) 二采（动态段数） ----------
say ""
say "########## 二采 ##########"
# 收集实际存在的段文件
SEGS=()
for f in $IN/${TAG}seg*.mp4; do [ -s "$f" ] && SEGS+=("$f"); done
NSEG=${#SEGS[@]}
say "共 ${NSEG} 段待二采"
SEGN=0
for F in "${SEGS[@]}"; do
  [ -s "$F" ] || continue
  GL=$($PY -c "import av; print(av.open('$F').streams.video[0].frames)" 2>/dev/null | tail -1)
  [ -z "$GL" ] && continue
  SEGN=$((SEGN+1))
  BN=$(basename "$F" .mp4)
  say ""
  say "--- 二采 ${BN} (${GL}帧) → 1728x960 / 4步 / beta / denoise 0.2 ---"
  timeout 2400 $PY $S/twopass_gen.py $PROMPT video/tp_${TAG}${SEGN} \
    ${BN}.mp4 1728 960 4 0.2 beta $((SEED + SEGN)) furina_single ${GL} >> $REP 2>&1
  say "退出码=$?"
done

# ---------- 4) 拼接（动态段数）· 官方音床合流法 · 音乐完整不截断 ----------
# 官方 api-wiring.md 装配：视频单独 concat(-an) + 音轨用 base 完整音轨(音床)整体合流，
# 避免每段 AAC 帧填充累积漂移（四段 96ms、相关 0.34 的坑）。
# 音乐完整版：视频 tpad 补帧对齐音床时长，保证 base 完整音轨(含收尾衰减)不被 -shortest 硬截。
say ""
say "########## 拼接（音床合流 + 音乐完整）##########"
LIST=$B/${TAG}_cat.txt
: > $LIST
for f in $O/tp_${TAG}*_00001_.mp4; do
  [ -s "$f" ] && echo "file '$f'" >> $LIST
done
# 段完整性校验：二采段数少于切出段数 = 有段失败 → 不产出残片，标记待重跑
if [ "${#SEGS[@]}" -gt 0 ] && [ "$(wc -l < $LIST)" -lt "${#SEGS[@]}" ]; then
  say "!! 段不完整：切出 ${#SEGS[@]} 段，二采成功 ${NSEG}/${#SEGS[@]}（产出 $(wc -l < $LIST) 个）"
  say "!! 跳过拼接，不产出残片（待补跑缺失段后重拼）"
  touch $B/${TAG}_INCOMPLETE
  exit 1
fi
cat $LIST | tee -a $REP
if [ "$(wc -l < $LIST)" -ge 2 ]; then
  # 1) 视频流单独拼接（去音频，零漂移）
  $FF -v error -f concat -safe 0 -i $LIST -c:v copy -an -y $O/${TAG}_video_only.mp4
  say "视频拼接退出码=$?"
  BASE=$O/${TAG}_base_00001_.mp4
  if [ -s "$BASE" ]; then
    # 2) 音床（base 完整音轨）+ 音床时长
    $FF -y -v error -i $BASE -vn -acodec pcm_s16le -ar 32000 -ac 2 $B/${TAG}_bed.wav 2>/dev/null
    BED_DUR=$($FF -hide_banner -i $BASE 2>&1 | grep -oE "Duration: [0-9:.]+" | grep -oE "[0-9:.]+")
    BED_SEC=$(python3 -c "h,m,s='$BED_DUR'.split(':'); print(round(int(h)*3600+int(m)*60+float(s),3))")
    VDO_DUR=$($FF -hide_banner -i $O/${TAG}_video_only.mp4 2>&1 | grep -oE "Duration: [0-9:.]+" | grep -oE "[0-9:.]+")
    VDO_SEC=$(python3 -c "h,m,s='$VDO_DUR'.split(':'); print(round(int(h)*3600+int(m)*60+float(s),3))")
    say "音床时长=${BED_SEC}s  视频拼接时长=${VDO_SEC}s  补帧=$([ $(echo "$BED_SEC > $VDO_SEC" | bc) ] && echo YES || echo NO)"
    # 3) 视频 tpad 补帧对齐音床（克隆末帧），保证音乐完整收尾
    PAD=$(python3 -c "print(max(0, round($BED_SEC - $VDO_SEC, 3)))")
    if [ "$(echo "$PAD > 0.05" | bc)" = "1" ]; then
      $FF -v error -i $O/${TAG}_video_only.mp4 -vf "tpad=stop_mode=clone:stop_duration=$PAD" \
          -c:v libx264 -crf 16 -preset medium -pix_fmt yuv420p -y $O/${TAG}_video_pad.mp4
      say "补帧退出码=$? (补 ${PAD}s)"
      VSRC=$O/${TAG}_video_pad.mp4
    else
      VSRC=$O/${TAG}_video_only.mp4
    fi
    # 4) 合流（此时音视频等长，-shortest 不再截音轨）
    $FF -v error -i $VSRC -i $B/${TAG}_bed.wav \
        -c:v copy -c:a aac -b:a 192k -shortest -y $O/${TAG}_FULL.mp4
    say "合流退出码=$?"
  else
    # 兜底：无 base 音床时直接用段音频拼接（旧法）
    $FF -v error -f concat -safe 0 -i $LIST -c:v libx264 -crf 16 -preset medium -pix_fmt yuv420p \
        -c:a aac -b:a 192k -y $O/${TAG}_FULL.mp4
    say "兜底拼接退出码=$?"
  fi
  $FF -hide_banner -i $O/${TAG}_FULL.mp4 2>&1 | grep -E 'Duration|Stream' | tee -a $REP
  $FF -v error -i $O/${TAG}_FULL.mp4 -vf 'fps=2,scale=288:160,tile=8x6' -frames:v 1 -y $R/frames/${TAG}_sheet.png
fi

say ""
say "########## 产出 ##########"
ls -la $O/${TAG}_FULL.mp4 $O/tp_${TAG}*_00001_.mp4 2>&1 | tee -a $REP
say "==================== 主题 $TAG 结束 $(date) ===================="
say "REPORT=$REP"
echo "THEME_DONE $TAG"
