#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《若娜瓦 · 崩解》15s 压迫感短片 v2 · Ref2VA 六段式
v2 修正（用户反馈）：
1. 转身节奏 → 拆成两镜，明确「静→仅头转→定住侧脸→肩躯干跟进→锁定」五拍节奏
2. 背景眼睛 → 参照 <Picture 1>/<Picture 2> 中她翅膀上的**手绘风格化眼**
   （平涂 cel-shaded + 干净描边 + 平面暗红虹膜 + 月牙高光），删除所有写实眼描述
角色：若娜瓦（Ronova），死之执政，四影之一
参考：<Picture 1>+<Picture 2> = 人形外观（同角色两视角，肩后飘带带成排小眼）
      <Picture 3> = 旧约天使终态
剧情：蓝天草地 → 现实溶解崩解 → 天空满布暗红眼 + 黑色草坪
配乐参照《苍白的骑行 O Mors》：厚重低频交响 / 9.6 起音每秒密集音流 / ~187BPM / E 心 + G 小调色彩
总帧 362 = 5+17×21，约 15.08 秒，7 镜
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Ronova (若娜瓦), the Ruler of Death of Teyvat and one of the Four Shades, whose exact design is shown in <Picture 1> and <Picture 2>, two views of the same character wearing the same costume. She has very long flowing white hair that falls well past her waist, and CRIMSON RED eyes; her skin is pale. She wears an ornate black-and-crimson regalia: a tall crimson crown-piece of pointed spikes and swept blades rising from her head, a fitted black high-collared bodice crossed by crimson ribbons and black straps, long black gloves reaching above her elbows, a crimson and black layered skirt with white lace panels and trailing black ribbons, and long crimson streamers hanging from her shoulders. These shoulder streamers are not plain cloth: they read as swept feather-blades, and along their length they carry a row of small crimson EYES, drawn exactly as they appear in <Picture 1> and <Picture 2> - each one a flat cel-shaded drawn shape with a clean dark outline, a flat dark-red iris and a simple crescent highlight, matching the line art and flat colour of the rest of her design. She has NO headset microphone in this video. Her voice, when she speaks, is a low, level, unhurried woman's voice.
<Subject 2> is the world of this video in two opposed states. In its first state it is a vast sunlit meadow: a wide green grassland under a clear blue sky, tall grass moving in slow waves in a warm breeze, small white clouds drifting high, and soft afternoon sunlight across the field. In its second state the same world has come apart: the blue of the sky is eaten away into a flat black-red, the green grass blackens and stiffens into a dead black lawn, the clouds rot into dark stains, and the air fills with fine drifting black ash. In this second state the sky is also covered with the SAME drawn eyes that run along her shoulder streamers in <Picture 1> and <Picture 2>, repeated at every scale across the whole sky - flat cel-shaded drawn eyes with clean dark outlines and flat dark-red irises, drawn in the same line art and flat colour as her costume.
<Subject 3> is the final form that <Subject 1>'s own body becomes in this video, exactly as shown in <Picture 3>: an Old Testament angel, a colossal dark-crimson mass of folded and unfolding wings in which many dark-red eyes of different sizes open and turn, with no human face, no human limbs and no human silhouette left - only the winged, many-eyed body. Every eye on this body is the same drawn eye as the ones on her shoulder streamers in <Picture 1> and <Picture 2>: a flat cel-shaded shape with a clean dark outline, a flat dark-red iris and a simple crescent highlight, drawn in the same line art and flat colour as the rest of the design."""

STYLE = ("The target video is 2D-animated hand-drawn cel-shaded anime in the official Genshin Impact style: bold "
         "clean dark outlines, flat vibrant colour blocking with simple two-tone cel shading, painterly highlights "
         "on hair, cloth and metal, crisp line art, and hard dramatic light. This is a hand-drawn 2D animated film "
         "throughout - the character, the meadow and the angel are drawn with ink lines and flat colour. Every eye "
         "in this video, whether on her shoulder streamers, on the angel body or repeated across the sky, is a "
         "DRAWN eye in that same hand-drawn language: a flat cel-shaded shape with a clean dark outline, a flat "
         "dark-red iris and a simple crescent highlight, matching the eyes on her wings in <Picture 1> and "
         "<Picture 2>. The visual arc of the video runs from clean bright daylight cel shading in the opening "
         "shots to heavy black-red shadow with deep crushed blacks as the world comes apart, so the image itself "
         "grows darker and heavier as the video proceeds.")

