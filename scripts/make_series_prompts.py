#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Furina 系列 · 六种编排/艺术形式 提示词生成器（每个题材定制镜数/运镜/串联/时长）
每个主题：Ref2VA 六段式 + 专属分镜表（中文 markdown）。
统一纪律只有一条：全中近景/特写、无大远景、头占画幅大。
"""
import os, json

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storyboards")
os.makedirs(OUT, exist_ok=True)
os.makedirs(SB, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
"""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light. ")

FRAMING = ("The framing discipline for this video is absolute: EVERY shot is a medium shot or a close shot. "
           "There are no wide shots, no full-body shots and no long shots anywhere in this video. Whenever her "
           "face is in shot her head occupies a large part of the frame and is rendered in full detail, with her "
           "pale icy-blue right eye and her deeper violet-blue left eye both clearly readable. There is no camera "
           "shake and no fast cutting inside a shot.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, or a wide or full-body shot.")

# ============ 主题定义（每个都是定制编排） ============
THEMES = []

# ---------- 1 雨天咖啡馆：目光即镜头（4 镜 / 226 帧） ----------
THEMES.append(dict(
    tag="cafe", title="雨天咖啡馆", frames=226,
    concept=("「目光即镜头」：整段模拟一个隔着雨窗看她的陌生人的视线。镜头从窗外雨景开始，横摇穿过玻璃入室，"
             "缓推到她脸上，最后下摇到杯沿蒸汽。用 match cut 让每镜都是上一镜目光的延续 —— 玻璃上的雨滴是贯穿元素。"),
    env=("<Subject 2> is a small warm cafe at dusk in the rain: a dark wooden table by a wide window pane with "
         "rain streaming down the glass and blurring the amber street lights outside, a porcelain cup of coffee "
         "with a rising curl of steam, a small cream pitcher, a folded newspaper, and soft golden pendant lamps "
         "hanging low over the table. Warm amber light fills the room and reflects off the wet window."),
    shots=[
        "A tight close-up on the rain-streaked window pane of <Subject 2>, seen from outside, with no person in frame: rain streams down the glass in bright streaks, each drop catching and smearing the amber street-light blobs beyond, and the warm blurred shape of the cafe interior glows behind the wet glass. One large drop rolls slowly down, gathering smaller drops, and hangs at the sill. The camera is a static shot, holding on the moving rain; the glass and the lights are the whole frame.",
        "A medium close-up through the window, framed from the chest up, seen from slightly outside the glass: <Subject 1> sits at the table inside <Subject 2>, her head and shoulders filling the frame through the rain-streaked pane, her face turned three-quarters away from the lens toward the interior light. Raindrops glint on the glass between her and the camera, softly blurring her edges. She lifts the porcelain cup with both gloved hands and takes a small sip. The camera holds this position for a moment, then tilts and tracks slowly sideways as if the gaze moves along the glass toward the door.",
        "A medium close-up, framed from the collarbone up, seen from her right inside the room: <Subject 1> has turned toward the window and looks up, as if noticing someone looking in; her pale icy-blue right eye and deeper violet-blue left eye are both sharp and readable in the warm lamplight, one lock of platinum hair across her brow. Her expression is quiet, unsurprised, a small private smile forming at the corner of her lips. The camera pushes in with small amplitude at slow speed, closing on her face. She does not speak; her lips part slightly and then close on the smile.",
        "A tight close-up on the porcelain cup and the table, no face in frame: <Subject 1>'s WHITE-gloved right hand rests on the warm cup beside the folded newspaper, and a single curl of steam rises from the coffee and drifts across the amber lamplight; a raindrop slides down the window behind, out of focus. The camera tilts down with small amplitude at slow speed from the steam to the cup rim. The frame holds on the steam and the wet window glow.",
    ],
    snd=("a soft steady patter of rain against the window, the low hiss of the espresso machine somewhere behind, "
         "the small ceramic ring of the cup, and one faint breath; the room tone is warm and close."),
    music=("a slow, warm piano figure with a soft brushed cymbal, unhurried and slightly melancholic; it enters "
           "under the rain in the first shot and holds level through the match cuts."),
    summary=("the target video is a single continuous nine-second scene told as one gaze through a rain-streaked "
             "cafe window: it begins on the rain and the amber lights outside, crosses the glass to <Subject 1> "
             "sipping coffee inside, closes on her noticing the gaze, and ends on the steam of her cup. Four hard-"
             "cut shots of unequal length, each continuing the gaze of the last. <Picture 1> supplies identity and "
             "costume only."),
    sb=("### 分镜表 · 雨天咖啡馆（目光即镜头 / 4 镜 / 9.4s）\n"
        "| 镜 | 时长 | 构图 | 运镜 | 串联逻辑 |\n"
        "|---|---|---|---|---|\n"
        "| 1 | ~2.2s | 窗外雨景特写，无人 | 固定 | 目光起点：雨 + 街灯 |\n"
        "| 2 | ~2.8s | 穿玻璃看她侧脸（中近景） | 侧移横摇 | match cut：雨滴衔接 |\n"
        "| 3 | ~2.6s | 她抬眼看镜头（面部特写） | 缓推 | 对视 = 目光落点 |\n"
        "| 4 | ~1.8s | 杯沿蒸汽特写，无人 | 下摇 | 目光收束于蒸汽 |\n"
        "\n编排意图：镜头=旁观者的眼睛；全程不切人、只切目光的移动方向。雨滴贯穿 4 镜。"),
))

