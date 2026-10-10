# MiniMax-H3 NVIDIA 部署整理（本机 + 社区方案）

## 本机环境（RTX 4060 Laptop 8GB）

### 检测结果
| 项 | 状态 |
|---|---|
| GPU | NVIDIA GeForce RTX 4060 Laptop 8GB（nvidia-smi 610.43, CUDA 13.3）|
| WSL | Ubuntu 24.04, WSL2 |
| Anaconda | `C:\PYTHON\anaconda3`（用户路径）|
| GPU 环境 | `envs/comfyui`: **torch 2.7.1+cu126, cuda True, RTX 4060 可用** |
| 其他环境 | `cartoon`: basicsr 1.4.2 + realesrgan（但 torch 2.0.0+cpu）|
| 已装超分库 | comfyui env 有 **spandrel 0.4.2** |

### 关键路径
```
C:\PYTHON\anaconda3\envs\comfyui\python.exe   ← GPU 可用
C:\PYTHON\anaconda3\envs\cartoon\             ← basicsr/realesrgan（CPU torch）
C:\PYTHON\anaconda3\envs\<3DDFAV2/DIFFSRIR/DSenv 等>  ← 图像处理项目
```

### 从 WSL 调用 Windows 侧 python
```bash
/mnt/c/PYTHON/anaconda3/envs/comfyui/python.exe -c "import torch; print(torch.cuda.is_available())"
# → True, RTX 4060
```

### ✅ WSL 侧 ffmpeg 可用（2026-09-29 实测修正）
| 项 | 值 |
|---|---|
| 路径 | **`/usr/bin/ffmpeg` · `/usr/bin/ffprobe`** |
| 版本 | ffmpeg 6.1.1-3ubuntu5（GPL build）|
| 编码器 | libx264 / libx265 / libvpx / aac |
| 实测 | 解 1728×960 h264 + aac 正常；抽帧正常；`volumedetect` 正常 |

> ⚠️ **修正**：此前文档写过「本地没有能解 mp4 的 ffmpeg」——**该结论错误**。
> 根因是最初用 `command -v ffmpeg` 在某个 PATH 环境下探测失败，未复查 `/usr/bin`。
> 教训：探测工具存在性时**同时查 PATH 与常见绝对路径**（`/usr/bin`、`/usr/local/bin`）。

#### 本地质检配方（无需 SSH 上集群）
```bash
# 规格与时长
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate \
        -show_entries format=duration -of default=noprint_wrappers=1 in.mp4

# 抽帧
ffmpeg -v error -ss 5 -i in.mp4 -frames:v 1 -y frame.png

# 联络表（一眼看全片切点/构图/顺序）
ffmpeg -v error -i in.mp4 -vf 'fps=2,scale=288:160,tile=8x6' -frames:v 1 -y sheet.png

# 音频响度（非静音校验）
ffmpeg -hide_banner -i in.mp4 -af volumedetect -f null - 2>&1 | grep mean_volume

# 音轨相关度（成片 vs 音床，PSNR + 相关系数）
ffmpeg -y -v error -i out.mp4 -vn -acodec pcm_s16le -ac 1 a.wav
ffmpeg -y -v error -i base.mp4 -vn -acodec pcm_s16le -ac 1 b.wav
python3 h3_soup/psnr_audio.py a.wav b.wav      # 应 ≥0.999
```

### 音频分析（FLAC 等）工具链
| 途径 | 状态 |
|---|---|
| WSL `/usr/bin/python3` + soundfile | ❌ 未装（可 pip 装）|
| Windows `envs/comfyui/python.exe` + soundfile | ✅ **已装 0.14.0**（自带 libsndfile，可解 FLAC）|
| librosa | ❌ 未装 |
| 逐帧 FFT 分析脚本 | ✅ `h3_soup/analyze_music.py`（numpy+FFT，无需 librosa）|

> ⚠️ Windows python **读不了 `/mnt/d/...` 路径**（含中文更会乱码）。
> 对策：先把文件复制到 WSL 内的 ASCII 相对路径，再用相对路径调用。

## 视频超分（Video2X 调研）

### Video2X 官方部署受阻
- 官方 release 在 GitHub（github.com 直连被墙，镜像全 403/404）
- pip 无 video2x 包
- **结论**：完整 Video2X GUI 需走代理/中转下载，暂缓

