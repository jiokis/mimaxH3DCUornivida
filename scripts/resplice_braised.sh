#!/bin/bash
# 等水之环舞完成 → 用已有 5 段 tp 重拼红烧肉（音床合流 + 音乐完整）
B=/root/private_data/h3
FF=$B/pylibs/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2
LOG=$B/logs/resplice_braised.log
echo "=== 等水之环舞成片 $(date) ===" >> $LOG
for i in $(seq 1 60); do
  [ -s $B/ComfyUI/output/video/water_dance_FULL.mp4 ] && { echo "水之环舞完成 ✓" >> $LOG; break; }
  sleep 60
done
# 等 run_theme 进程退出（避免抢 ComfyUI）
for i in $(seq 1 30); do
  ps -ef | grep -q "run_theme.sh water_dance" || { echo "water_dance 进程已退" >> $LOG; break; }
  sleep 20
done
sleep 15
echo "=== 重拼红烧肉（5 段 + 音床）$(date) ===" >> $LOG
LIST=$B/braised_pork_cat.txt
: > $LIST
for i in 1 2 3 4 5; do
  f=$B/ComfyUI/output/video/tp_braised_pork${i}_00001_.mp4
  [ -s "$f" ] && printf "file '%s'\n" "$f" >> $LIST
done
echo "清单段数: $(wc -l < $LIST)" >> $LOG
# 视频单独拼接
$FF -v error -f concat -safe 0 -i $LIST -c:v copy -an -y $B/ComfyUI/output/video/braised_pork_video_only.mp4 >> $LOG 2>&1
# 音床
$FF -y -v error -i $B/ComfyUI/output/video/braised_pork_base_00001_.mp4 -vn -acodec pcm_s16le -ar 32000 -ac 2 $B/braised_pork_bed.wav 2>/dev/null
# tpad 补帧到音床时长
BED_DUR=$($FF -hide_banner -i $B/ComfyUI/output/video/braised_pork_base_00001_.mp4 2>&1 | grep -oE "Duration: [0-9:.]+" | grep -oE "[0-9:.]+")
BED_SEC=$(python3 -c "h,m,s='$BED_DUR'.split(':'); print(round(int(h)*3600+int(m)*60+float(s),3))")
VDO_DUR=$($FF -hide_banner -i $B/ComfyUI/output/video/braised_pork_video_only.mp4 2>&1 | grep -oE "Duration: [0-9:.]+" | grep -oE "[0-9:.]+")
VDO_SEC=$(python3 -c "h,m,s='$VDO_DUR'.split(':'); print(round(int(h)*3600+int(m)*60+float(s),3))")
PAD=$(python3 -c "print(max(0, round($BED_SEC - $VDO_SEC, 3)))")
echo "音床 ${BED_SEC}s 视频 ${VDO_SEC}s 补帧 ${PAD}s" >> $LOG
if [ "$(echo "$PAD > 0.05" | bc)" = "1" ]; then
  $FF -v error -i $B/ComfyUI/output/video/braised_pork_video_only.mp4 -vf "tpad=stop_mode=clone:stop_duration=$PAD" -c:v libx264 -crf 16 -preset medium -pix_fmt yuv420p -y $B/ComfyUI/output/video/braised_pork_video_pad.mp4 >> $LOG 2>&1
  VSRC=$B/ComfyUI/output/video/braised_pork_video_pad.mp4
else
  VSRC=$B/ComfyUI/output/video/braised_pork_video_only.mp4
fi
$FF -v error -i $VSRC -i $B/braised_pork_bed.wav -c:v copy -c:a aac -b:a 192k -shortest -y $B/ComfyUI/output/video/braised_pork_FULL.mp4 >> $LOG 2>&1
echo "=== 重拼完成 $(date) ===" >> $LOG
$FF -hide_banner -i $B/ComfyUI/output/video/braised_pork_FULL.mp4 2>&1 | grep Duration >> $LOG
echo RESPLICE_DONE >> $LOG
