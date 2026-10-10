#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《草莓奶油蛋糕》15s 快切 · Ref2VA 六段式
针对官方「多参考生成视频」工作流（Lite/Standard / Lite/Plus / Ultra）。
设计要点（用户指定）：
1. 总时长 15 秒 → 362 帧 = 17×21+5；9 镜
2. 画面过渡流畅紧凑 → 全片 match cut（出画形态/运动 = 入画形态/运动）+ 切点落动作峰值
3. 有配乐 → 五段式完整作品，随切点加速，末镜长音完整衰减（never cut off）
4. 流程符合逻辑 → 真实戚风工序不倒序
参考绑定：<Picture 1> 角色卡；若工作流再绑蛋糕参考图见文末 VARIANT。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She wears a plain pastel-blue apron over the tailcoat, tied at the waist, and a thin blue ribbon tying her hair back. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is a bright home pastry kitchen on a sunny morning: a white marble counter with a flour-dusted worktop, a stainless steel stand mixer with a whisk attachment, a wire sieve, a row of eggs in a small bowl, a small bowl of caster sugar, a jug of milk, a block of butter, a bowl of glossy red strawberries, a round cake tin lined with parchment, a piping bag with a star nozzle, and a small decorating turntable. Behind the counter is a warm-toned oven with a glass door and a rack of cooling cakes, and a window with soft morning light pouring across the marble. The palette is clean white, warm cream and vivid strawberry red."""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light, over a bright pastry-kitchen palette of white "
         "marble, cream, pale gold morning light and vivid strawberry red, with shallow depth of field that "
         "throws the background into soft warm bokeh so the mixing, the batter and the cream carry the frame.")

FRAMING = ("The framing mix across the nine shots is deliberately balanced: four shots are tight medium close-ups "
           "or close-ups in which <Subject 1>'s head occupies roughly one third to one half of the frame height "
           "and her face is rendered in full detail, with her pale icy-blue right eye and deeper violet-blue left "
           "eye both clearly readable; and five shots are tight inserts of her gloved hands, the ingredients and "
           "the cake with no face in frame, in which the subject fills the frame and the background falls into "
           "soft warm bokeh. There are no wide shots, no full-body shots and no establishing shots of the whole "
           "kitchen anywhere in this video.")

TRANSITIONS = ("The transition design for this video is absolute and is the point of the whole piece: EVERY cut is "
               "a match cut, built so that the outgoing form or motion of one shot continues directly into the "
               "incoming form or motion of the next shot. The white flour falling from the sieve scatters into "
               "the white of the meringue; the ribbon of egg white pouring from the shell swirls into the swirl "
               "of the whisk; the stiff peak of the meringue becomes the stiff peak of the piped cream; the "
               "circling motion of the folding spatula becomes the circling turn of the decorating turntable; "
               "the batter flowing into the tin becomes the batter rising inside the oven glass. No cut lands on "
               "a static or settled beat: every cut lands at the peak of an action, on the exact frame where the "
               "motion is fastest, so the movement carries across the join and the whole video reads as one "
               "continuous flowing gesture rather than nine separate clips. The rhythm accelerates from shot to "
               "shot through the middle of the video and then releases into one long held final shot.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, or a wide or establishing shot of the kitchen.")

SHOTS = [
 # 1 备料（中景，有脸）— 动作峰值：手伸向面粉
 "[Shot 1] A tight medium close-up of <Subject 1> from the collarbone up, seen from her left, standing at the white marble counter of <Subject 2>: her head occupies about half the frame height, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable, her brows level, the corners of her lips curved up slightly; she sets the last of the ingredients onto the flour-dusted marble with her WHITE-gloved right hand and reaches for the wire sieve, and a puff of flour lifts off the worktop at the exact moment she takes it. The camera pushes in with small amplitude at slow speed. The sound in this shot is the soft clink of the bowl on marble and the small puff of flour. She does not speak; her lips stay closed.",
 # 2 筛粉（特写，无脸）— 入画：白粉落下（match 到蛋白霜的白）
 "[Shot 2] A tight insert, seen from her left, of <Subject 1>'s WHITE-gloved right hand shaking the wire sieve over the marble of <Subject 2>: a soft curtain of white flour falls and piles into a small drifting mound, the fine dust catching the morning light, and her BLACK-gloved left hand steadies the sieve. The camera is a static shot, holding on the falling flour as the mound grows; the cut lands on the frame where the flour is falling fastest. The sound in this shot is the soft dry hiss of the flour falling. No face is in frame.",
 # 3 分离蛋清（特写）— 入画：流动蛋液（match 到打蛋漩涡）
 "[Shot 3] A tight insert of <Subject 1>'s WHITE-gloved right hand cracking an egg against the rim of a small bowl on the marble of <Subject 2> and tipping the shell so the clear white pours out in a smooth ribbon while the yolk stays in the half-shell; her BLACK-gloved left hand holds the other half. The camera pushes in extremely slowly with very small amplitude on the pouring ribbon of egg white; the cut lands as the ribbon is at its longest and thinnest. The sound in this shot is the sharp crack of the shell and the soft wet pour of the white. No face is in frame.",
 # 4 打发蛋白霜（特写）— 入画：白色漩涡 + 起尖（match 到裱花尖端）
 "[Shot 4] A tight insert over the stainless steel bowl of the stand mixer of <Subject 2>: the whisk turns fast and the egg whites swirl into a glossy white foam that climbs the side of the bowl and pulls into a stiff upright peak as the whisk lifts; <Subject 1>'s WHITE-gloved right hand is just visible at the frame edge tilting the bowl. The camera arcs slowly around the bowl with small amplitude at slow speed, following the swirl; the cut lands on the frame where the whisk pulls out the tall peak. The sound in this shot is the rapid mechanical whir of the mixer and the soft pull of the meringue. No face is in frame.",
 # 5 拌面糊（特写）— 入画：圆形翻拌（match 到转盘旋转）
 "[Shot 5] A tight insert of <Subject 1>'s WHITE-gloved right hand folding the meringue into the yolk batter with a flexible spatula in the big bowl on the marble of <Subject 2>, turning the mixture over in slow circles so the white streaks marble through the yellow batter; her BLACK-gloved left hand turns the bowl steadily. The camera is a static shot; the cut lands at the top of a folding circle so the circular motion continues into the next shot. The sound in this shot is the soft wet fold of the spatula through the batter. No face is in frame.",
 # 6 入模（特写）— 入画：面糊流淌（match 到烤箱里隆起）
 "[Shot 6] A tight insert of the lined round cake tin on the marble of <Subject 2>: <Subject 1>'s WHITE-gloved right hand tilts the big bowl and the pale batter pours in a wide smooth ribbon into the tin, spreading and levelling across the parchment while her BLACK-gloved left hand steadies the tin. The camera pushes in with small amplitude at slow speed as the batter fills the tin; the cut lands on the moment the batter reaches the rim and settles. The sound in this shot is the soft heavy pour of the batter. No face is in frame.",
 # 7 烘烤（近景，脸映在烤箱玻璃）— 入画：蛋糕隆起
 "[Shot 7] A tight medium close-up of <Subject 1> kneeling to look into the glass door of the warm oven in <Subject 2>: her head occupies about one third of the frame height and her face is clearly readable, lit warmly from below by the oven light, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable in the glow, her brows lifted in a small pleased expression; in the glass her reflection overlays the cake, which has risen high and domed above the tin with a golden top. The camera pushes in extremely slowly with very small amplitude, closing on the glass; the cut lands as the dome reaches its full height. The sound in this shot is the low hum of the oven and the soft creak of the rack. She does not speak; her lips stay closed.",
 # 8 裱花（中近景，有脸）— 入画：圆周运转（match 到切蛋糕）
 "[Shot 8] A tight medium close-up of <Subject 1> from the collarbone up, seen from her right, at the marble counter of <Subject 2>: her head occupies about half the frame height, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable, her brows drawn slightly down in concentration, her lips pressed, her gaze following the work of her hands; with her WHITE-gloved right hand she pipes a ring of cream from the star nozzle onto the top of the cooled cake as her BLACK-gloved left hand turns the small decorating turntable, so the piped ring curls in a continuous spiral and a sliced strawberry is set into it. The camera arcs slowly around the cake with small amplitude at slow speed, keeping her face and the turning cake in frame; the cut lands at the fastest point of the turn. The sound in this shot is the small hiss of the cream and the soft squeak of the turntable. She does not speak; her lips stay pressed.",
 # 9 品尝（中近景，有脸）— 长落点收尾（音乐完整衰减）
 "[Shot 9] A tight medium close-up of <Subject 1> from the collarbone up, seen almost straight on at the marble counter of <Subject 2>, with the finished cream cake on its stand just below frame: she lifts a fork with a piece of the soft sponge, cream and strawberry on it with her WHITE-gloved right hand, takes it, and closes her eyes to chew slowly; her brows relax, her lips curve up into a satisfied smile around the fork, and her pale icy-blue right eye and deeper violet-blue left eye are both clearly readable when she opens them and looks down at the cake in front of her. The camera is a static shot, holding on her face for the whole final shot; the rhythm releases here after the fast cutting and the frame stays steady. She does not speak; her lips hold the smile.",
]

RET = """retention_analysis:
<Subject 1> (appears in full face in [Shot 1], [Shot 7], [Shot 8] and [Shot 9] as medium or close shots, and as her gloved hands only in [Shot 2], [Shot 3], [Shot 4], [Shot 5] and [Shot 6] where her face is out of frame): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, the dark-blue bow-topped ankle boots, and the plain pastel-blue apron are all retained wherever she appears. She wears no headset microphone in this video.
<Subject 2> (appears in every shot): fully_preserved - the bright pastry kitchen, the white marble counter with flour dusting, the stainless steel stand mixer with the whisk, the wire sieve, the eggs, the caster sugar, the milk, the butter, the bowl of strawberries, the lined round cake tin, the piping bag with the star nozzle, the decorating turntable, the warm-toned oven with the glass door, and the soft morning window light are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous fifteen-second fast-cut pastry film in "
           "a bright home kitchen, in which <Subject 1>, Furina, bakes and decorates a strawberry cream cake in "
           "nine tightly cut shots whose order follows the real process exactly: gathering the ingredients, "
           "sifting the flour, separating the egg white, whipping the meringue to a stiff peak, folding the "
           "meringue into the batter, pouring the batter into the tin, watching the cake rise through the oven "
           "glass, piping a spiral of cream and setting a strawberry, and finally tasting a forkful with a "
           "satisfied closed-eye smile. Every cut is a match cut that carries the outgoing form or motion into "
           "the incoming form or motion and lands at the peak of an action, so the whole video reads as one "
           "continuous flowing gesture, with the cutting accelerating through the middle and releasing into the "
           "long final tasting shot. The whole video carries one continuous piece of music that moves through "
           "five phrases and ends on a long note that decays completely over the last shot without being cut "
           "off. <Picture 1> supplies identity and costume only and never serves as a concrete frame anchor.")