FRAMING = ("The framing is built for pressure rather than for beauty. Every shot is a medium shot or a medium "
           "close-up; there are no wide establishing shots and no distant landscape views, so the sky and the "
           "grass always press in close behind and around her. From the moment her face turns toward the lens the "
           "camera sits LOW and looks slightly UP at her, and it creeps forward in very slow, very small pushes "
           "that never stop, so she grows slowly larger in the frame and the viewer is made to feel small. In the "
           "final two shots the angel mass and the field of eyes fill and overflow the frame. Her face, whenever "
           "it is toward the lens, has both of her crimson eyes clearly readable. There is no camera shake and no "
           "fast cutting anywhere in this video: every move is slow, even and relentless.")

TIMING = ("The timing of the turn is the spine of this video and it is fixed as a five-beat movement spread "
          "across [Shot 3] and [Shot 4]. [Shot 3] holds the first three beats: for its first third <Subject 1> "
          "stands completely still with her back to the lens and only her hair and her shoulder streamers moving "
          "in the dead air; in its second third her HEAD ALONE begins to rotate and nothing else moves, the chin "
          "crossing her shoulder until her face is seen in profile; and in its final third the rotation stops "
          "dead and holds in profile, her face half toward the lens, and she does not blink. [Shot 4] holds the "
          "last two beats: in its first two thirds her shoulders and then her whole chest and torso follow the "
          "head through and the body rotates as one unit until she faces the lens squarely, with the white hair "
          "and the crimson streamers swinging out and settling behind her; and in its final third the rotation "
          "is complete and she stands perfectly still with both crimson eyes locked into the lens and held there "
          "without a single further movement. At no point does the whole body turn in one continuous motion: the "
          "head always leads, the body always arrives after it, and each phase comes to a full stop before the "
          "next one begins.")

NEG = ("Keep every frame free of storyboard line art, sketch lines, labels, captions, watermarks, on-screen "
       "text, duplicated or mirror-image figures, extra limbs, extra hands and extra fingers, and keep the "
       "rendering hand-drawn cel-shaded anime with flat colour and clean outlines. Every eye is a drawn flat "
       "cel-shaded shape with a clean outline and a flat dark-red iris, drawn in the same hand-drawn language as "
       "her costume, and the field of eyes in the sky is that same drawn eye repeated at many sizes.")