### 替代方案（本机 GPU 可直接跑）
| 方案 | 引擎 | 说明 |
|---|---|---|
| Real-ESRGAN 直跑 | spandrel + realesrgan 权重 | 用 comfyui env（GPU），ffmpeg 拆帧→超分→合帧，4x |
| 权重来源 | hf-mirror.com（可达）| `realesrgan-x4plus.pth` 等 |
| 社区 NCNN 引擎 | realesrgan-ncnn-vulkan | 免 torch，需下载二进制（GitHub，受阻）|

### 推荐路线
```
comfyui env (GPU) + pip install realesrgan + hf-mirror 下权重
ffmpeg 拆帧 → realesrgan 逐帧 4x → ffmpeg 合帧（含音轨）
```

## 社区 NVIDIA 部署资料

### 官方/高星项目
| 项目 | Stars | 说明 |
|---|---|---|
| MiniMax-AI/awesome-minimax-h3-integration | ★353 | 官方生态索引，按开发者关注度排序 |
| nkxx188/ComfyUI-MiniMaxH3-Easy | ★728 | 24GB 首选出片，T2V/I2V/首尾帧/参考 |
| AIMixer/ComfyUI_MiniMaxH3_Director | ★1696 | 多段 Director |
| T8mars/comfyui-minimax-h3-audio-T8 | ★1051 | H3 音频专项（lock_source 方案）|
| NikoDemon80/ComfyUI-H3-Motion-Context | ★960 | 上一段末帧+音频前传，长视频衔接 |
| vizart-vj/ComfyUI-MiniMax-H3-LongMedia | - | Native Continuation / Selective Regeneration |
| bbaudio-2025/Comfyui-MiniMax-H3-LatentSplit | - | latent 分割长视频 |
| joeygambino/MiniMax-H3-Multishot-Workflow | - | 多镜头工作流 + audio_lock |
| pmhaidn/ComfyUI-Minimax-H3-Extender | - | H3 扩展 |

### 权重选择（官方指引）
| 精度 | 何时用 |
|---|---|
| bf16 | 原始精度，显存够时的最大质量基线 |
| int8_convrot | 社区 24GB 首选，需 PyTorch cu130（驱动 ≥580）|
| fp8_scaled | 官方说"只有 int8_convrot 用不了时才用" |
| GGUF Q4/Q2 | 12-16GB 路线，有损 |

### 3090 实例已验证配方（配方 H）
```
DiT: MiniMax-H3-Ref2VA-Q4_K_M.gguf (Abiray, 18.49GB, arch 标签 "wan")
TE:  qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors (14.61GB)
VAE: minimax_h3_video_vae_fp16 + minimax_h3_audio_vae_fp32
启动: --lowvram --disable-pinned-memory（绝不用 --novram：TE 落 CPU）
采样: 1024x576 / 124帧 / 20步 / res_multistep + simple / CFG 1.0
耗时: ~11.5 分钟/镜头
```

### 加速手段（社区，注意有损）
| 手段 | 步数 | 有损？ |
|---|---|---|
| Turbo (LightX2V DMD) | 4-8 | 4 步音轨退化；8 步基本追平 |
| PDD (阿里 PAI) | 8 | 需用其设计的 8 步 |
| FastH3 | 4 | 丢纹理最多，仅预览 |
| BlockCache | - | turbo 蒸馏与步缓存是替代关系，不叠加 |

## 双环境差异（3090 vs DCU）
| 项 | 3090 | 海光 DCU |
|---|---|---|
| 量化 | 驱动550→只能 bf16 | int8_convrot 可用 |
| 显存 | 24GB | 64GB |
| 直出分辨率 | 1024×576 上限(OOM) | 1728×960 可行 |
| 半精度 | 正常 | fp16 比 fp32 快 23 倍 |

## 本机下一步（Video2X/超分落地）
1. 用 comfyui env（GPU）跑 Real-ESRGAN：`pip install realesrgan`
2. hf-mirror 下载 realesrgan-x4plus 权重
3. 对 `D:\H3\Furina系列_20260927\rain_coffee_FULL.mp4` 等做 4x 超分
4. 或用 spandrel（已装）加载 Real-ESRGAN 模型