# ---------- 2 烛光书房：烛火节拍（5 镜 / 226 帧） ----------
THEMES.append(dict(
    tag="study", title="烛光书房", frames=226,
    concept=("「烛火节拍」：以烛火的闪烁为节拍器，切点对齐火苗闪动，剪接越来越快形成蒙太奇加速 —— "
             "1.9s/镜递减到 1.2s/镜，最后停在她闭眼的静帧。火光是唯一的运动源。"),
    env=("<Subject 2> is a candlelit study at night: a heavy dark desk scattered with old books, an open leather "
         "journal, a brass inkwell and a fountain pen, and a single tall candle in a brass holder casting a warm "
         "flickering orange pool of light that throws long soft shadows across the room. Deep blue shadows fill "
         "everything beyond the candle's reach."),
    shots=[
        "A tight close-up, low and angled, with no face in frame: the tall candle flame in its brass holder on the desk of <Subject 2> sways slowly and throws moving orange light across the open leather journal and inkwell. Wax drips down the candle's side. The camera is a static shot, holding on the flame and the swaying shadows; the cut comes exactly as the flame dips.",
        "A tight close-up on the open journal and the brass inkwell, seen from above, no face in frame: the flickering candlelight moves across the blank page, and the shadows of the inkwell and pen sway with each flame dip. A fountain pen rests across the page. The camera tilts down a fraction at slow speed. The cut lands on another flame dip.",
        "A medium close-up, framed from the collarbone up, seen from her right: <Subject 1> sits at the desk, the candle flame light moving across her face and platinum hair, her pale icy-blue right eye and deeper violet-blue left eye both catching the warm flicker as she looks up from the page. Her brow is soft, her lips slightly parted. The camera pushes in with small amplitude at slow speed. She does not speak; the flame light is the only motion.",
        "A tight close-up on the writing, no face in frame: <Subject 1>'s WHITE-gloved right hand holds the fountain pen and writes a slow line across the journal page, the brass nib glinting, the ink line following; her BLACK-gloved left hand holds the page flat. The candle flame flutters and the pen pauses, then continues. The camera holds tight on the nib and the ink.",
        "A tight close-up on her face, almost straight on, the candle flame now low and leaning: <Subject 1> stops writing and closes her eyes slowly, the flame light still moving across her closed lids and platinum hair; one long exhale, and her lips press into a quiet line. The camera is a static shot, holding on her face until the frame settles.",
    ],
    snd=("a quiet room tone with the soft crackle of the candle wick, the rustle of the page, the scratch of the "
         "pen, and one slow breath; the cuts land on small quiet pops of the wick."),
    music=("a single low cello line over a soft dark drone, with a plucked note on each page turn; the tempo "
           "tightens slightly across the five shots and then relaxes on the closing face."),
    summary=("the target video is a single continuous nine-second scene told as a candle-flame montage in a dark "
             "study: the flame, the page, her eyes, the pen, and her closing eyes, five hard-cut shots of "
             "decreasing length, each cut landing on a dip of the flame. <Picture 1> supplies identity and costume "
             "only."),
    sb=("### 分镜表 · 烛光书房（烛火节拍 / 5 镜 / 9.4s / 蒙太奇加速）\n"
        "| 镜 | 时长 | 构图 | 运镜 | 节拍 |\n"
        "|---|---|---|---|---|\n"
        "| 1 | ~2.0s | 烛火特写，无人 | 固定 | 起拍 |\n"
        "| 2 | ~1.9s | 俯拍书页+墨水 | 缓下摇 | 火闪一下切 |\n"
        "| 3 | ~1.8s | 她抬眼（火光映眼） | 缓推 | 加速 |\n"
        "| 4 | ~1.6s | 笔尖书写特写 | 固定 | 更紧 |\n"
        "| 5 | ~2.1s | 她闭眼静帧 | 固定 | 收束 |\n"
        "\n编排意图：火光是节拍器，剪接频率递增形成向内的紧张感，最后以闭眼静帧释放。"),
))

