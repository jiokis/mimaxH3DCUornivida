#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《若娜瓦 · 崩解》15s 压迫感短片 v4 · Ref2VA 官方六段式
v4 修正（对照官方 ref-en.txt 规范 + 用户反馈）：
1. 恢复官方格式：**只有六段**，删掉此前自造的 NEG 块（约束并入 detailed_description/retention_analysis）
2. 天使变身 = <Picture 3> 的旧约天使本身（眼即图3 所绘）；<Picture 4> 的发光红眼**只用于背景天空**
3. 音乐改用官方 <Audio N> + reference 标记引用参考曲风格；编制改**管风琴**
4. 运镜按用户指定重排：大远景背影 → 近景回头斜睨 → 全身 → 转身 → 变形；运镜类型多样
5. 镜头用官方时间戳格式「At 00:0X.XXX, the camera cuts to ...」
参考绑定（全部在图内引用，不建独立 Picture 条目 —— 官方 §2.2）
总帧 358 ≈ 14.9s（7 镜：39/39/39/56/73/73/39）
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Ronova (若娜瓦), the Ruler of Death of Teyvat and one of the Four Shades, whose exact design is shown in <Picture 1> and <Picture 2>, two views of the same character wearing the same costume. She has very long flowing white hair that falls well past her waist, and CRIMSON RED eyes; her skin is pale. She wears an ornate black-and-crimson regalia: a tall crimson crown-piece of pointed spikes and swept blades rising from her head, a fitted black high-collared bodice crossed by crimson ribbons and black straps, long black gloves reaching above her elbows, a crimson and black layered skirt with white lace panels and trailing black ribbons, and long crimson streamers hanging from her shoulders that read as swept feather-blades, each carrying a row of small closed eyes along its length. She has NO headset microphone in this video. Her voice, when she speaks, is a low, level, unhurried woman's voice.
<Subject 2> is the world of this video in two opposed states. In its first state it is a vast sunlit meadow: a wide green grassland under a clear blue sky, tall grass moving in slow waves in a warm breeze, small white clouds drifting high, and soft afternoon sunlight across the field. In its second state the same world has come apart: the blue of the sky is eaten away into flat black-red, the green grass blackens and stiffens into a dead black lawn, the clouds rot into dark stains, and the air fills with fine drifting black ash. In this second state the sky is covered with the large glowing eyes shown in <Picture 4>, repeated at every scale across the whole sky: each eye is a deep black-red sclera, a brilliant glowing crimson iris with a thin bright rim, a narrow dark pupil, thin radiating lines around the iris and a soft crimson glow bleeding outward, drawn as flat cel-shaded shapes with clean dark outlines in the same hand-drawn language as her costume.
<Subject 3> is the final form that <Subject 1>'s own body becomes in this video: the Old Testament angel shown in <Picture 3>, reproduced exactly as it is drawn there, with no human face, no human limbs and no human silhouette left. Its wings, its silhouette, its surface and every detail of its form are taken from <Picture 3> and are not altered, added to or re-described.
<Audio 1> is the music-style and motive reference for the audience-only score of this video: a dark, heavy cue built on a slow tread under a dense stream of fast equal notes with a fast driving pulse and a modal colour centred on E with the minor shade of G. Only its motives, density, pulse and modal colour are referenced; its signal is not copied."""

SUMMARY = """summary:
[reference generation + audio reference] The target video is a single continuous fifteen-second 2D-animated scene in the official Genshin Impact style in which <Subject 1>, Ronova, stands with her back to the lens in a sunlit meadow in <Subject 2>, looks back over her shoulder at the lens, turns her whole body to face it, and then comes apart and transforms into the Old Testament angel of <Picture 3> while <Subject 2> decays from sunlit grassland into a black lawn under a sky packed with the glowing eyes of <Picture 4>. <Subject 1>'s identity and costume come from <Picture 1> and <Picture 2>, the angel form comes from <Picture 3>, the eyes covering the broken sky come from <Picture 4>, and <Audio 1> supplies the motives, density, pulse and modal colour of the score."""