SHOTS = [
 # 1 美景（低角度已埋伏笔）
 "[Shot 1] At 0.0 seconds, a medium shot seen from behind and slightly below, looking up at <Subject 1> from the waist up, standing in the first state of <Subject 2>: her long white hair and the crimson streamers from her shoulders - with their row of small drawn eyes - move slowly in the warm breeze, and beyond her the tall green grass runs away in slow silver waves under the clear blue sky with small white clouds drifting high. She faces away from the lens, so her face is not visible and not the focus. The camera creeps forward with very small amplitude at the slowest speed, so she grows a little larger against the sky. The sound in this shot is only the soft dry hiss of the wind through the tall grass and one distant bird. She does not speak.",
 # 2 崩解开始
 "[Shot 2] At 1.6 seconds, a medium close-up of the tall grass at the right edge of the frame in <Subject 2>, with <Subject 1>'s still back and white hair filling the left side of the frame, seen from slightly below: the grass blades in the near foreground blacken and stiffen into brittle black stalks that spread inward in a slow creeping line, and above them a thin dark seam opens in the blue sky and bleeds a dull dark red along its edge; inside the seam, at this distance, the first few drawn eyes begin to appear as small flat cel-shaded shapes. A faint black ash begins to drift across the light. The camera creeps forward with very small amplitude at the slowest speed, never stopping. The sound in this shot is the wind thinning into a low dry rattle and a very low far-off rumble under the ground. She does not speak.",
 # 3 转身前半：静→仅头转→定住侧脸（三拍）
 "[Shot 3] At 3.4 seconds, the camera sits LOW and looks up at <Subject 1> in a medium close-up from the chest up, still from behind. The turn begins as a controlled three-beat movement and each beat is separated by a full stop: for the first third of this shot she is completely motionless with her back to the lens while only her hair and her shoulder streamers drift in the dead air; in the second third her HEAD ALONE turns - her neck rotates and the chin crosses her shoulder, the white hair sliding across her collar, while her shoulders and her back stay exactly where they are; and in the final third the head rotation stops dead and holds in profile, so only the edge of her face and one crimson eye are visible against the black-red sky. She does not blink during the hold. Behind her the sky is now half eaten into flat black-red and the grass is black to the horizon, and the drawn eyes packed into the sky can be seen clearly. The camera creeps forward with very small amplitude at the slowest speed throughout all three beats. The sound in this shot is the low rumble rising under a dead, airless silence. She does not speak.",
 # 4 转身后半：肩躯干跟进→转正→锁定（两拍）
 "[Shot 4] At 5.6 seconds, the camera sits LOW and looks up at <Subject 1> in a medium close-up from the chest up, continuing directly from the held profile at the end of the previous shot. In the first two thirds of this shot her shoulders and then her whole chest and torso follow the head: the rotation travels down through her shoulders and her ribs, the crimson streamers and the long white hair swing out and settle behind her, and the body arrives squarely facing the lens with both crimson eyes clearly readable and open, her brows level, her lips closed and still; her expression does not change at all. In the final third the rotation is complete and she is perfectly still, her gaze locked into the lens, held without a single further movement. The camera creeps forward with very small amplitude at the slowest speed. The sound in this shot is the low rumble continuing under an airless silence. She does not speak; her lips stay closed.",
 # 5 溶解
 "[Shot 5] At 8.0 seconds, the camera sits LOW and looks up at <Subject 1> in a medium close-up: as she holds her gaze into the lens, her body begins to come apart - the edges of her sleeves, her trailing ribbons and the ends of her white hair break into dark red motes and fine black mist that lift upward off her, and her outline deforms and rises as the solid shape of her shoulders and arms loses its edge and swells into something much larger. Her crimson eyes stay fixed on the lens and do not blink as the surface around them dissolves. Above her, the sky is now entirely flat black-red and covered with the drawn eyes repeated at every size, and the largest of them begin to turn slowly and orient toward the lens. The camera creeps forward with very small amplitude at the slowest speed. The sound in this shot is the dense low rumble rising and a chorus of low voices entering underneath. She does not speak.",
 # 6 旧约天使（高潮）
 "[Shot 6] At 11.2 seconds, the camera sits LOW and looks steeply up as <Subject 1>'s transformed body - <Subject 3>, the Old Testament angel of <Picture 3> - now fills and overflows the whole frame: a colossal dark-crimson mass of folded and unfolding wings, covered in many drawn dark-red eyes of different sizes, every one of them a flat cel-shaded shape with a clean outline and a flat dark-red iris in the same hand-drawn language as her costume, all of them turned toward the lens, with no human face and no human body left in it. Above and behind it the entire sky is packed with the same drawn eyes at every scale, slowly turning, and below, the meadow is a dead black lawn stretching to the black horizon with black ash drifting across it. The angel mass breathes and its wings shift with a slow heavy unfolding motion. The camera creeps forward with very small amplitude at the slowest speed. The sound in this shot is the dense low rumble at its heaviest under the low voices. Nothing speaks.",
 # 7 定格压迫
 "[Shot 7] At 14.2 seconds, the camera holds LOW and looks up in a tight medium close-up on part of the angel mass of <Subject 3> with the eye-packed black-red sky behind it: several of the largest drawn dark-red eyes in the nearest wings are fixed directly into the lens and they do not look away, drawn as flat cel-shaded shapes with clean outlines exactly as on her shoulder streamers, the wings shifting only slightly, the black lawn below and the packed drawn eyes above both visible at the edges of the frame. The camera creeps forward with the smallest amplitude in the whole video and the frame stays otherwise still, so the pressure holds without release. The sound in this shot is the low rumble and the low voices holding a single sustained note that does not resolve. Nothing speaks.",
]

RET = """retention_analysis:
<Subject 1> (appears in [Shot 1] seen from behind with her face away from the lens, in [Shot 2], [Shot 3] and [Shot 4] as a medium shot or medium close-up through the turn, and in [Shot 5] as her dissolving body; she remains present in [Shot 6] and [Shot 7] in so far as <Subject 3> is her own transformed body): fully_preserved - Ronova's identity, her very long flowing white hair, her crimson red eyes, her pale skin, the tall crimson crown-piece of pointed spikes and swept blades, the fitted black high-collared bodice with crimson ribbons and black straps, the long black gloves above the elbow, the crimson and black layered skirt with white lace panels and trailing black ribbons, and the long crimson shoulder streamers with their row of small drawn crimson eyes are all retained wherever her human form appears, up to and through the shot where her body dissolves.
<Subject 2> (appears in every shot, in its first sunlit state in [Shot 1] and in its second broken state from [Shot 2] onward): fully_preserved - the same grassland and the same sky are carried through both states: the tall green grass becoming the dead black lawn, the clear blue sky becoming the flat black-red sky, the white clouds becoming dark stains, and the clean afternoon light becoming heavy black-red shadow with drifting black ash; and in the second state the sky carries the same drawn eyes as her shoulder streamers, repeated at many sizes.
<Subject 3> (appears in [Shot 6] and [Shot 7] as the final state of <Subject 1>'s own body, exactly as shown in <Picture 3>): fully_preserved - the colossal dark-crimson winged mass covered in many drawn dark-red eyes of different sizes, with no human face and no human body, is retained exactly as shown in <Picture 3>, with every eye drawn in the same flat cel-shaded hand-drawn language as the eyes on her shoulder streamers in <Picture 1> and <Picture 2>."""