# ---------- 3 聚光舞台：光控开合（3 镜 / 141 帧） ----------
THEMES.append(dict(
    tag="stage", title="聚光舞台", frames=141,
    concept=("「光控开合」：聚光灯就是唯一的镜头。光从下扫亮她 → 环绕运镜跟随她唱长音 → 光收窄到她双眼后渐暗。"
             "三段式紧凑结构（5.9s），光即剪辑点。"),
    env=("<Subject 2> is a dark theatre stage: a bare polished wooden stage floor, a single brilliant white-gold "
         "spotlight cutting through thin drifting haze, and deep black emptiness all around. A thin mist of haze "
         "hangs in the light beam and drifts slowly."),
    shots=[
        "A medium close-up, framed from the waist up, seen from slightly below: the stage of <Subject 2> is black; a white-gold spotlight sweeps up from below and catches <Subject 1> standing still, her face and costume snapping into bright relief against the haze, her pale icy-blue right eye and deeper violet-blue left eye both sharp as the light reaches them. Haze drifts across the beam behind her. The camera is a static shot; all motion is the light arriving.",
        "A medium close-up, framed from the collarbone up, the camera slowly orbiting: <Subject 1> sings a single held note in the spotlight, her lips shaping it, her eyes open and readable, and the camera arcs around her face with small amplitude at slow speed so the haze and the black change behind her. The light holds steady on her. Her mouth moves as she sings a wordless phrase.",
        "A tight close-up on her face, straight on: the spotlight narrows until it frames only her eyes and brow, her pale icy-blue right eye and deeper violet-blue left eye glowing in the white-gold light; she closes her eyes and the light fades to black around her face as the frame holds. The camera is a static shot.",
    ],
    snd=("a dead theatre room tone with a faint high ring, the soft movement of her coat, one held vocal note that "
         "carries and decays, and then a long quiet silence as the light dims."),
    music=("a sparse low piano with a soft string swell that enters under the held note and thins to nothing as the "
           "light fades."),
    summary=("the target video is a single continuous six-second scene on a dark stage in which the spotlight is "
             "the only camera language: it sweeps up to light <Subject 1>, she sings one held note while the "
             "camera orbits, and the light narrows to her eyes and fades. Three hard-cut shots. <Picture 1> "
             "supplies identity and costume only."),
    sb=("### 分镜表 · 聚光舞台（光控开合 / 3 镜 / 5.9s / 紧凑三段式）\n"
        "| 镜 | 时长 | 构图 | 运镜 | 光语言 |\n"
        "|---|---|---|---|---|\n"
        "| 1 | ~2.0s | 黑场中光扫亮她（中近景） | 固定 | 光=开场 |\n"
        "| 2 | ~2.4s | 她唱长音，环绕 | 环绕运镜 | 光稳 |\n"
        "| 3 | ~1.5s | 光收窄到双眼 | 固定 | 光=谢幕 |\n"
        "\n编排意图：镜头不动、光动；用光代替剪辑点，制造剧场呼吸感。"),
))