SOUNDSCAPE = """overall_soundscape:
A bright pastry-kitchen room tone throughout - a soft hum of the oven and a faint morning quiet. [Shot 1] the small clink of the bowl on the marble and the soft puff of flour as she takes the sieve. [Shot 2] the dry hiss of the flour falling through the mesh. [Shot 3] the sharp crack of the eggshell and the wet pour of the egg white. [Shot 4] the fast mechanical whir of the stand mixer and the soft pull of the meringue as the whisk lifts. [Shot 5] the soft wet fold of the spatula turning the batter. [Shot 6] the heavy smooth pour of the batter into the tin. [Shot 7] the low hum of the oven through the glass and the small creak of the rack. [Shot 8] the small hiss of the piped cream and the soft squeak of the turntable turning. [Shot 9] the light clink of the fork on the plate, the soft sounds of her chewing, and one small satisfied breath."""

MUSIC = """non_diegetic_music:
One continuous piece of music runs through the entire video in five phrases, scored for a light pizzicato string line, a celesta, a soft brushed drum and a warm string pad, written only in instruments, register, tempo, texture and dynamics - no mood words. It sits in a bright major key and its tempo follows the cutting, so that the music and the picture breathe together.
- Opening phrase ([Shot 1]): a single low pizzicato pluck on the strings, answered by one high celesta note, in a slow and even rhythm; the texture is two voices, the dynamics are piano.
- Gathering phrase ([Shot 2] and [Shot 3]): the pizzicato quickens to a light walking figure in the middle register and the celesta adds short high notes on each cut; the drum enters with a soft brush stroke per shot; the texture grows to three voices, the dynamics rise to mezzo-piano.
- Whipping phrase ([Shot 4] and [Shot 5]): the tempo steps up again, the strings play a fast repeated figure and the drum moves to a steady brushed pulse on each beat, the celesta runs in quick ascending pairs; the dynamics rise to mezzo-forte and the texture is at its fullest, with the string pad entering underneath.
- Rising phrase ([Shot 6] and [Shot 7]): the tempo holds but the drum adds one accented hit on each cut and the strings climb a stepwise figure upward as the batter rises; the dynamics stay at mezzo-forte with a small swell on the dome of the cake.
- Tasting and resolve phrase ([Shot 8] and [Shot 9]): the pizzicato and drum fall away as the cream is piped, leaving the warm string pad and the celesta holding a single sustained high note; the tempo slows and the piece ends with the celesta sounding one last high note and the strings settling onto a low held chord that decays slowly and completely over the final two seconds of the shot, ending exactly with the frame and never cut off."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING + " " + TRANSITIONS,
]
for i, s in enumerate(SHOTS):
    lines.append(s)
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "cake_fastcut.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("9 镜 × 362 帧 = 15.08s · 全 match cut · 五段式完整音乐")

# ---------- 自检 ----------
import re
print("\n=== 工序逻辑（真实烘焙顺序）===")
steps = ["sifting the flour", "separating the egg white", "whipping the meringue",
         "folding the meringue", "pouring the batter", "oven glass",
         "piping a spiral of cream", "tasting a forkful"]
for s in steps:
    print(f"  {s}: {'✓' if s in ' '.join(SHOTS) + SUMMARY else '✗'}")
print("\n=== match cut 过渡链 ===")
pairs = ["flour ... into the white of the meringue", "ribbon of egg white", "peak of the meringue becomes",
         "circling motion of the folding spatula becomes", "batter flowing into the tin becomes"]
for s in pairs:
    print(f"  {s[:46]}: {'✓' if s in TRANSITIONS else '✗'}")
print(f"  切点落动作峰值声明: {'✓' if 'lands at the peak of an action' in TRANSITIONS else '✗'}")
print("\n=== 音乐完整性 ===")
for ph in ["Opening phrase", "Gathering phrase", "Whipping phrase", "Rising phrase", "Tasting and resolve phrase"]:
    print(f"  {ph}: {'✓' if ph in MUSIC else '✗'}")
print(f"  never cut off: {'✓' if 'never cut off' in MUSIC else '✗'}")
print(f"  随切点变速: {'✓' if 'tempo follows the cutting' in MUSIC else '✗'}")
print("\n=== 构图（4 有脸 + 5 工序特写，无全景）===")
faces = sum(1 for s in SHOTS if "clearly readable" in s)
noface = sum(1 for s in SHOTS if "No face is in frame" in s)
print(f"  有脸镜 {faces} / 无脸镜 {noface} / 共 {len(SHOTS)}")
print(f"  抽象情绪词: {re.findall(r'warmth|melancholy|cozy|peaceful|tender|nostalgic|sweet|delicious', MUSIC)}")
print(f"  帧数网格: 362 = 17×21+5 {'✓' if 362 == 17*21+5 else '✗'}")
