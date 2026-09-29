# MiniMax-H3 工作流总档（DCU / NVIDIA 双环境）

## 项目概述
基于 MiniMax H3（音视频联合生成模型）的芙宁娜（原神角色）短片生产流水线。
已产出 **15 部成片**（1728×960 / 24fps / 含音轨），跨烹饪/舞台/自然/水神四大题材。

## 目录结构
```
h3_soup/                    核心生产脚本
  run_theme.sh              ★ 单主题流水线（base→切段→二采→音床合流拼接）
  h3_gen_wire_fixed.py      base 生成（点号参考图接线 + 落盘确认）
  twopass_gen.py            二采（1728×960，音轨透传/音床合流）
  auto_chain*.sh            自动接力队列（多主题连跑）
  make_*.py                 提示词生成器（每个题材一个）
  prompts/                  生成的 Ref2VA 六段式提示词
  finals/                   已下载成片
h3_docs/                    本仓库文档
```

## 核心管线（run_theme.sh）
```
1. base 480p 生成：h3_gen_wire.py <prompt> <prefix> 20 <帧数> <seed> simple max furina_single 864 480 dotted
2. 切段：场景检测(select=gt(scene,0.15)) → 就近网格+最小段保护+大段缩124+余量传递
3. 二采：twopass_gen.py → 1728×960 / 4步 / beta / denoise 0.2（每段）
4. 拼接：视频单独 concat(-an) + base 完整音轨(音床)合流 + tpad 补帧（音乐完整不截断）
```

## 关键技术点（踩坑沉淀）

### 1. 帧数网格（H3 硬约束）
- length 必须 `17n+5`：22/39/56/73/90/107/124/141/362...
- **切段丢帧问题**：旧 `grid_floor` 向下取整，362 帧 5-7 段累计丢 2-3 秒（15s→12s）
- **修复**：`grid_nearest`（就近网格）+ 最小段保护(<39并入) + 大段缩到 124（960p 二采安全上限）+ 余量传递
- 960p 二采帧数悬崖：124帧=192s/it，192帧=1504s/it（慢8倍）→ 段必须 ≤124

### 2. 参考图接线（Autogrow 点号陷阱）
- 必须写 `ref_images.ref_image_0`（点号扁平键），嵌套 dict 静默失效零报错
- 验证：`grep -n "ref_images" script.py` 必须出现点号写法

### 3. 音频同步（H3 AV 联合生成）
- **根因**：每段 AAC 编码多 832 采样帧填充 → 4 段累积 96ms 漂移 → concat 后相关度 0.9999→0.34
- **解法**：视频单独 concat(-an) + 音轨用 base 完整音轨(音床)整体合流 + `-shortest`
- 实测相关度 0.9994–1.0000（官方标准区间 0.9985–0.9995）

### 4. 音乐完整收尾
- 提示词 non_diegetic_music 写五段式完整结构（引入→发展→高点→收束），末镜"never cut off"
- 拼接时视频 tpad 补帧对齐音床时长，音乐末音符完整衰减

### 5. base 落盘确认
- ComfyUI status=success 时 SaveVideo 可能只写了 48B 头 → 需轮询文件 >1MB 且连续两次大小相同

### 6. 二采输出序号陷阱
- ComfyUI SaveVideo 检测到 _00001_ 存在会递增到 _00002_ → 重跑后拼接需指向最新序号

### 7. 构图纪律（角色呈现）
- 脸要读得清 → 中景（头占≥1/3）是安全下限；近景/特写最佳
- 必须全景时让角色低头/背身/侧身（"消除全景余地"写法优于"求近景"）
- 镜头写"物理上无法拍全景"（近景+压黑背景+无开阔环境）才能稳定出近景

### 8. 提示词六段式（Ref2VA）
```
subject_definitions / summary / retention_analysis / detailed_description /
overall_soundscape / non_diegetic_music
```
- 表情用物理描述（眉头/嘴角/闭眼/呼吸），禁抽象情绪词
- 每镜：构图+运镜(类型+幅度+速度)+当前声音
- 台词 `(S1)` + `<d>[Chinese] ...</d>`，单块 ≤16 字

## DCU 环境（notebook）
- torch 2.9.0+das.opt1.dtk2604，DCU BW 64GB
- **HIP_VISIBLE_DEVICES=0 必设**（否则算子回退 CPU，HCU=0）
- **--highvram**（cgroup 内存仅 59G，lowvram 会撞顶）
- 半精度架构：fp16 比 fp32 快 23 倍
- 参考图：ComfyUI/input/furina_single.png
- ComfyUI：port 7681，models 在 /root/private_data/h3/models/

## 提示词设计哲学
每个题材定制镜数/运镜/串联逻辑/时长，拒绝模板化：
- 煲汤 6镜16.9s / 咖啡馆 4镜 / 书房 5镜 / 舞台 3镜 / 夜街 4镜
- 花园 4镜 / 湖滨 5镜 / 片场 10镜 / 灯塔v1 5镜 / 灯塔v2 6镜
- 蛋炒饭 9镜 / 功夫茶 8镜 / 雨中咖啡 5镜 / PV 7镜 / 红烧肉 7镜 / 水之环舞 6镜
