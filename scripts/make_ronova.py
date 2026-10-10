#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《若娜瓦 · 崩解》15s 压迫感短片 · Ref2VA 六段式
角色：若娜瓦（Ronova），死之执政，四影之一
参考绑定：<Picture 1>+<Picture 2> = 人形外观（同角色同服装两个视角）
          <Picture 3> = 旧约天使形态（溶解后的终态）
剧情弧线：风和日丽的蓝天草地 → 现实溶解崩解 → 天空满是暗红瞳孔 + 黑色草坪
动作关键：背对镜头 → 转头带动身体 → 身体逐渐溶解 → 化为旧约天使
核心诉求：压迫感（低角度仰拍 + 缓慢碾压式推镜 + 瞳孔齐视镜头 + 静默）
配乐参照：《苍白的骑行 O Mors》的风格与动机特征
          厚重低频交响 / 9.6 起音每秒的密集音流 / ~187BPM 急促脉动 / E 心 + G 小调色彩
总帧 362 = 5+17×21，约 15.08 秒，6 镜（长镜慢节奏，服务于压迫感）
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Ronova (若娜瓦), the Ruler of Death of Teyvat and one of the Four Shades, whose exact design is shown in <Picture 1> and <Picture 2>, two views of the same character wearing the same costume. She has very long flowing white hair that falls well past her waist, and CRIMSON RED eyes; her skin is pale. She wears an ornate black-and-crimson regalia: a tall crimson crown-piece of pointed spikes and swept blades rising from her head, a fitted black high-collared bodice crossed by crimson ribbons and black straps, long black gloves reaching above her elbows, a crimson and black layered skirt with white lace panels and trailing black ribbons, and long crimson streamers hanging from her shoulders that float like wings behind her. The whole design is built on crimson, black and white, and the crimson shapes on her crown and shoulders read as swept feather-blades. She has NO headset microphone in this video. Her voice, when she speaks, is a low, level, unhurried woman's voice.
<Subject 2> is the world of this video in two opposed states. In its first state it is a vast sunlit meadow: a wide green grassland under a clear blue sky, tall grass moving in slow waves in a warm breeze, small white clouds drifting high, and soft afternoon sunlight pouring across the field. In its second state the same world has come apart: the blue of the sky is eaten away into a flat black-red, the green grass blackens and stiffens into a dead black lawn, the clouds rot into dark stains, and the air fills with fine drifting black ash. The grass and the sky are the same landscape in both states.
<Subject 3> is the final form that <Subject 1>'s own body becomes in this video, exactly as shown in <Picture 3>: an Old Testament angel, a colossal dark-crimson mass of folded and unfolding wings in which many wet dark-red eyes of different sizes open and turn, with no human face, no human limbs and no human silhouette left - only the winged, many-eyed body, its surface glistening and its colour a deep blood red and black."""

STYLE = ("The target video is 2D-animated hand-drawn cel-shaded anime in the official Genshin Impact style: bold "
         "clean dark outlines, flat vibrant colour blocking with simple two-tone cel shading, painterly highlights "
         "on hair, cloth and metal, crisp line art, and hard dramatic light. This is a hand-drawn 2D animated film "
         "throughout - the character, the meadow and the angel are drawn with ink lines and flat colour, never live "
         "action and never photographic. The visual arc of the video runs from clean bright daylight cel shading in "
         "the opening shots to heavy black-red shadow with deep crushed blacks as the world comes apart, so the "
         "image itself grows darker and heavier as the video proceeds.")

FRAMING = ("The framing is built for pressure rather than for beauty. Every shot is a medium shot or a medium "
           "close-up; there are no wide establishing shots and no distant landscape views, so the sky and the "
           "grass always press in close behind and around her. From the moment her face turns toward the lens the "
           "camera sits LOW and looks slightly UP at her, and it creeps forward in very slow, very small pushes "
           "that never stop, so she grows slowly larger in the frame and the viewer is made to feel small. In the "
           "final two shots the angel mass and the field of eyes fill and overflow the frame. Her face, whenever "
           "it is toward the lens, has both of her crimson eyes clearly readable. There is no camera shake and no "
           "fast cutting anywhere in this video: every move is slow, even and relentless.")