RET = """retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4] and [Shot 5], and up to the moment her head is absorbed in [Shot 6]): fully_preserved - Ronova's identity, her very long flowing white hair, her crimson red eyes, her pale skin, the tall crimson crown-piece of pointed spikes and swept blades, the fitted black high-collared bodice with crimson ribbons and black straps, the long black gloves above the elbow, the crimson and black layered skirt with white lace panels and trailing black ribbons, and the folded crimson feather-blades with their rows of small eyes are retained wherever her human form appears.
<Subject 2> (appears in every shot, in its first sunlit state in [Shot 1] and in its second broken state from [Shot 2] onward): fully_preserved - the same grassland and the same sky are carried through both states; in the second state the sky carries the glowing eyes of <Picture 4> repeated at many sizes.
<Subject 3> (appears in [Shot 6] and [Shot 7] as the final state of <Subject 1>'s own body): fully_preserved - the Old Testament angel of <Picture 3> is retained exactly as drawn there, with its wings, its silhouette and every detail of its form unchanged.
<Audio 1>: reference - its slow tread, its dense stream of fast equal notes, its fast driving pulse and its modal colour centred on E with the minor shade of G guide the score, without copying the original signal."""

DESC = """detailed_description:
The target video is 2D-animated hand-drawn cel-shaded anime in the official Genshin Impact style: bold clean dark outlines, flat vibrant colour blocking with simple two-tone cel shading, painterly highlights, crisp line art and hard dramatic light, drawn with ink lines and flat colour throughout. Every eye belonging to <Subject 2> is drawn from the eye shown in <Picture 4> as a flat cel-shaded shape with a deep black-red sclera, a glowing crimson iris and a soft bleeding glow. The visual arc runs from clean bright daylight in the opening shots into heavy black-red shadow with deep crushed blacks, so the image grows darker and heavier as the world comes apart. The camera is LOCKED OFF for the whole video: every shot is a static shot, the camera never pans, pushes, tilts, arcs or tracks, and it stays on the same side of her, behind her back, from the first frame to the last. Nothing the audience sees is caused by camera movement - every motion in the frame comes from her own body and from the world coming apart - and the shot scale changes only at the cuts, never inside a shot.
[Shot 1] A wide shot of the first state of <Subject 2> frames the whole sunlit meadow from a low position, with <Subject 1> standing small at the centre of the frame with her back to the lens: her long white hair and the folded crimson feather-blades on her back move slowly in the warm breeze, tall green grass runs away in slow silver waves toward the horizon, and small white clouds drift high in the clear blue sky. Her face is away from the lens and is not the subject of the shot. The camera is a static shot and does not move. The sound is only the soft dry hiss of wind through tall grass and one distant bird. She does not speak.
[Shot 2] At 00:01.625, the camera cuts to a close-up of <Subject 1> from the shoulders up, seen from behind and slightly below: she turns her head back over her shoulder and looks at the lens from the side, her chin held low, her gaze coming to the viewer sidelong from the corners of her crimson eyes without her body moving at all, and her white hair slides across her shoulder as the head comes round. Behind her the first black seam opens in the blue sky and bleeds a dull dark red along its edge, the first blades of her folded wings stir and lift slightly away from her back, and fine black ash begins to drift across the light. The camera does not move at all: it stays where it is, behind her back, and the glance reaches the lens only because her head turns, not because the camera does. The sound is the wind thinning into a low dry rattle and a very low far-off rumble under the ground. Her lips stay closed and she does not speak.
[Shot 3] At 00:03.250, the camera cuts to a full shot of <Subject 1> standing in the meadow of <Subject 2>, shown complete from the crown of her head to her feet, still turned three-quarters away from the lens with one crimson eye visible in profile: her folded blades are now fully lifted and parted behind her shoulders in a dark crimson fan, the small eyes along them opening from the tips inward, and the grass around her feet has already blackened into dead black stalks while the sky behind is half eaten into flat black-red. The camera remains exactly where it was, still behind her, and does not move. The sound is the low rumble rising, a faint dry rustle as the blades part, and a dead, airless silence underneath. Her lips stay closed and she does not speak.
[Shot 4] At 00:04.875, the camera cuts to a medium shot of <Subject 1> from the waist up, from the same low position behind her, and it does not move for the whole shot. Her head is still turned back over her shoulder from the glance of the previous shot; she now lets the turn run down into her body and rotates slowly and evenly on the spot - her shoulders, then her chest, then her hips come round after the head in one slow continuous rotation with no snap and no pause in it - so that the audience, watching from a camera that has not moved at all, sees her back give way to her profile and then to her front as she comes all the way round. By the end of the shot she stands squared to the lens with both crimson eyes clearly readable and open, her brows level and her lips closed and still, and her expression has not changed at all. Behind her the sky is now entirely flat black-red and the grass is a dead black lawn to the horizon. The sound is the low rumble continuing under an airless silence and the light rustle of the blades settling. Her lips stay closed and she does not speak.
[Shot 5] At 00:07.208, the camera cuts to a medium close-up of <Subject 1> from the chest up, and the unfolding begins in earnest: the parted blades spread outward and upward into the first full pair of wings and more blades unfold from behind them layer under layer, each layer larger and wider than the last, so a stack of opening wings rises up behind and above her shoulders in the dark crimson surface and the swept edge of the blades she already wears. Her arms are then absorbed into the mass first - the crimson blades close over them and swallow the black gloves and flared cuffs into the dark crimson surface - while her white-haired head and shoulders remain above the wall of wings and her gaze stays fixed on the lens. Above her, the sky is entirely flat black-red and covered with the glowing eyes of <Picture 4>, and the largest of them begin to turn slowly toward the lens. The camera is locked off and does not move at all: the wings grow outward and upward toward the lens and it is the mass itself that fills the frame, not any camera movement. The sound is a dense low rumble swelling, a dry layered rustle as each new wing unfolds, and a chorus of low voices entering underneath. Her lips stay closed and she does not speak.
[Shot 6] At 00:10.250, the camera cuts to a low shot looking up as the wings now fill and overflow the frame around her: her torso is taken next - the black bodice, the crossed ribbons and the crimson skirt pull apart and run into the same dark crimson surface - so that only her white-haired head and the last of her shoulders are left above the wall of unfolding wings, and then her head is the final human part to go as the tall crown-piece tips slowly back and the head is closed over and absorbed by the wings from behind and above, the white hair drawn into the dark crimson surface last of all, with her gaze held on the lens until the surface closes over her. Only then is what stands there <Subject 3>, the Old Testament angel shown in <Picture 3> and reproduced exactly as it is drawn there - the wings that have been opening all along are its wings - and they keep spreading outward and upward until they fill the sky. Below, the meadow is a dead black lawn to the black horizon. The camera stays locked off and does not move: the mass grows up and outward out of her own position and overflows the frame by itself. The sound is the dense low rumble at its heaviest with a slow heavy wingbeat deep in it and the low voices rising. She does not speak.
[Shot 7] At 00:13.292, the camera cuts to a low static shot on part of the mass of <Subject 3> with the eye-covered black-red sky behind it, and from this cut to the last frame the camera does not move at all: the nearest part of the mass of <Subject 3>, exactly as drawn in <Picture 3>, fills the frame with its wings shifting only slightly, while the dead black lawn below and the packed glowing eyes of <Picture 4> in the sky above both remain visible at the edges of the frame. The camera holds its locked static shot without a single movement, so the pressure holds without release. The sound is the low rumble and the low voices holding a single sustained note that does not resolve. Nothing speaks."""