SUMMARY = ("[reference generation] The target video is a single continuous fifteen-second 2D-animated scene in "
           "the official Genshin Impact style, in which <Subject 1>, Ronova the Ruler of Death, stands with her "
           "back to the lens in a sunlit meadow, and then turns - her head first, her body after it, in a "
           "controlled sequence of held beats - and as she comes to face the lens her body dissolves and swells "
           "until what stands there is <Subject 3>, the many-eyed Old Testament angel of <Picture 3>, under a sky "
           "that has filled with the same drawn eyes that run along her shoulder streamers, above a lawn gone "
           "black. The arc is one continuous escalation with no release: uniform green grass and blue sky, then a "
           "black seam opening and spreading, then her slow head-led turn arrested in profile and then carried "
           "through to a locked gaze, then her body breaking into red motes and black mist as the sky fills with "
           "drawn eyes, and finally the angel mass overflowing the frame beneath a sky packed with drawn eyes "
           "that all look into the lens. The camera is always low and looking up from the moment she turns, "
           "creeping forward in a very slow push that never stops. The whole video carries one complete piece of "
           "music that begins thin and high in the daylight and grows into a heavy, dense, dark orchestral mass "
           "with a driving pulse and a low choir, ending on a single sustained low chord that is held without "
           "resolving and decays naturally over the last shot without being cut off. <Picture 1> and <Picture 2> "
           "supply her identity, her costume and the drawn eyes on her shoulder streamers, and <Picture 3> "
           "supplies the exact form of the angel she becomes; none of them serve as a concrete first or last "
           "frame.")

SOUNDSCAPE = """overall_soundscape:
The sound of the video moves from an open, airy meadow into a sealed, airless, low space. [Shot 1] only the soft dry hiss of wind through tall grass and one distant bird, with the air wide and open. [Shot 2] the wind thinning into a low dry rattle, a faint crackle as the grass stiffens black, and a very low far-off rumble coming up under the ground. [Shot 3] the wind and the bird gone entirely - a dead, airless silence with the low rumble rising underneath it, and one soft hair-thin sound as her head turns. [Shot 4] the low rumble continuing under the silence, and the light rustle of her streamers as the body completes the rotation. [Shot 5] a dense low rumble swelling, with fine particles of ash drifting audibly past the microphone. [Shot 6] the rumble at its heaviest with a slow heavy wingbeat deep in it. [Shot 7] the rumble and a single unbroken low tone holding without resolving, and nothing else at all."""

