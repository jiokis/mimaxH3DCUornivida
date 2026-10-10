#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《手擀番茄鸡蛋面》15s 做菜编排 · Ref2VA 六段式
修正上一版（蛋糕）的四个问题：
1. 画风：强锁 2D-animated cel-shaded 原神动画风，删除摄影语言（浅景深/bokeh），
   厨具改手绘感（木案板/陶碗/竹擀杖/铁锅），避免被拉向实拍美食纪录片
2. 工序：手擀面全流程闭环，每步必要且不倒序（和面→揉面→炒卤→擀→切→煮→捞→浇→吃）
3. 半身：7 镜半身（胸上/腰上）显角色 + 仅 2 镜手部特写
4. 配乐：完整乐曲（引子→发展→高潮→终止式），末镜终止和弦完全衰减
总帧 362 = 5+17×21，约 15.08 秒，9 镜。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She wears a plain deep-blue apron over the tailcoat, tied at the waist, and her sleeves are pushed up a little above the flared cuffs. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is a warm traditional kitchen drawn in the same anime style: a thick wooden chopping board on a worn wooden counter, a small heap of flour, a handmade ceramic bowl, a clay pot, a bamboo rolling pin, a Chinese cleaver, a pair of long wooden chopsticks, a wire skimmer, a shallow ceramic noodle bowl with a blue painted rim, a small dish of chopped spring onions, two ripe red tomatoes and a small bowl of beaten egg, and an iron wok on a clay stove with a low flame. Behind the counter hang bamboo baskets and dried chillies, a paper window lets in soft late-afternoon light, and thin steam drifts from the pot. The palette is warm wood brown, cream, vivid tomato red, bright egg yellow and fresh spring-onion green. Everything in this kitchen is drawn in flat cel-shaded shapes with clean outlines, not photographed."""

STYLE = ("The target video is 2D-animated hand-drawn cel-shaded anime in the official Genshin Impact style: bold "
         "clean dark outlines, flat vibrant colour blocking with simple two-tone cel shading, painterly highlights "
         "on hair, cloth and metal, crisp line art, and soft volumetric light. This is a hand-drawn 2D animated "
         "film throughout - the character, the kitchen and the food are drawn with ink lines and flat colour, "
         "never live action and never photographic.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, photographic realism, or a wide or establishing shot of the kitchen.")

FRAMING = ("The framing across the nine shots is deliberately weighted towards the character: seven shots are "
           "medium shots or medium close-ups framed from the chest up or the waist up in which <Subject 1> is "
           "clearly present in frame with her upper body, arms and face visible while she works, her head "
           "occupying roughly one third to one half of the frame height, with her pale icy-blue right eye and "
           "deeper violet-blue left eye both clearly readable and her expression shown through specific physical "
           "details of brows, eyes, mouth and breathing; only two shots are tight inserts of her gloved hands and "
           "the food with no face in frame. There are no wide shots, no full-body shots and no establishing shots "
           "of the kitchen anywhere in this video.")

SHOTS = [
 # 1 和面（半身·胸上）工序闭环第1步
 "[Shot 1] A medium shot of <Subject 1> from the chest up, seen from her left, standing at the wooden counter of <Subject 2> in 2D cel-shaded anime style: her head occupies about one third of the frame height, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable, her brows level, her lips pressed in concentration; she has heaped the flour into a mound on the chopping board and made a well in the middle, and she now pours water from the ceramic bowl into the well with her WHITE-gloved right hand while her BLACK-gloved left hand steadies the board, then pushes the flour inward so it breaks into soft shaggy pieces. Her upper body, both arms and the whole board are inside the frame. The camera pushes in with small amplitude at slow speed. The sound in this shot is the soft pour of water and the dry rustle of flour being pushed together. She does not speak; her lips stay pressed.",
 # 2 揉面（半身·腰上）第2步
 "[Shot 2] A medium shot of <Subject 1> from the waist up, seen from her right, at the wooden counter of <Subject 2>: she leans her weight forward and kneads the dough with the heel of her WHITE-gloved right hand, folding it over with her BLACK-gloved left hand and pressing again, so the mass turns and stretches under her palms and the muscles of her shoulders and arms work with each push; her head occupies about one third of the frame height, her face readable, her brows drawn slightly down, her lips parted with the effort of the push. The camera arcs slowly around her with small amplitude at slow speed, keeping her upper body and the dough in frame. The sound in this shot is the soft heavy thud of the dough on wood and her slow breath. She does not speak.",
 # 3 炒卤（半身·胸上）第3步：趁醒面时间做浇头
 "[Shot 3] A medium shot of <Subject 1> from the chest up, seen from her left, at the iron wok on the clay stove of <Subject 2>: her head occupies about one third of the frame height, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable, warm firelight on her face; she tips the chopped tomato into the hot wok with her WHITE-gloved right hand and the pieces hiss and soften, then pours the beaten egg in a thin stream around them with her BLACK-gloved left hand, and folds the egg through the tomato with the spatula so the red and yellow swirl together and a cloud of steam rises past her shoulder. The camera pushes in with small amplitude at slow speed. The sound in this shot is the strong hiss of the tomato hitting the wok, the pour of the egg and the scrape of the spatula. She does not speak.",
 # 4 擀面（半身·胸上）第4步
 "[Shot 4] A medium shot of <Subject 1> from the chest up, seen from her right, at the wooden counter of <Subject 2>: she presses the bamboo rolling pin down with both gloved hands and rolls the rested dough outward in long even strokes, and the dough flattens and widens into a broad pale sheet that grows across the board as her arms extend and draw back; her head occupies about one third of the frame height, her face readable, her eyes following the rolling pin, her lips pressed. The camera trucks right with small amplitude at slow speed, following the lengthening sheet of dough. The sound in this shot is the steady wooden roll of the pin on the board. She does not speak; her lips stay pressed.",
 # 5 切面（手部特写）第5步 —— 唯一允许的手部特写之一
 "[Shot 5] A tight insert of <Subject 1>'s WHITE-gloved right hand rocking the Chinese cleaver down the folded sheet of dough on the chopping board of <Subject 2>, the blade cutting through the layers so a neat row of pale strips falls open, while her BLACK-gloved left hand holds the folded edge back; the cut noodles spring apart and a little loose flour puffs up. The camera pushes in extremely slowly with very small amplitude, following the blade along the fold. The sound in this shot is the fast rhythmic tap of the cleaver on wood and the soft fall of the cut noodles. No face is in frame.",
 # 6 煮面（半身·腰上）第6步
 "[Shot 6] A medium shot of <Subject 1> from the waist up, seen from her left, at the clay pot of <Subject 2>: she drops the fresh noodles into the boiling water with her WHITE-gloved right hand and loosens them with the long wooden chopsticks in her BLACK-gloved left hand so they separate and swirl in the rolling water, and thick steam rises across her chest and shoulder; her head occupies about one third of the frame height, her face readable through the steam, her brows level, her lips pressed. The camera tilts down slowly with small amplitude from her face to the pot and the swirling noodles. The sound in this shot is the hard rolling boil of the water and the light click of the chopsticks. She does not speak.",
 # 7 捞面（手部特写）第7步 —— 唯一允许的手部特写之二
 "[Shot 7] A tight insert of <Subject 1>'s WHITE-gloved right hand lifting the wire skimmer full of noodles out of the pot of <Subject 2> and shaking it once so the water drains off in a thin curtain, while her BLACK-gloved left hand holds the shallow ceramic noodle bowl below to catch them; the noodles settle into the bowl and steam curls up from them. The camera is a static shot, holding on the skimmer, the falling water and the bowl. The sound in this shot is the light splash of draining water and the soft settle of the noodles in the bowl. No face is in frame.",
 # 8 浇卤（半身·胸上，有脸）第8步
 "[Shot 8] A medium shot of <Subject 1> from the chest up, seen almost straight on, at the wooden counter of <Subject 2>: her head occupies about one third of the frame height, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable as she looks down at her work, her brows lifted slightly, her lips curved up at the corners; she pours the red-and-yellow tomato egg sauce from the wok over the noodles with her WHITE-gloved right hand so it spreads across the top and pools at the edge, then scatters the chopped spring onions over it with her BLACK-gloved left hand and the green pieces tumble down onto the red sauce. The camera pushes in with small amplitude at slow speed, keeping her face and the bowl in frame. The sound in this shot is the soft pour of the thick sauce and the light rustle of the spring onions. She does not speak; her lips hold the small smile.",
 # 9 吃面（半身·胸上，有脸）第9步 —— 长落点收尾
 "[Shot 9] A medium close-up of <Subject 1> from the chest up, seen from her right, at the wooden counter of <Subject 2> with the full noodle bowl just below frame: she lifts a long strand of noodles and a piece of tomato and egg with the chopsticks in her WHITE-gloved right hand, blows once across it with her lips pursed, takes it into her mouth and chews slowly, and her brows relax as the corners of her lips curve up into a warm satisfied smile, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable in the soft light as she looks down at the bowl; she gives one small nod. The camera is a static shot holding on her face for the whole final shot, and the cutting releases here after the faster middle shots. She does not speak; her lips hold the smile.",
]

RET = """retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4], [Shot 6], [Shot 8] and [Shot 9] as medium shots from the chest up or the waist up with her upper body, arms and face in frame, and as her gloved hands only in [Shot 5] and [Shot 7] where her face is out of frame): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, the dark-blue bow-topped ankle boots, and the plain deep-blue apron tied at the waist are all retained wherever she appears. She wears no headset microphone in this video.
<Subject 2> (appears in every shot): fully_preserved - the warm traditional kitchen, the thick wooden chopping board, the worn wooden counter, the flour, the ceramic bowl, the clay pot, the bamboo rolling pin, the Chinese cleaver, the wooden chopsticks, the wire skimmer, the ceramic noodle bowl with the blue rim, the dish of spring onions, the tomatoes, the bowl of beaten egg, the iron wok on the clay stove, the bamboo baskets, the dried chillies and the paper window light are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous fifteen-second 2D-animated cooking film "
           "in a warm traditional kitchen, in which <Subject 1>, Furina, makes a bowl of hand-rolled noodles with "
           "tomato and egg sauce in nine shots that follow the real order of the dish without skipping a step: "
           "she mixes the flour and water into a dough, kneads it until it turns smooth, cooks the tomato and egg "
           "sauce in the wok while the dough rests, rolls the dough out into a wide sheet, cuts the sheet into "
           "noodles, boils them, lifts them out into the bowl, pours the sauce over them and scatters spring "
           "onions, and finally eats a mouthful with a warm satisfied smile. Seven of the nine shots are framed "
           "from the chest or waist up so her upper body, arms and face stay visible while she cooks, and only "
           "two shots are close inserts of her hands at the knife and the skimmer. The whole video is hand-drawn "
           "cel-shaded 2D animation, and the cutting moves at a quick even pace with one longer held shot at the "
           "end. It carries one complete piece of music in five phrases that ends with a full cadence whose final "
           "chord decays completely over the last shot without being cut off. <Picture 1> supplies identity and "
           "costume only and never serves as a concrete frame anchor.")