# ---------- 4 霓虹夜街：脚步节拍+倒影（4 镜 / 226 帧） ----------
THEMES.append(dict(
    tag="neon", title="霓虹夜街", frames=226,
    concept=("「脚步节拍 + 倒影」：切点踩在脚步声上；两镜用镜面倒影衔接（积水里的霓虹反射）。"
             "低角度跟拍 + 手持微晃，霓虹颜色作情绪轨（蓝→紫→粉→青）。"),
    env=("<Subject 2> is a narrow night street in the rain-wet city: shopfronts glowing with blue-violet and pink "
         "neon signs, wet asphalt mirroring the coloured light, a few drifting pedestrians out of focus in the "
         "distance, and fine drizzle catching the glow. The palette is deep blue night cut by violet, magenta and "
         "cyan neon."),
    shots=[
        "A tight close-up, low angle at boot height: <Subject 1>'s dark-blue bow-topped ankle boots walk through a shallow puddle on the wet asphalt of <Subject 2>, each step sending a small ripple through a violet neon reflection; water splashes and the neon smears. The camera trucks alongside the boots with small amplitude, slightly handheld, the streetlights and signs washing across the wet ground. No face in frame.",
        "A medium close-up seen as a reflection: the shot is framed on a shop window and a wet puddle mirror where <Subject 1> walks past, her figure doubled in the glass and the water, a magenta neon sign burning behind her reflection; her platinum hair reads as a pale shape against the blue-violet night. The camera is a static shot, holding on the reflections as she crosses them. Her face is seen only in reflection, small but readable.",
        "A tight close-up on her face, straight on: <Subject 1> stops and turns her head to the lens, a magenta neon sign reflecting in her pale icy-blue right eye and a cyan one in her deeper violet-blue left eye, the two colours clearly readable; fine drizzle drifts past the light. She holds the look for a beat. The camera pushes in with small amplitude at slow speed.",
        "A medium close-up, seen from behind at low angle: <Subject 1> turns and walks on down the neon street, the camera following her figure from behind as the blue-violet and pink signs slide past, her coat hem swinging, her silhouette rimmed by cyan light; she does not look back. The camera holds and lets her walk toward the deep blue end of the street.",
    ],
    snd=("the soft hiss of fine rain, the low hum and buzz of the neon signs, footsteps on wet asphalt with a "
         "small splash in the puddle, and the faint ring of her boots; each cut lands on a footstep."),
    music=("a slow, cool synthwave pulse with a soft bass line and a relaxed drum beat, entering with her steps and "
           "riding the neon hum."),
    summary=("the target video is a single continuous nine-second scene on a rainy neon night street told in four "
             "hard-cut shots cut on footsteps: her boots through a puddle, her reflection in glass and water, her "
             "face with two neon colours in her eyes, and her walking away into the blue dark. <Picture 1> "
             "supplies identity and costume only."),
    sb=("### 分镜表 · 霓虹夜街（脚步节拍+倒影 / 4 镜 / 9.4s）\n"
        "| 镜 | 时长 | 构图 | 运镜 | 串联逻辑 |\n"
        "|---|---|---|---|---|\n"
        "| 1 | ~2.0s | 靴子踩水（低角度特写） | 手持跟拍 | 切点=落步 |\n"
        "| 2 | ~2.6s | 玻璃+积水里的倒影 | 固定 | 倒影衔接 |\n"
        "| 3 | ~2.4s | 回眸特写（双眼各映一色霓虹） | 缓推 | 与倒影对视 |\n"
        "| 4 | ~2.4s | 背影走入蓝暗 | 低角度跟随 | 告别 |\n"
        "\n编排意图：脚步是节拍器，倒影是叙事者；颜色从紫→粉→青渐变作情绪轨。"),
))

