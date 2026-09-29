#!/usr/bin/env python3
"""H3 Ref2VA —— 点号路径接线（已按 ComfyUI 源码 build_nested_inputs 修正）
用法: h3_gen_fixed.py <prompt> <prefix> <steps> <len> <seed> <sched> <refsize> <refname> <W> <H>
"""
import json, sys, time, urllib.error, urllib.request
BASE="http://127.0.0.1:7681"
def get(p,t=180):
    with urllib.request.urlopen(BASE+p,timeout=t) as r: return json.loads(r.read().decode())
def post(p,o,t=300):
    q=urllib.request.Request(BASE+p,data=json.dumps(o).encode(),headers={"Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(q,timeout=t) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print("== HTTP %d: %s"%(e.code,e.read().decode()[:3000])); raise SystemExit(1)
def wait_prompt(pid,timeout,poll=20):
    t0=time.time()
    while time.time()-t0<timeout:
        time.sleep(poll)
        try: h=get("/history/%s"%pid,180)
        except Exception: continue
        if pid in h: return h[pid]
        print("  ... %d 分钟"%(int((time.time()-t0)//60)),flush=True)
    return None
pf,PREFIX=sys.argv[1],sys.argv[2]
STEPS,LEN,SEED=int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
SCHED,REFSIZE,REFNAME=sys.argv[6],sys.argv[7],sys.argv[8]
W,H=int(sys.argv[9]),int(sys.argv[10])
WIRING=sys.argv[11] if len(sys.argv)>11 else "dotted"
PROMPT=open(pf,encoding="utf-8").read()
print("== %s | %dx%d | %d帧 | %d步 | %s | ref_size=%s | ref=%s"%(PREFIX,W,H,LEN,STEPS,SCHED,REFSIZE,REFNAME),flush=True)
oi=get("/object_info",300)
def opts(n,k):
    try:
        v=oi[n]["input"]["required"][k]
        if isinstance(v,list) and len(v)>=2 and isinstance(v[1],dict) and "options" in v[1]: return v[1]["options"]
        return v[0]
    except Exception: return []
UNET=[x for x in opts("UNETLoader","unet_name") if "int8" in x and "minimax" in x.lower()]
CLIP=[x for x in opts("CLIPLoader","clip_name") if "qwen3vl" in x]
VAES=[x for x in opts("VAELoader","vae_name") if x.endswith(".safetensors")]
VID=[x for x in VAES if "video_vae" in x]; AUD=[x for x in VAES if "audio_vae" in x]
REF=[x for x in opts("LoadImage","image") if REFNAME in x]
assert UNET and CLIP and VID and AUD and REF,("缺资源",UNET,CLIP,VID,AUD,REF)
print("== REF =",REF,"| WIRING =",WIRING,flush=True)
wf={
 "1":{"class_type":"UNETLoader","inputs":{"unet_name":UNET[0],"weight_dtype":"default"}},
 "2":{"class_type":"CLIPLoader","inputs":{"clip_name":CLIP[0],"type":"minimax","device":"default"}},
 "3":{"class_type":"VAELoader","inputs":{"vae_name":VID[0]}},
 "4":{"class_type":"VAELoader","inputs":{"vae_name":AUD[0]}},
 "5":{"class_type":"LoadImage","inputs":{"image":REF[0]}},
 # ★★★ 点号路径：ComfyUI execution.py:296 build_nested_inputs 只 pop 这种扁平键
 "6":{"class_type":"MiniMaxH3ReferenceToVideo",
      "inputs":{"clip":["2",0],"prompt":PROMPT,"width":W,"height":H,"length":LEN,
                 "ref_image_size":REFSIZE,"vae":["3",0],"audio_vae":["4",0],
                 **({"ref_images.ref_image_0":["5",0]} if WIRING=="dotted"
                    else {"ref_images":{"ref_image_0":["5",0]}})}},
 "7":{"class_type":"KSamplerSelect","inputs":{"sampler_name":"res_multistep"}},
 "10":{"class_type":"RandomNoise","inputs":{"noise_seed":SEED}},
 "8":{"class_type":"BasicScheduler","inputs":{"model":["1",0],"scheduler":SCHED,"steps":STEPS,"denoise":1.0}},
 "9":{"class_type":"BasicGuider","inputs":{"model":["1",0],"conditioning":["6",0]}},
 "11":{"class_type":"SamplerCustomAdvanced","inputs":{"noise":["10",0],"guider":["9",0],"sampler":["7",0],"sigmas":["8",0],"latent_image":["6",1]}},
 "12":{"class_type":"VAEDecode","inputs":{"samples":["11",0],"vae":["3",0]}},
 "13":{"class_type":"VAEDecodeAudio","inputs":{"samples":["11",1],"vae":["4",0]}},
 "14":{"class_type":"CreateVideo","inputs":{"images":["12",0],"audio":["13",0],"fps":24}},
 "15":{"class_type":"SaveVideo","inputs":{"video":["14",0],"filename_prefix":PREFIX,"format":"auto"}},
}
t0=time.time()
r=post("/prompt",{"prompt":wf}); pid=r.get("prompt_id"); print("prompt_id:",pid,flush=True)
rec=wait_prompt(pid,14400)
if rec is None: print("超时"); sys.exit(1)
st=rec.get("status",{}).get("status_str")
print("status:",st,"耗时 %.1f 分钟"%((time.time()-t0)/60))
if st!="success":
    print(json.dumps(rec.get("status",{}),ensure_ascii=False)[:3000]); sys.exit(1)
import os, glob as _glob
# ★ 落盘确认：SaveVideo 异步写，status=success 时文件可能只写了头（48B）。
# 轮询输出文件：存在且大小 >1MB 且连续两次大小相同（写完成）才返回。
def _wait_file(prefix, timeout=600):
    t0 = time.time()
    last = -1
    while time.time() - t0 < timeout:
        files = sorted(_glob.glob("/root/private_data/h3/ComfyUI/output/" + prefix + "*.mp4"))
        if files:
            sz = os.path.getsize(files[-1])
            if sz > 1000000 and sz == last:
                print("  落盘确认: %s (%d B)" % (os.path.basename(files[-1]), sz), flush=True)
                return files[-1]
            last = sz
        time.sleep(10)
    print("!! 落盘超时: %s" % prefix, flush=True)
    return None
_wait_file(PREFIX)

for nid,o in (rec.get("outputs") or {}).items():
    for k,v in o.items(): print("   %s.%s = %s"%(nid,k,json.dumps(v)[:250]))
print("DONE")