NEG = ("Keep every frame free of storyboard line art, sketch lines, labels, captions, watermarks, on-screen "
       "text, duplicated or mirror-image figures, extra limbs, extra hands and extra fingers, and keep the "
       "rendering hand-drawn cel-shaded anime rather than photographic. <Subject 3> is a body of wings and eyes "
       "only: its form is wings, eyes and glistening dark-crimson surface, with the head and the limbs of "
       "<Subject 1> entirely dissolved away, and the field of eyes in the sky is the same eyes repeated.")

SHOTS = [
 # 1 美景（但镜头已低角度，埋压迫伏笔）
 "[Shot 1] At 0.0 seconds, a medium shot seen from behind and slightly below, looking up at <Subject 1> from the waist up, standing in the first state of <Subject 2>: her long white hair and the crimson streamers from her shoulders move slowly in the warm breeze, and beyond her the tall green grass runs away in slow silver waves under the clear blue sky with small white clouds drifting high. She faces away from the lens, so her face is not visible and not the focus. The camera creeps forward with very small amplitude at the slowest speed, so she grows a little larger against the sky. The sound in this shot is only the soft dry hiss of the wind through the tall grass and one distant bird. She does not speak.",
 # 2 异变初现
 "[Shot 2] At 1.6 seconds, a medium close-up of the tall grass at the right edge of the frame in <Subject 2>, with <Subject 1>'s still back and white hair filling the left side of the frame, seen from slightly below: the grass blades in the near foreground blacken and stiffen into brittle black stalks that spread inward in a slow creeping line, and above them a thin dark seam opens in the blue sky and bleeds a dull dark red along its edge. A faint black ash begins to drift across the light. The camera creeps forward with very small amplitude at the slowest speed, never stopping. The sound in this shot is the wind thinning into a low dry rattle and a very low far-off rumble under the ground. She does not speak.",
 # 3 转头带动身体（核心动作）
 "[Shot 3] At 3.9 seconds, the camera sits LOW and looks up at <Subject 1> in a medium close-up from the chest up: she begins to turn toward the lens, and the turn is led by her head - her head rotates first and her shoulders and then her whole torso follow through after it, so the white hair and the crimson streamers swing around her and settle as the rotation completes. Her face comes into frame with both crimson eyes clearly readable and open, her brows level, her lips closed and still; her expression does not change at all as she looks into the lens. Behind her the sky is now half eaten into flat black-red and the grass is black to the horizon. The camera creeps forward with very small amplitude at the slowest speed throughout the turn. The sound in this shot is the low rumble rising under a dead, airless silence. She does not speak; her lips stay closed.",
 # 4 身体溶解
 "[Shot 4] At 6.9 seconds, the camera sits LOW and looks up at <Subject 1> in a medium close-up: as she holds her gaze into the lens, her body begins to come apart - the edges of her sleeves, her trailing ribbons and the ends of her white hair break into dark red motes and fine black mist that lift upward off her, and her outline deforms and rises as the solid shape of her shoulders and arms loses its edge and swells into something much larger. Her crimson eyes stay fixed on the lens and do not blink as the surface around them dissolves. Above her, the black-red sky begins to open with wet dark-red eyes of different sizes that turn slowly and orient toward the lens. The camera creeps forward with very small amplitude at the slowest speed. The sound in this shot is the dense low rumble rising and a chorus of low voices entering underneath. She does not speak.",
 # 5 旧约天使（高潮）
 "[Shot 5] At 9.9 seconds, the camera sits LOW and looks steeply up as <Subject 1>'s transformed body - <Subject 3>, the Old Testament angel of <Picture 3> - now fills and overflows the whole frame: a colossal dark-crimson mass of folded and unfolding wings, its surface glistening, covered in many wet dark-red eyes of different sizes, all of them turned toward the lens, with no human face and no human body left in it. Above and behind it the entire sky is filled with the same dark-red eyes packed together and slowly turning, and below, the meadow is a dead black lawn stretching to the black horizon with black ash drifting across it. The angel mass breathes and its wings shift with a slow heavy unfolding motion. The camera creeps forward with very small amplitude at the slowest speed. The sound in this shot is the dense low rumble at its heaviest under the low voices. Nothing speaks.",
 # 6 定格压迫
 "[Shot 6] At 13.6 seconds, the camera holds LOW and looks up in a tight medium close-up on part of the angel mass of <Subject 3> with the eye-filled black-red sky behind it: several of the large wet dark-red eyes in the nearest wings are fixed directly into the lens and they do not look away, the wings shifting only slightly, the black lawn below and the packed eyes above both visible at the edges of the frame. The camera creeps forward with the smallest amplitude in the whole video and the frame stays otherwise still, so the pressure holds without release. The sound in this shot is the low rumble and the low voices holding a single sustained note that does not resolve. Nothing speaks.",
]