# ---------- 5 清晨花园：水滴韵脚（4 镜 / 226 帧） ----------
THEMES.append(dict(
    tag="garden", title="清晨花园", frames=226,
    concept=("「水滴韵脚」：每镜的最后一拍都是一颗水滴 —— 滚落、落进掌心、飞散、定格闪亮。"
             "俯拍微距 + 逆光，露珠是贯穿的视觉押韵。"),
    env=("<Subject 2> is a small sunlit garden at early morning: a stone path between flower beds of pale blue and "
         "white blooms, a small brass watering can, dew on every leaf, and soft golden morning light low through a "
         "thin mist. Green and soft gold tones with pale blue flowers."),
    shots=[
        "A tight close-up, seen from above at a shallow angle, no face in frame: a pale blue flower bud in the garden of <Subject 2> carries a large dew drop on its petal; the low golden sun flares softly through the mist behind it. A breeze makes the bloom nod and the dew drop rolls along the petal, hangs at the tip, and falls out of frame. The camera is a static shot, holding on the bloom; the frame ends exactly as the drop falls.",
        "A medium close-up, framed from the chest up, seen from her left: <Subject 1> kneels by the flower bed in the low golden light, reaches out with her WHITE-gloved right hand, and holds her palm beneath a leaf; a dew drop falls from the leaf into her palm and beads there. Her pale icy-blue right eye and deeper violet-blue left eye are both readable in the morning light; she looks down at the drop in her hand. The camera tilts down with small amplitude at slow speed to follow the drop.",
        "A tight close-up on the brass watering can, no face in frame: <Subject 1>'s WHITE-gloved right hand tilts the small brass can and a fine glittering spray falls onto the pale blue blooms in the low backlit sun, each drop flashing as it catches the light; her BLACK-gloved left hand steadies the handle. The camera holds on the falling spray, and the frame ends as one bright drop lands on a petal and beads.",
        "A tight close-up, seen from a low angle, no face in frame: a single dew drop sits on the tip of a pale blue petal in the full morning light, the mist thinning behind it, the whole garden soft and gold; the drop quivers, gathers the light, and holds. The camera pushes in with very small amplitude and holds the drop in sharp focus as the frame ends.",
    ],
    snd=("early-morning birdsong, a soft breeze in the leaves, the light patter of the watering spray, the tiny "
         "tick of a drop landing on a petal, and a faint creak of the can handle."),
    music=("a bright, gentle music-box theme over a soft string pad at a slow tempo; each drop lands on a single "
           "plucked note."),
    summary=("the target video is a single continuous nine-second scene in a sunlit garden told as a chain of "
             "falling drops: a dew drop rolls off a bud, a drop falls into <Subject 1>'s palm, a spray of drops "
             "falls onto the blooms, and a single drop holds on a petal in the light. Four hard-cut shots, each "
             "ending on a drop. <Picture 1> supplies identity and costume only."),
    sb=("### 分镜表 · 清晨花园（水滴韵脚 / 4 镜 / 9.4s）\n"
        "| 镜 | 时长 | 构图 | 运镜 | 韵脚 |\n"
        "|---|---|---|---|---|\n"
        "| 1 | ~2.2s | 花苞露珠（俯拍微距） | 固定 | 露珠滚落 |\n"
        "| 2 | ~2.6s | 她伸手接水（中近景） | 缓下摇 | 水珠落掌心 |\n"
        "| 3 | ~2.4s | 浇水壶逆光喷水（特写） | 固定 | 水珠飞散 |\n"
        "| 4 | ~2.2s | 花瓣尖水珠定格（微距） | 极缓推 | 水珠hold住 |\n"
        "\n编排意图：水滴是每镜的句号，形成循环的诗意节奏。"),
))

