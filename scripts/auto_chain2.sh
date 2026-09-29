#!/bin/bash
# 自动接力队列 v2：等前一个成片出现 → 等其 run_theme 进程退出（按 PID）→ 跑下一个
# 用 PID 追踪避免 grep 字符串自匹配问题
set -u
B=/root/private_data/h3
L=$B/logs
LOG=$L/auto_chain2.log
mkdir -p $L
echo "==================== 自动接力队列 v2 启动 $(date) ====================" >> $LOG

# ---------- 主题链 ----------
CHAIN=(
  "gongfu_tea 345 20261060"
)

# 等蛋炒饭 v2 成片（正在跑的）
PREV=fried_rice
echo "等待 $PREV 成片 ..." >> $LOG
GOT=0
for i in $(seq 1 240); do
  if [ -s $B/ComfyUI/output/video/${PREV}_FULL.mp4 ]; then
    echo "$PREV 成片 ✓ $(date)" >> $LOG; GOT=1; break
  fi
  sleep 30
done
[ "$GOT" = "0" ] && { echo "!! 等待 $PREV 超时（2h）" >> $LOG; }

# 等前一个 run_theme 进程退出（避免两个客户端抢同一 ComfyUI）
# 先找出蛋炒饭的 run_theme PID（若有），按 PID 等
FR_PID=$(pgrep -f "run_theme.sh fried_rice" | head -1)
if [ -n "$FR_PID" ]; then
  echo "等 fried_rice run_theme (PID $FR_PID) 退出 ..." >> $LOG
  for i in $(seq 1 30); do
    if ! kill -0 $FR_PID 2>/dev/null; then echo "已退出 ✓" >> $LOG; break; fi
    sleep 10
  done
fi
sleep 20

# 逐个跑链上主题
N=${#CHAIN[@]}
IDX=0
for spec in "${CHAIN[@]}"; do
  read -r TAG FRAMES SEED <<< "$spec"
  IDX=$((IDX+1))
  echo "" >> $LOG
  echo "########## [$IDX/$N] 主题 $TAG (${FRAMES}帧, seed=$SEED) $(date) ##########" >> $LOG
  bash $B/scripts/run_theme.sh $TAG $FRAMES $SEED >> $LOG 2>&1
  OK=$([ -s $B/ComfyUI/output/video/${TAG}_FULL.mp4 ] && echo YES || echo NO)
  echo "## $TAG 结束 $(date) 成片=$OK" >> $LOG
done

echo "==================== 队列全部完成 $(date) ====================" >> $LOG
echo AUTO_CHAIN_DONE >> $LOG
