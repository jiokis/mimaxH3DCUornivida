#!/bin/bash
# 自动接力队列：等前一个成片出现 → 自动开跑下一个主题 → 逐个连跑，卡零空转
# 可随时往 CHAIN 追加主题；每个主题完成后自动进入下一个。
set -u
B=/root/private_data/h3
L=$B/logs
LOG=$L/auto_chain.log
mkdir -p $L
echo "==================== 自动接力队列启动 $(date) ====================" >> $LOG

# ---------- 主题链（按顺序；首个等 lighthouse2 成片） ----------
# 格式：tag 帧数 种子
CHAIN=(
  "fried_rice 345 20261040"
)

# ---------- 1) 等灯塔 v2 成片（正在跑的） ----------
PREV=lighthouse2
echo "等待 $PREV 成片 ..." >> $LOG
for i in $(seq 1 180); do
  [ -s $B/ComfyUI/output/video/${PREV}_FULL.mp4 ] && { echo "$PREV 成片 ✓ $(date)" >> $LOG; break; }
  sleep 60
done
# 等前一个 run_theme 进程完全退出（避免两个客户端抢同一 ComfyUI）
for i in $(seq 1 30); do
  if ! ps -ef | grep -q "run_theme.sh $PREV"; then echo "$PREV 进程已退出 ✓" >> $LOG; break; fi
  sleep 20
done
sleep 10

# ---------- 2) 逐个跑链上主题 ----------
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