MUSIC = """non_diegetic_music:
One complete piece of music runs through the whole video, written as a single continuous escalation with a clear opening, a turning point, a transformation and a held final chord - not a loop and not a fade-out. Its style and its motives are taken from a dark symphonic funeral-march cue: a very heavy low-register orchestral mass, a dense continuous stream of fast equal notes, a fast driving pulse, and a modal colour centred on E with the minor shade of G. It is scored for low strings and cellos, low brass, timpani, a low male choir and one high shimmering celesta, written only in instruments, register, tempo, texture and dynamics with no mood words.
- Opening ([Shot 1]): one high shimmering celesta figure in the upper register, thin and bright and widely spaced, over a barely audible low string drone; the texture is two voices, the dynamics are piano, and there is no pulse at all - the daylight is empty and open.
- Turning point ([Shot 2], [Shot 3] and [Shot 4]): the low strings enter properly and begin a very slow, very quiet repeated figure, and this figure TIGHTENS IN STEP WITH THE TURN: it holds at its most sparse through the still beat of [Shot 3], adds one note as the head alone turns, holds again through the arrested profile, then takes hold properly as the shoulders follow in [Shot 4] and settles into a steady tread at the moment her gaze locks; the timpani adds a single soft stroke on each shot and the celesta figure moves down a step and repeats; the texture grows to three voices, the dynamics rise to mezzo-piano.
- Transformation ([Shot 5]): the tempo takes hold at a fast driving pulse near 188 beats per minute, the low strings and cellos break into a dense continuous stream of fast equal notes at roughly nine attacks per second, the low brass enters with long heavy chords, the timpani pounds on the beat and the low male choir enters underneath on one sustained note; the dynamics rise through forte and the texture is at its fullest.
- Held ending ([Shot 6] and [Shot 7]): the fast stream of notes stops and the whole orchestra lands together on one massive low chord centred on E, the low male choir holding it, the timpani rolling softly underneath and one high celesta note ringing over the top; this single chord is held without resolving, with no return to the home cadence, and it sustains across both final shots and decays naturally over the final two seconds of the video, ending exactly with the frame. The piece is complete in itself and is never cut off."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING + " " + TIMING,
]
for s in SHOTS:
    lines.append(s)
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "ronova_collapse.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("7 镜 × 362 帧 = 15.08s · 转身五拍节奏 · 全绘制眼")

# ---------- 自检 ----------
import re
allshots = " ".join(SHOTS)
print("\n=== ① 转身节奏（五拍，拆两镜）===")
beats = [("拍1 完全静止（仅发丝动）", "for the first third of this shot she is completely motionless"),
         ("拍2 仅头转", "her HEAD ALONE turns"),
         ("拍3 定住侧脸（不眨眼）", "the head rotation stops dead and holds in profile"),
         ("拍4 肩→胸→躯干跟进", "her shoulders and then her whole chest and torso follow the head"),
         ("拍5 转正锁定不动", "her gaze locked into the lens, held without a single further movement"),
         ("总则：头先领/每拍完全停住", "the head always leads, the body always arrives after it")]
for name, key in beats:
    print(f"  {name}: {'✓' if (key in allshots or key in TIMING) else '✗'}")
print(f"  拆镜: 镜3=前三拍 / 镜4=后两拍: {'✓' if '[Shot 3] and [Shot 4]' in TIMING else '✗'}")

print("\n=== ② 眼睛：参照图1/2 翅膀上的绘制眼（非写实）===")
eye = [("图1/2 翅膀携带成排小眼", "they carry a row of small crimson EYES"),
       ("平涂 cel-shaded + 干净描边", "a flat cel-shaded drawn shape with a clean dark outline"),
       ("平面暗红虹膜 + 月牙高光", "a flat dark-red iris and a simple crescent highlight"),
       ("天空是同款绘制眼重复", "the SAME drawn eyes that run along her shoulder streamers"),
       ("天使体同款绘制眼", "Every eye on this body is the same drawn eye"),
       ("风格锁声明所有眼皆绘制", "Every eye in this video")]
for name, key in eye:
    print(f"  {name}: {'✓' if key in (SUBJECTS + STYLE + NEG + allshots) else '✗'}")
wet = re.findall(r"\bwet\b|\bglassy\b|\bphotographic eyeball\b|lens-like", SUBJECTS + STYLE + allshots + NEG)
print(f"  写实眼词残留: {'无 ✓' if not wet else wet}")

print("\n=== 剧情/压迫感 ===")
for name, key in [("蓝天草地", "clear blue sky with small white clouds"),
                  ("现实崩解", "grass blades in the near foreground blacken"),
                  ("天空满布暗红眼", "the sky is now entirely flat black-red and covered with the drawn eyes"),
                  ("黑色草坪", "the meadow is a dead black lawn"),
                  ("背对镜头", "faces away from the lens"),
                  ("溶解", "her body begins to come apart"),
                  ("旧约天使", "the Old Testament angel of <Picture 3>"),
                  ("低角度仰拍", "sits LOW and looks up"),
                  ("缓慢不停推镜", "creeps forward with very small amplitude at the slowest speed"),
                  ("眼齐视镜头", "all of them turned toward the lens")]:
    print(f"  {name}: {'✓' if (key in allshots or key in FRAMING) else '✗'}")

print("\n=== 配乐（O Mors 动机）===")
print(f"  9/s 密集音流: {'✓' if 'nine attacks per second' in MUSIC else '✗'}")
print(f"  188BPM 脉动: {'✓' if 'near 188 beats per minute' in MUSIC else '✗'}")
print(f"  E 心 + G 小调: {'✓' if 'centred on E with the minor shade of G' in MUSIC else '✗'}")
print(f"  悬置未解决 + 不截断: {'✓' if 'held without resolving' in MUSIC and 'never cut off' in MUSIC else '✗'}")
print(f"  音乐随转身收紧: {'✓' if 'TIGHTENS IN STEP WITH THE TURN' in MUSIC else '✗'}")