SOUND = """overall_soundscape:
An open, airy meadow becomes a sealed, airless, low space. [Shot 1] only the soft dry hiss of wind through tall grass and one distant bird, with the air wide and open. [Shot 2] the wind thinning into a low dry rattle, a faint crackle as the grass stiffens black, a soft dry stir as her folded blades lift, and a very low far-off rumble coming up under the ground. [Shot 3] the rumble rising, a faint dry rustle as the blades part, and a dead airless silence underneath. [Shot 4] the low rumble continuing under the silence and the light rustle of the blades settling. [Shot 5] a dense low rumble swelling, a dry layered rustle as each new wing unfolds, and fine ash drifting audibly past. [Shot 6] the rumble at its heaviest with a slow heavy wingbeat deep in it and the layered rustle of the wings closing over her. [Shot 7] the rumble and a single unbroken low tone holding without resolving, and nothing else at all."""

MUSIC = """non_diegetic_music:
One complete piece of audience-only score runs through the whole video, written as a single continuous escalation with a clear opening, a turning point, a transformation and a held final chord, and played on a large pipe organ with its full pedal division and a low male choir over it. Its motives, its density, its pulse and its modal colour centred on E with the minor shade of G follow <Audio 1>, while its instrumentation is the organ rather than an orchestra.
- Opening ([Shot 1]): one thin high organ stop alone in the upper register, widely spaced single notes over a barely audible low pedal point; there is no pulse and the dynamics are piano, so the daylight is empty and open.
- Turning point ([Shot 2], [Shot 3] and [Shot 4]): the pedals enter with a slow heavy tread and the manuals add a quiet repeated figure, and this figure TIGHTENS IN STEP WITH THE TURN AND THE GLANCE: it stays most sparse through the glance in [Shot 2], adds one note as the blades part in [Shot 3], and takes hold properly as the body completes the rotation in [Shot 4], settling into a steady tread at the moment her gaze locks; the dynamics rise to mezzo-piano.
- Unfolding ([Shot 5] and [Shot 6]): the manuals break into a dense continuous stream of fast repeated notes at roughly nine attacks per second, with fast driving pulses near 188 beats per minute, over full pedals that roll under each new layer of wings in step with the picture; the organ adds thick added-note clusters and the low male choir enters on one sustained note; each time a new layer of wings opens, one more rank is drawn and the register climbs, so the organ thickens exactly as the wings do; the dynamics rise through forte and the texture is at its fullest as her head is absorbed.
- Held ending ([Shot 7]): the fast figures stop and the organ lands on one massive low chord centred on E with the full pedal division and the choir holding it, with no return to the home cadence; this single chord is held without resolving across the final shot and decays naturally over the final two seconds of the video, ending exactly with the frame. The piece is complete in itself and is never cut off."""