SOUNDSCAPE = """overall_soundscape:
A warm wooden-kitchen room tone throughout - the low bubbling of the pot, a faint crackle of the stove flame and the soft clink of ceramic. [Shot 1] the pour of water into the flour well and the dry rustle of flour being gathered. [Shot 2] the soft heavy thud of the dough on the board and one slow breath. [Shot 3] the strong hiss of tomato into the hot wok, the thin pour of beaten egg and the scrape of the spatula. [Shot 4] the steady wooden roll of the bamboo pin on the board. [Shot 5] the fast rhythmic tap of the cleaver and the soft fall of cut noodles. [Shot 6] the hard rolling boil and the light click of chopsticks in the pot. [Shot 7] the light splash of draining water and the settle of noodles in the bowl. [Shot 8] the soft pour of thick sauce and the light rustle of spring onions. [Shot 9] the small click of chopsticks, one short breath blown across the hot noodles, and the soft sounds of her chewing."""

MUSIC = """non_diegetic_music:
One complete piece of music runs through the whole video, written as a single rounded composition with a clear introduction, a developing middle, a peak and a full closing cadence - not a loop and not a fade. It is scored for a plucked Chinese lute and guzheng, a bamboo flute, a soft hand drum and a warm string pad, written only in instruments, register, tempo, texture and dynamics with no mood words. It sits in a bright pentatonic key and its tempo steps up with the cutting, so the music breathes with the picture.
- Introduction ([Shot 1]): a single low plucked lute note struck twice, answered by one long bamboo flute note and a soft guzheng pluck; the tempo is slow and even, the texture is two voices, the dynamics are piano.
- Development ([Shot 2] and [Shot 3]): the lute settles into a steady walking pluck that keeps the rhythm of the kneading, the guzheng adds a light counter-figure, and the hand drum enters with one soft stroke per shot; the texture grows to three voices, the dynamics rise to mezzo-piano.
- Rolling and cutting ([Shot 4] and [Shot 5]): the tempo steps up, the lute plays a faster repeated figure, the drum moves to a steady pulse on every beat and the flute runs quick ascending pairs above them; the texture is at its fullest, the dynamics rise to mezzo-forte.
- Boiling ([Shot 6] and [Shot 7]): the tempo holds at its fastest with the drum striking one accent on each cut and the string pad entering underneath the lute, and the flute climbs a stepwise line as the noodles rise in the water; the dynamics peak at forte and then begin to ease.
- Sauce and closing cadence ([Shot 8] and [Shot 9]): the drum and the fast lute figure fall away as the sauce is poured, leaving the guzheng, the string pad and the flute, and the piece resolves to its home note in a full closing cadence: the flute holds one long final note over a guzheng pluck that lands on the tonic, and this final chord decays slowly and completely over the last two seconds of the video, ending exactly with the frame. The piece is complete in itself and is never cut off."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for s in SHOTS:
    lines.append(s)
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "noodles.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("9 镜 × 362 帧 = 15.08s · 7 半身 + 2 手部特写 · 完整终止式配乐")

# ---------- 自检 ----------
import re
allshots = " ".join(SHOTS)
print("\n=== 工序闭环（9 步，无断层）===")
steps = [("1 和面", "pours water from the ceramic bowl into the well"),
         ("2 揉面", "kneads the dough with the heel of her WHITE-gloved right hand"),
         ("3 炒卤", "tips the chopped tomato into the hot wok"),
         ("4 擀面", "rolls the rested dough outward in long even strokes"),
         ("5 切面", "rocking the Chinese cleaver down the folded sheet"),
         ("6 煮面", "drops the fresh noodles into the boiling water"),
         ("7 捞面", "lifting the wire skimmer full of noodles out of the pot"),
         ("8 浇卤", "pours the red-and-yellow tomato egg sauce"),
         ("9 吃面", "lifts a long strand of noodles and a piece of tomato")]
for name, key in steps:
    print(f"  {name}: {'✓' if key in allshots else '✗'}")
print("\n=== 半身 vs 手部特写 ===")
half = sum(1 for s in SHOTS if ("from the chest up" in s or "from the waist up" in s))
ins = sum(1 for s in SHOTS if "No face is in frame" in s)
print(f"  半身（胸上/腰上）= {half} 镜；手部特写 = {ins} 镜  ← 目标 7/2")
print("\n=== 画风锁（2D 手绘，无摄影语言）===")
photo_words = ["shallow depth of field", "bokeh", "marble", "stainless steel", "photograph", "documentary", "live action"]
for w in photo_words:
    hit = w in (STYLE + FRAMING + allshots)
    tag = "✗ 仍存在" if (hit and w not in ("photograph", "live action")) else ("✓ 仅作否定声明" if w in (STYLE,) else "✓")
    print(f"  {w}: {tag}")
print(f"  2D-animated 声明次数: {len(re.findall(r'2D-animated|cel-shaded|hand-drawn', STYLE + FRAMING + allshots))}")
print("\n=== 配乐完整性 ===")
for ph in ["Introduction", "Development", "Rolling and cutting", "Boiling", "Sauce and closing cadence"]:
    print(f"  {ph}: {'✓' if ph in MUSIC else '✗'}")
print(f"  full closing cadence（终止式）: {'✓' if 'full closing cadence' in MUSIC else '✗'}")
print(f"  lands on the tonic（落在主音）: {'✓' if 'tonic' in MUSIC else '✗'}")
print(f"  never cut off: {'✓' if 'never cut off' in MUSIC else '✗'}")
print(f"  抽象情绪词: {re.findall(r'warmth|melancholy|cozy|peaceful|tender|nostalgic|sweet|delicious', MUSIC) or '无 ✓'}")