RET = """retention_analysis:
<Subject 1> (appears in [Shot 1] seen from behind with her face away from the lens, and in [Shot 2], [Shot 3] and [Shot 4] as a medium or medium close-up; she is present as the transforming body in [Shot 5] and [Shot 6] in so far as <Subject 3> is her own transformed body): fully_preserved - Ronova's identity, her very long flowing white hair, her crimson red eyes, her pale skin, the tall crimson crown-piece of pointed spikes and swept blades, the fitted black high-collared bodice with crimson ribbons and black straps, the long black gloves above the elbow, the crimson and black layered skirt with white lace panels and trailing black ribbons, and the long crimson streamers hanging from her shoulders like swept feather-blades are all retained wherever her human form appears, up to and through the shot where her body dissolves.
<Subject 2> (appears in every shot, in its first sunlit state in [Shot 1] and in its second broken state from [Shot 2] onward): fully_preserved - the same grassland and the same sky are carried through both states: the tall green grass becoming the dead black lawn, the clear blue sky becoming the flat black-red sky, the white clouds becoming dark stains, and the clean afternoon light becoming heavy black-red shadow with drifting black ash.
<Subject 3> (appears in [Shot 5] and [Shot 6] as the final state of <Subject 1>'s own body, exactly as shown in <Picture 3>): fully_preserved - the colossal dark-crimson winged mass covered in many wet dark-red eyes of different sizes, with no human face and no human body, is retained exactly as shown in <Picture 3>."""

SUMMARY = ("[reference generation] The target video is a single continuous fifteen-second 2D-animated scene in "
           "the official Genshin Impact style, in which <Subject 1>, Ronova the Ruler of Death, stands with her "
           "back to the lens in a sunlit meadow and then turns her head, and her body follows the turn and comes "
           "apart, dissolving and swelling until what stands there is <Subject 3>, the many-eyed Old Testament "
           "angel of <Picture 3>, under a sky that has filled with dark red eyes above a lawn gone black. The arc "
           "is one continuous escalation with no release: uniform green grass and blue sky, then a black seam "
           "opening and spreading, then her slow head-led turn into the lens, then her body breaking into red "
           "motes and black mist as the sky opens with eyes, and finally the angel mass overflowing the frame "
           "beneath a sky packed with eyes that all look into the lens. The camera is always low and looking up "
           "from the moment she turns, creeping forward in a very slow push that never stops. The whole video "
           "carries one complete piece of music that begins thin and high in the daylight and grows into a heavy, "
           "dense, dark orchestral mass with a driving pulse and a low choir, ending on a single sustained low "
           "chord that is held without resolving and decays naturally over the last shot without being cut off. "
           "<Picture 1> and <Picture 2> supply her identity and costume, and <Picture 3> supplies the exact form "
           "of the angel she becomes; none of them serve as a concrete first or last frame.")

SOUNDSCAPE = """overall_soundscape:
The sound of the video moves from an open, airy meadow into a sealed, airless, low space. [Shot 1] only the soft dry hiss of wind through tall grass and one distant bird, with the air wide and open. [Shot 2] the wind thinning into a low dry rattle, a faint crackle as the grass stiffens black, and a very low far-off rumble coming up under the ground. [Shot 3] the wind and the bird gone entirely - a dead, airless silence with the low rumble rising underneath it. [Shot 4] a dense low rumble swelling, with fine particles of ash drifting audibly past the microphone. [Shot 5] the rumble at its heaviest with a slow heavy wingbeat deep in it. [Shot 6] the rumble and a single unbroken low tone holding without resolving, and nothing else at all."""