# ---------- 6 湖滨黄昏：风的呼吸（5 镜 / 311 帧） ----------
THEMES.append(dict(
    tag="lakeside", title="湖滨黄昏", frames=311,
    concept=("「风的呼吸」：风是贯穿元素，强度变化定节奏 —— 起→强→弱→停→再起。5 镜最长最慢（13s），"
             "长镜感，风的每一次变化都是一个镜头。"),
    env=("<Subject 2> is a lakeside promenade at golden hour: a low stone balustrade beside calm water, the sky "
         "and lake both burning in deep gold and orange, a few distant birds, and a warm evening breeze ruffling "
         "the surface. Warm gold, amber and deep bronze tones."),
    shots=[
        "A tight close-up on <Subject 1>'s face and hair, seen from her right: a first breeze rises and lifts a few strands of her platinum hair across her brow; her pale icy-blue right eye and deeper violet-blue left eye are both readable in the low orange sun. She does not turn; her lips are still. The camera is a static shot, holding on her face as the breeze passes.",
        "A medium close-up of the lake and sky seen over the stone balustrade, no person in frame: the wind ruffles the water in long bright streaks of gold, the orange sky burns above, and a few distant birds cross the light; the wind strengthens and the streaks ripple wider. The camera is a static shot, a long hold on the water and the light.",
        "A medium close-up, framed from the chest up, seen from her left: the wind now stronger presses her coat against her, and she lifts her WHITE-gloved right hand to hold the brim of her dark-navy hat as the gold light catches the crown's spikes; her lips press and her eyes narrow against the breeze, both eyes still readable. The camera tilts up with small amplitude at slow speed, following her hand to the hat.",
        "A tight close-up on her face, straight on: the wind has dropped; the lake behind her is almost flat, the orange light settling. She lets her hand down slowly, opens her eyes fully, and looks out across the water with a quiet, unreadable calm. The camera pushes in with small amplitude at very slow speed, ending close on her eyes.",
        "A medium close-up, seen from behind at low angle: the wind rises again as <Subject 1> turns and walks away along the balustrade, her platinum hair lifting, her coat hem swinging, the low orange sun flaring gently behind her; the camera follows her with a slow lateral move and holds as she walks toward the burning horizon.",
    ],
    snd=("a soft evening breeze building and dropping, the gentle lap of lake water against the stone, a few "
         "distant bird calls, the rustle of her coat, and the small sound of her hand meeting the hat brim."),
    music=("a slow, warm string melody with a soft acoustic guitar; the strings swell as the wind strengthens and "
           "thin as it drops, and the final swell carries her off the frame."),
    summary=("the target video is a single continuous thirteen-second scene on a lakeside promenade at golden "
             "hour told as the breath of the wind: it rises through her hair, ruffles the water, presses her coat "
             "and hat, drops to a calm close-up of her face, and rises again as she walks away. Five hard-cut "
             "shots of unequal length, each keyed to the wind. <Picture 1> supplies identity and costume only."),
    sb=("### 分镜表 · 湖滨黄昏（风的呼吸 / 5 镜 / 13.0s / 最长最慢）\n"
        "| 镜 | 时长 | 构图 | 运镜 | 风的强度 |\n"
        "|---|---|---|---|---|\n"
        "| 1 | ~2.4s | 发丝扬起（面部特写） | 固定 | 风起 |\n"
        "| 2 | ~3.0s | 水面+天空（无人的中景长镜） | 固定长镜 | 风强 |\n"
        "| 3 | ~2.6s | 她按帽檐（中近景） | 缓上摇 | 风最强 |\n"
        "| 4 | ~2.8s | 风停后她的脸（特写） | 极缓推 | 风停 |\n"
        "| 5 | ~2.2s | 背影走入夕阳 | 横向跟随 | 风再起 |\n"
        "\n编排意图：风=全片的呼吸；5 镜对应风的五个强度，形成起承转合的悠远弧线。"),
))

for th in THEMES:
    lines = []
    lines.append(SUBJECTS)
    lines.append("")
    lines.append(th["env"])
    lines.append("")
    lines.append("summary:")
    lines.append(th["summary"])
    lines.append("")
    lines.append("retention_analysis:")
    lines.append("<Subject 1> (appears in full - head, body and face - in the shots where she is present, and as her gloved hands, boots or reflected figure only in the shots where her face is not the subject): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, and the dark-blue bow-topped ankle boots are all retained wherever she appears. She wears no headset microphone in this video.")
    lines.append("<Subject 2> (appears in every shot): fully_preserved - the environment described above is retained throughout, with its light and atmosphere as the dominant visual character.")
    lines.append("")
    lines.append("detailed_description:")
    lines.append(STYLE + th["env"] + " " + FRAMING)
    for i, s in enumerate(th["shots"]):
        lines.append("[Shot %d] %s" % (i + 1, s))
    lines.append("")
    lines.append("overall_soundscape:")
    lines.append(th["snd"])
    lines.append("")
    lines.append("non_diegetic_music:")
    lines.append(th["music"])
    lines.append("")
    lines.append(NEG)
    p = os.path.join(OUT, "series_%s.txt" % th["tag"])
    open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    # 分镜表
    sb_path = os.path.join(SB, "storyboard_%s.md" % th["tag"])
    open(sb_path, "w", encoding="utf-8").write(th["sb"] + "\n")
    print("wrote %-36s %5d B  [%s · %d镜 · %s]" % (os.path.basename(p), os.path.getsize(p),
          th["title"], len(th["shots"]), "%.1fs" % (th["frames"] / 24.0)))
print("\n分镜表已写入 storyboards/")