content = "\n\n".join([SUBJECTS, SUMMARY, RET, DESC, SOUND, MUSIC]) + "\n"
p = os.path.join(OUT, "ronova_collapse.txt")
open(p, "w", encoding="utf-8").write(content)
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("7 镜 × 358 帧 ≈ 14.9s · 官方六段式 · 管风琴配乐")

# ---------- 对照官方规范自检 ----------
import re
txt = content
print("\n=== ① 官方格式合规（只有六段）===")
secs = re.findall(r"^(subject_definitions|summary|retention_analysis|detailed_description|overall_soundscape|non_diegetic_music):", txt, re.M)
print(f"  段落顺序: {secs}")
print(f"  恰为官方六段: {'✓' if secs == ['subject_definitions','summary','retention_analysis','detailed_description','overall_soundscape','non_diegetic_music'] else '✗'}")
print(f"  非官方 NEG 块: {'已删除 ✓' if 'Keep every frame free of' not in txt else '✗ 仍存在'}")
print(f"  summary 任务类型前缀: {'✓' if txt.split('summary:')[1].strip().startswith('[reference generation + audio reference]') else '✗'}")
print(f"  官方时间戳格式(At 00:0X.XXX, the camera cuts to): {len(re.findall(r'At 00:[0-9]{2}[.][0-9]{3}, the camera cuts to', txt))} 处（应 6）")

print("\n=== ② 参考标签用法（官方 §2.2 不建独立 Picture 条目）===")
print(f"  独立 <Picture N> 条目: {len(re.findall(r'^<Picture [0-9]>', txt, re.M))} 个（应 0）")
print(f"  <Audio 1> 定义: {'✓' if '<Audio 1> is the music-style' in txt else '✗'}")
print(f"  <Audio 1> retention 用 reference 标记: {'✓' if '<Audio 1>: reference' in txt else '✗'}")

print("\n=== ③ 变身 = 图3 旧约天使（图4 只管背景）===")
print(f"  天使取自图3: {'✓' if 'exactly as shown in <Picture 3>' in txt else '✗'}")
print(f"  天使眼即图3所绘: {'✓' if 'including its own eyes as drawn there' in txt else '✗'}")
print(f"  图4 仅用于背景天空: {'✓' if 'the sky is covered with the large glowing eyes shown in <Picture 4>' in txt else '✗'}")
print(f"  误把图4装到天使身上: {'无 ✓' if 'Every eye on this body' not in txt else '✗ 仍存在'}")

print("\n=== ④ 运镜（按你指定）===")
plan = [("[镜1] 大远景含背影", "A wide shot of the first state of <Subject 2>"),
        ("[镜2] 近景回头斜睨", "her gaze coming to the viewer sidelong"),
        ("[镜3] 全身", "a full shot of <Subject 1> standing in the meadow"),
        ("[镜4] 转身", "she turns her whole body to face the lens"),
        ("[镜5-6] 变形", "the unfolding begins in earnest"),
        ("[镜7] 定格压迫", "the pressure holds without release")]
for name, key in plan:
    print(f"  {name}: {'✓' if key in txt else '✗'}")
moves = re.findall(r"camera (pushes in|pulls out|arcs|pedestals up|tilts up|holds a static shot)", txt)
print(f"  运镜类型序列: {moves}")

print("\n=== ⑤ 管风琴配乐 ===")
org = [("管风琴+全踏板+低男声合唱", "a large pipe organ with its full pedal division and a low male choir"),
       ("动机参照 Audio1", "follow <Audio 1>"),
       ("编制为管风琴非交响", "its instrumentation is the organ rather than an orchestra"),
       ("密集音流 9/s", "nine attacks per second"),
       ("急促脉动 188BPM", "188 beats per minute"),
       ("随翼层加厚", "the organ thickens exactly as the wings do"),
       ("悬置不解决+不截断", "held without resolving")]
for name, key in org:
    print(f"  {name}: {'✓' if key in MUSIC else '✗'}")
print(f"  抽象情绪词: {re.findall(r'warmth|melancholy|cozy|peaceful|tender|ominous|eerie', MUSIC) or '无 ✓'}")