MUSIC = """non_diegetic_music:
One complete piece of music runs through the whole video, written as a single continuous escalation with a clear opening, a turning point, a transformation and a held final chord - not a loop and not a fade-out. Its style and its motives are taken from a dark symphonic funeral-march cue: a very heavy low-register orchestral mass, a dense continuous stream of fast equal notes, a fast driving pulse, and a modal colour centred on E with the minor shade of G. It is scored for low strings and cellos, low brass, timpani, a low male choir and one high shimmering celesta, written only in instruments, register, tempo, texture and dynamics with no mood words.
- Opening ([Shot 1]): one high shimmering celesta figure in the upper register, thin and bright and widely spaced, over a barely audible low string drone; the texture is two voices, the dynamics are piano, and there is no pulse at all - the daylight is empty and open.
- Turning point ([Shot 2] and [Shot 3]): the low strings enter properly and begin a very slow, very quiet repeated figure that tightens as the grass blackens, the timpani adds a single soft stroke on each shot, and the celesta figure moves down a step and starts to repeat; the texture grows to three voices, the dynamics rise to mezzo-piano.
- Transformation ([Shot 4]): the tempo takes hold at a fast driving pulse near 188 beats per minute, the low strings and cellos break into a dense continuous stream of fast equal notes at roughly nine attacks per second, the low brass enters with long heavy chords, the timpani pounds on the beat and the low male choir enters underneath on one sustained note; the dynamics rise through forte and the texture is at its fullest.
- Held ending ([Shot 5] and [Shot 6]): the fast stream of notes stops and the whole orchestra lands together on one massive low chord centred on E, the low male choir holding it, the timpani rolling softly underneath and one high celesta note ringing over the top; this single chord is held without resolving, with no return to the home cadence, and it sustains across the last two shots and decays naturally over the final two seconds of the video, ending exactly with the frame. The piece is complete in itself and is never cut off."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for s in SHOTS:
    lines.append(s)
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "ronova_collapse.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("6 镜 × 362 帧 = 15.08s · 压迫感弧线 · 完整未解决终止")

# ---------- 自检 ----------
import re
allshots = " ".join(SHOTS)
print("\n=== 剧情弧线（你的分镜要求）===")
arc = [("① 蓝天草地美景", "clear blue sky with small white clouds"),
       ("② 现实溶解崩解", "grass blades in the near foreground blacken"),
       ("③ 天空暗红瞳孔", "the black-red sky begins to open with wet dark-red eyes"),
       ("④ 黑色草坪", "the meadow is a dead black lawn"),
       ("⑤ 背对镜头", "faces away from the lens"),
       ("⑥ 转头带动身体", "led by her head - her head rotates first and her shoulders and then her whole torso follow"),
       ("⑦ 身体溶解变化", "her body begins to come apart"),
       ("⑧ 旧约天使形态", "<Subject 3>, the Old Testament angel of <Picture 3>")]
for name, key in arc:
    print(f"  {name}: {'✓' if key in allshots else '✗'}")
print("\n=== 压迫感手段 ===")
opp = [("低角度仰拍", "sits LOW and looks up|LOW and looks slightly UP|from behind and slightly below"),
       ("缓慢不停推镜", "creeps forward with very small amplitude at the slowest speed"),
       ("瞳孔齐视镜头", "all of them turned toward the lens"),
       ("静默段落", "dead, airless silence"),
       ("无快切/无抖动", "no camera shake and no fast cutting"),
       ("天使占满画面", "fills and overflows the whole frame")]
for name, pat in opp:
    print(f"  {name}: {'✓' if re.search(pat, allshots + FRAMING) else '✗'}")
print("\n=== 画风锁（2D 手绘）===")
print(f"  2D/cel-shaded/hand-drawn 声明: {len(re.findall(r'2D-animated|cel-shaded|hand-drawn|2D animated', STYLE + FRAMING + allshots))} 次")
print(f"  摄影语言残留: {re.findall(r'shallow depth of field|bokeh|photographic realism(?! )', STYLE + FRAMING + allshots) or '无 ✓'}")
print("\n=== 配乐（参照 O Mors 风格动机）===")
mus = [("厚重低频交响", "heavy low-register orchestral mass"),
       ("密集音流 9/s", "nine attacks per second"),
       ("急促脉动 ~188BPM", "near 188 beats per minute"),
       ("E 心 + G 小调色彩", "centred on E with the minor shade of G"),
       ("低男声合唱", "low male choir"),
       ("完整不截断", "complete in itself and is never cut off")]
for name, key in mus:
    print(f"  {name}: {'✓' if key in MUSIC else '✗'}")
print(f"  抽象情绪词: {re.findall(r'warmth|melancholy|cozy|peaceful|tender|ominous|eerie|dark and moody', MUSIC) or '无 ✓'}")
print("\n=== 参考图绑定 ===")
print(f"  Picture 1/2 = 人形外观: {'✓' if '<Picture 1> and <Picture 2>' in SUBJECTS else '✗'}")
print(f"  Picture 3 = 旧约天使终态: {'✓' if 'exactly as shown in <Picture 3>' in SUBJECTS else '✗'}")
