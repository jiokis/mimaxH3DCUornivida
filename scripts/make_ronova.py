#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《若娜瓦 · 崩解》15s 压迫感短片 v7 · Ref2VA 官方六段式 —— 骨架重写

v6 之前所有版本都在打补丁，三条主症反复复发。v7 不再修补句子，直接换骨架：

【脊梁1】世界只消解一次（治「反复变黑」）
  旧版镜2→镜6 每镜都宣布「世界又暗了一格」= 同一事件发生五次。
  新版：镜1-2 完好明亮 → 镜3 开始消解 → 镜4 同一场消解结束 → 镜5-7 静止在已死世界里。
  消解是一个事件，用 continuation 措辞（the same single dissolve that began ... finishes），
  而不是分级阶梯。

【脊梁2】镜头只有一个方向（治「运镜不连贯」）
  旧版：推→推→拉→静止→抬→升→推，方向乱摆 + 一次死停。
  新版：镜1/2/3/4/5/7 一律持续往里推（唯一方向）；全片只后退一次，动机硬：
  镜6 天使长出画面、必须看全形状 → 后退揭示。画幅变化交给剪辑（cut），不靠镜头反向运动。

【脊梁3】天使必须有一次完整可读的形状（治「没有图3 旧约天使的形状」）
  旧版镜6/镜7 全是塞满画面 + 极端畸变，剪影被畸变吃掉，形状一秒没看清。
  新版：<Subject 3> 明写剪影几何（**双翼巨墙、横向展开**：中央折羽核 + 左右两片巨大羽翼
  分别向左右张开，每片由逐级加长的羽刃层层叠成，整体远宽于高、铺满画幅宽度）；
  两墙的生长出处 = 她左右两肩原有的两排 blade-streamers；
  镜6 = 干净直筒、拉远、全形入画、零畸变，3.04s（全片最长）；畸变只留镜7 一镜做收尾压迫。

v9 修订（用户看 RunningHub 接线后确认）：
16. 参考图改为 **只用 3 张**：图1(全身) + 图2(近景) + 图3(旧约天使)；**图4(那只写实眼睛)不作参考**，
    背景瞳孔改由提示词用文字描述为「平面赛璐珞动画风 / 游戏插画完成度」
17. 清掉 <Subject 2> 里自相矛盾的写实眼措辞（fine radiating lines = 写实虹膜纹理、
    soft crimson glow = 渲染感辉光），这些与同句的 flat cel-shaded 直接冲突，是往写实漂的原因之一
18. 天使配色改为**浅色羽毛 + 深红根部**（贴合图3 的浅色羽团，也让剪影在黑红天地间可读）
其他：消解 = 一次连续 wash（drains ... at the same rate, no part ahead of any other），不分级阶梯；
     每只眼各自独立（非复眼整体）；图3 遵循度 partially_preserved（沿用形态，剪影细节自由）。

分镜：39/39/39/56/56/73/56 = 358 帧 ≈ 14.917s（全部 17n+5，24fps）
"""
import os
import re

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

# 分镜表：(序号, 交付帧数, 起始秒, 画幅/运动, 一句话职能)
SHOTS = [
    (1, 39, 0.000, "extreme wide / push in", "大远景背影，世界完好"),
    (2, 39, 1.625, "close-up / push in", "肩后回头斜睨"),
    (3, 39, 3.250, "full shot / push in", "全身，消解开始"),
    (4, 56, 4.875, "medium / push in", "转身面向镜头，消解结束"),
    (5, 56, 7.208, "medium / push in", "羽层炸开，手臂被吞"),
    (6, 73, 9.542, "low wide / pull back", "天使全形揭示（干净、零畸变）"),
    (7, 56, 12.583, "low close / push in + 畸变", "收尾压迫"),
]

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Ronova (若娜瓦), the Ruler of Death of Teyvat and one of the Four Shades, whose design is shown in <Picture 1> and <Picture 2>, two views of the same character in the same costume. She has very long flowing white hair falling well past her waist, and CRIMSON RED eyes; her skin is pale. She wears an ornate black-and-crimson regalia: a tall crimson crown-piece of pointed spikes and swept blades on her head, a fitted black high-collared bodice crossed by crimson ribbons and black straps, long black gloves reaching above her elbows, a crimson and black layered skirt with white lace panels and trailing black ribbons, and long crimson blade-streamers hanging from her shoulders that read as swept feather-blades, each carrying a row of small closed eyes along its length. She wears no headset microphone in this video.
<Subject 2> is the world of this video, and it changes exactly once. In its first state it is a vast sunlit meadow: wide green grassland under a clear blue sky, tall grass moving in slow waves in a warm breeze, small white clouds drifting high, soft afternoon sunlight across the field. In its second state the same world is dead: flat black-red sky, stiff black lawn running to a black horizon, clouds gone, fine black ash drifting in the air. The change between the two states is one single dissolve: colour drains out of the whole world in one even wash, the blue of the sky and the green of the grass and the white of the clouds all running out together at the same rate and flowing upward and away, so no part of the world falls ahead of any other. It runs from the moment it starts until it is finished, and then the world stays dead. After the sky has died, dark-red pupils open in it and turn to look down. Each pupil is a single eye drawn in the same flat cel-shaded anime style as the characters of this video: a bold clean dark outline, a flat black-red sclera, an iris of two flat crimson tones with one hard-edged highlight, and a narrow dark pupil, every shape simplified and flat, with the finish of a game illustration and none of the texture of a rendered eye. The sky carries many of these pupils, and each one is its own separate eye with its own outline, its own iris and its own size, standing apart from the others in the sky.
<Subject 3> is the Old Testament angel that <Subject 1>'s body becomes, in the form of <Picture 3>: a being built out of layered feathers and eyes, shaped as a great two-sided wall of feathers, much wider than it is tall. The feathers are pale: white and light grey at their tips, shading to dark crimson at their roots and along the underside of every tier, so the two wings read as pale layered masses banded with crimson against the dead black world. From a core of folded feathers low in the middle, two colossal wings open to the left and to the right, each of them built of tier after tier of feather blades sweeping outward and slightly upward with every tier longer than the one inside it, so the two wings read as two high walls of feathers standing edge to edge across the black lawn and filling the whole width of the world. Its middle is a slowly turning core of feathers wrapped over itself, and the two walls meet there. Eyes open singly all over both walls, scattered one by one among the feathers, small ones near the core and wide ones across the outer sweeps; each eye is its own eye with its own outline and its own flat crimson iris, drawn in the same simplified game-illustration style as the pupils in the sky, and each one opens on its own beat. It is alive: the tiers of both walls keep opening and closing in slow heavy beats, the whole mass breathes and turns slowly on the spot, and the dark surfaces roll as the feathers move. Its two wings grow out of the two rows of crimson blade-streamers that <Subject 1> already wears, the left wall out of the left row and the right wall out of the right row.
<Audio 1> is the music-style and motive reference for the audience-only score of this video: a dark, heavy cue built on a slow tread under a dense stream of fast equal notes with a fast driving pulse and a modal colour centred on E with the minor shade of G. Only its motives, density, pulse and modal colour are referenced; its signal is not copied."""

SUMMARY = """summary:
[reference generation + audio reference] The target video is a single continuous fifteen-second 2D-animated scene in the official Genshin Impact style in which <Subject 1>, Ronova, stands with her back to the lens in the sunlit meadow of <Subject 2>, looks back over her shoulder at the lens, turns her whole body to face it, and comes apart from the inside into the Old Testament angel of <Subject 3> - two great feathered walls of layered tiers covered in singly-set eyes - while <Subject 2> drains its colour in one single dissolve and settles into a dead black landscape under a sky of separate dark-red eyes. <Subject 1>'s identity and costume come from <Picture 1> and <Picture 2>, the angel form comes from <Picture 3>, the pupils in the dead sky are drawn in the same flat game-illustration eye style as everything else, and <Audio 1> supplies the motives, density, pulse and modal colour of the score."""

RET = """retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4] and [Shot 5], and up to the moment her head is absorbed in [Shot 6]): fully_preserved - Ronova's identity, her very long flowing white hair, her crimson red eyes, her pale skin, the tall crimson crown-piece of pointed spikes and swept blades, the fitted black high-collared bodice with crimson ribbons and black straps, the long black gloves above the elbow, the crimson and black layered skirt with white lace panels and trailing black ribbons, and the folded crimson blade-streamers with their rows of small eyes are retained wherever her human form appears.
<Subject 2> (appears in every shot: whole and bright in [Shot 1] and [Shot 2], dissolving through [Shot 3] and [Shot 4], and finished and unchanging from [Shot 5] to [Shot 7]): fully_preserved - the same grassland and the same sky are carried through both states, and the second state carries many separate dark-red eyes in the flat game-illustration style, each one its own eye with its own outline.
<Subject 3> (appears in [Shot 6] and [Shot 7] as the final state of <Subject 1>'s own body): partially_preserved - the Old Testament angel form of <Picture 3> is carried over as a colossal two-sided wall of pale layered feathers banded with dark crimson and filled with singly-set eyes, alive and moving with its tiers and its eyes opening and closing; the exact silhouette and the exact detail of <Picture 3> are free, and the shape written in this prompt is the one to build.
<Audio 1>: reference - its slow tread, its dense stream of fast equal notes, its fast driving pulse and its modal colour centred on E with the minor shade of G guide the score, without copying the original signal."""

DESC = """detailed_description:
The target video is 2D-animated hand-drawn cel-shaded anime in the official Genshin Impact style: bold clean dark outlines, flat vibrant colour blocking with simple two-tone cel shading, painterly highlights, crisp line art and hard dramatic light, drawn with ink lines and flat colour throughout. Three rules hold the whole video together. First, the world of <Subject 2> changes exactly once: it is whole and bright through [Shot 1] and [Shot 2], it dissolves through [Shot 3] and [Shot 4], and it is finished and unchanging from [Shot 5] to [Shot 7], so the collapse is one single event spread over two shots and the dead world after it is a still backdrop. Second, the camera moves in one direction: it pushes in slowly and continuously in [Shot 1], [Shot 2], [Shot 3], [Shot 4], [Shot 5] and [Shot 7], always inward, and it pulls back exactly once, in [Shot 6], because the angel has grown past the frame and its whole shape has to be seen; there is no other backward move in the video, and changes of shot size are made by cutting rather than by reversing the lens. Third, the camera keeps to the side her back faces and never travels around her, so her face comes into view only because she turns to face the lens. The lens is clean and straight from [Shot 1] through [Shot 6], which is what lets the angel's whole silhouette read in [Shot 6]; only in [Shot 7] does the camera go in close on a heavy wide-angle that bends the mass outward past every edge of the frame.
[Shot 1] An extreme wide shot of the sunlit meadow of <Subject 2> from low in the grass, with <Subject 1> standing small at the centre of the frame with her back to the lens: her long white hair and the folded crimson blade-streamers on her back move slowly in the warm breeze, tall green grass runs away in slow silver waves toward the horizon, and small white clouds drift high in a clear blue sky. She is a small dark figure against a bright field, and her face is turned away. The world is whole and bright in this shot: clear blue sky, green grass running to the horizon, clean white clouds, and not one mark of the collapse anywhere in the frame. The camera pushes in with small amplitude at slow speed, closing on her back. The sound is the soft dry hiss of wind through tall grass and one distant bird. She does not speak.
[Shot 2] At 00:01.625, the camera cuts to a close-up of <Subject 1> from the shoulders up, seen from just over her left shoulder and slightly below, and it keeps pushing in with small amplitude at slow speed: she turns her head back over her shoulder and looks at the lens sidelong from the corners of her crimson eyes, chin held low, white hair sliding across her shoulder, while her shoulders and body stay exactly where they were and the world behind her stays whole and bright. The camera arrives on her face at the same slow rate as before, one continuous move across the cut. The sound is the wind thinning into a low dry rattle and a very low far-off rumble coming up under the ground. Her lips stay closed and she does not speak.
[Shot 3] At 00:03.250, the camera cuts to a full shot of <Subject 1> from the crown of her head to her feet, still pushing in with small amplitude at slow speed, and the dissolve begins: colour drains out of the whole world in one even wash, the blue of the sky and the green of the grass and the white of the clouds running out together at the same rate and flowing upward and away, and as the colour goes it leaves flat black-red behind in the sky and dead black behind on the ground, with fine black ash starting to drift. Her blade-streamers lift and part behind her shoulders into a dark crimson fan, and the small eyes set along their edges open one by one from the tips inward. Her body still faces away from the lens and her head stays turned back over her shoulder, so one crimson eye shows in profile. The sound is a single long low rush as the colour drains out, under a dead airless silence. She does not speak.
[Shot 4] At 00:04.875, the camera cuts to a medium shot of <Subject 1> from the waist up and keeps pushing in with small amplitude at slow speed: she lets the turn run down into her body, her shoulders and then her chest and then her hips coming round after the head in one slow continuous rotation, and by the end of the shot she stands squared to the lens with both crimson eyes open on it and her expression unchanged. The same single dissolve that began in the previous shot finishes in this one: the last of the colour runs out of the sky and out of the field, and from this moment the world is flat black-red above and dead black below for the rest of the video, holding still. The camera has closed on her to the level of her eyes as the turn completes. The sound is the low rush ending into a low rumble and the dry settle of the blades. Her lips stay closed and she does not speak.
[Shot 5] At 00:07.208, the camera cuts to a medium shot of <Subject 1> from the waist up, still pushing in with small amplitude at slow speed, and she comes apart: the blade-streamers on both shoulders spread outward, the left row opening to the left and the right row to the right, each into the first full tier of its wing. More tiers unfold beyond them, tier under tier, each one longer than the last, and the two wings already run past both sides of the frame. The feathers then close over her arms first, swallowing the black gloves and the flared cuffs into the dark crimson surface, while her white-haired head and shoulders stay clear above the rising wall of feathers and her gaze stays on the lens. The world behind her is the finished dead one - flat black-red sky, black lawn, ash in the air - and it does not change in this shot. The sound is a dense low rumble swelling, a dry layered rustle at each new tier, and a chorus of low voices entering underneath. Her lips stay closed and she does not speak.
[Shot 6] At 00:09.542, the camera cuts to a low wide shot and pulls back for the only time in the video - the two wings have opened past both sides of the frame and the whole shape has to be seen - opening the frame as the last of her is taken. Her torso pulls apart and runs into the mass, and then her head is the final human part to go as the tall crown-piece tips back and the head is closed over and absorbed, the white hair drawn in last of all, with her gaze held on the lens until the surface closes over her. By the middle of the shot the pull-back has the whole of <Subject 3> standing clear in the finished dead world - flat black-red sky above, black lawn below, ash in the air, all of it holding still - and for the rest of the shot what stands there is the angel, whole and legible in silhouette: a core of folded feathers low in the middle of the frame, and out of it two colossal wings opening to the left and to the right, each built of tier after tier of feather blades sweeping outward and slightly upward with every tier longer than the one inside it, so the two wings read as two high walls of feathers standing edge to edge across the black lawn and filling the whole width of the frame, much wider than the mass is tall, with eyes opening singly all over both walls, small ones near the core and wide ones across the outer sweeps, each one its own eye with its own outline and its own iris. It is alive: the tiers of both walls open and close in slow heavy beats and the mass turns slowly on the spot. The lens is clean and straight in this shot, so the whole silhouette reads without distortion, and the separate dark-red eyes of <Subject 2> hang in the sky behind it. The sound is the rumble at its heaviest with a slow heavy beat deep in the mass, and the low voices rising. It does not speak.
[Shot 7] At 00:12.583, the camera cuts to a low close shot on part of the mass of <Subject 3> and pushes in with the smallest amplitude in the whole video, and the lens goes to a heavy wide-angle: the two walls bend outward past the left and right edges of the frame, the black lawn curves up along the bottom edge and the sky of eyes bows down over the top edge, so the mass presses out of the picture on all sides and keeps pressing to the last frame. The eyes on the mass and the separate dark-red eyes of <Subject 2> above both stay visible at the edges of the frame. The sound is the low rumble and the low voices holding one sustained note that does not resolve. Nothing speaks."""

SOUND = """overall_soundscape:
An open, airy meadow becomes a sealed, airless, low space, with one long rush through the middle of it. [Shot 1] only the soft dry hiss of wind through tall grass and one distant bird, with the air wide and open. [Shot 2] the wind thinning into a low dry rattle, a soft dry stir as her folded blades lift, and a very low far-off rumble coming up under the ground. [Shot 3] a single long low rush as the colour drains out of the world, a faint dry rustle as the blades part, and a dead airless silence underneath. [Shot 4] the same rush ending into a low rumble, under the silence, with the light rustle of the blades settling. [Shot 5] a dense low rumble swelling, a dry layered rustle at each new tier of feathers, and a chorus of low voices entering underneath. [Shot 6] the rumble at its heaviest with a slow heavy beat of the mass deep in it, the layered rustle of the feathers closing over her, and the low voices rising. [Shot 7] the rumble and the low voices holding one unbroken low tone that does not resolve, and nothing else at all."""

MUSIC = """non_diegetic_music:
One complete piece of audience-only score runs through the whole video, written as a single continuous escalation with an opening, a long build, a transformation and a held final chord, and played on a large pipe organ with its full pedal division and a low male choir over it. Its motives, its density, its pulse and its modal colour centred on E with the minor shade of G follow <Audio 1>; its instrumentation is the pipe organ with the low male choir.
- Opening ([Shot 1]): one thin high organ stop alone in the upper register, widely spaced single notes over a barely audible low pedal point, with no pulse and the dynamics at piano.
- Build ([Shot 2], [Shot 3] and [Shot 4]): the pedals enter on a slow heavy tread and the manuals add a quiet repeated figure that grows in step with the turn, staying most sparse through the glance in [Shot 2], adding one note as the blades part in [Shot 3], and taking hold as the body completes its rotation in [Shot 4], settling into a steady tread at the moment her gaze locks; the dynamics rise to mezzo-piano.
- Transformation ([Shot 5] and [Shot 6]): the manuals break into a dense continuous stream of fast repeated notes at roughly nine attacks per second with fast driving pulses near 188 beats per minute, over full pedals that roll under each new tier of feathers in step with the picture; the organ adds thick added-note clusters and the low male choir enters on one sustained note; each time a new tier of feathers opens, one more rank is drawn and the register climbs, so the organ thickens exactly as the feathers do, reaching its fullest and its highest as the whole shape of the angel is revealed in [Shot 6]; the dynamics rise through forte.
- Held ending ([Shot 7]): the fast figures stop and the organ lands on one massive low chord centred on E with the full pedal division and the choir holding it, with no return to the home cadence; this single chord is held without resolving across the final shot and decays naturally over the final two seconds of the video, ending exactly with the frame. The piece is complete in itself and is never cut off."""

content = "\n\n".join([SUBJECTS, SUMMARY, RET, DESC, SOUND, MUSIC]) + "\n"
p = os.path.join(OUT, "ronova_collapse.txt")
open(p, "w", encoding="utf-8").write(content)
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("7 镜 " + "/".join(str(x[1]) for x in SHOTS) + " = %d 帧 = %.3f s" % (sum(x[1] for x in SHOTS), sum(x[1] for x in SHOTS) / 24))

# ================= 自检：格式 + 三根脊梁 =================
txt = content
desc_block = txt.split("detailed_description:")[1].split("overall_soundscape:")[0]
shots = {}
for m in re.finditer(r'\[Shot (\d)\](.*?)(?=\[Shot \d\]|$)', desc_block, re.S):
    shots[int(m.group(1))] = m.group(2)
snd = {}
for m in re.finditer(r'\[Shot (\d)\] (.*?)(?=\[Shot \d\]|$)', SOUND.split("overall_soundscape:")[1], re.S):
    snd[int(m.group(1))] = m.group(2)

def ok(b):
    return "OK" if b else "FAIL"

print("\n=== (1) 官方格式合规 ===")
secs = re.findall(r"^(subject_definitions|summary|retention_analysis|detailed_description|overall_soundscape|non_diegetic_music):", txt, re.M)
print("  恰为官方六段: %s (%s)" % (ok(secs == ['subject_definitions','summary','retention_analysis','detailed_description','overall_soundscape','non_diegetic_music']), secs))
print("  summary 任务类型前缀: %s" % ok(txt.split('summary:')[1].strip().startswith('[reference generation + audio reference]')))
stamps = re.findall(r'At (\d\d):(\d\d)\.(\d\d\d), the camera cuts to', txt)
print("  官方时间戳 %d 处（应 6）: %s" % (len(stamps), ok(len(stamps) == 6)))
want = ["%02d:%06.3f" % (int(s // 60), s % 60) for _, _, s, _, _ in SHOTS[1:]]
got = ["%s:%s.%s" % t for t in stamps]
print("  时间戳与分镜表一致: %s  %s" % (ok(want == got), got))
print("  独立 <Picture N> 条目: %d 个（应 0）" % len(re.findall(r'^<Picture [0-9]>', txt, re.M)))
print("  镜头正文出现 <Picture N>: %s" % (re.findall(r'<Picture [0-9]>', " ".join(shots.values())) or "无 OK"))

print("\n=== (2) 脊梁1：世界只消解一次（治反复变黑）===")
CHANGE = ['darken', 'blacken', 'grow darker', 'goes grey', 'dirty grey', 'sag into', 'climb', 'sweeps over', 'first sign of the collapse']
bad = {i: [w for w in CHANGE if w in shots[i]] for i in range(5, 8)}
print("  镜5-7 不再出现任何「变暗」叙述: %s %s" % (ok(not any(bad.values())), bad if any(bad.values()) else ""))
for i in range(5, 8):
    print("    镜%d 只陈述已死世界: %s" % (i, ok(any(k in shots[i] for k in ['finished dead one', 'does not change', 'stay visible', 'finished and unchanging', 'holding still']))))
print("  消解=一个事件（continuation 措辞）: %s" % ok('The same single dissolve that began in the previous shot finishes in this one' in shots[4]))
print("  消解不搞分级阶梯（same rate / no part ahead）: %s" % ok('running out together at the same rate' in shots[3] and 'no part of the world falls ahead of any other' in txt))
print("  镜1-2 世界完好: %s" % ok(('whole' in shots[1].lower()) and not any(w in shots[1] + shots[2] for w in ['dissolve', 'ash', 'black'])))
print("  含 dissolve 的镜号: %s（应 [3,4]）" % sorted(i for i in shots if 'dissolve' in shots[i]))

print("\n=== (3) 脊梁2：镜头只有一个方向 ===")
moves = {}
for i in shots:
    m = re.search(r'(keeps pushing in|still pushing in|pushes in|pulls back)', shots[i])
    moves[i] = m.group(1) if m else "?"
ins = sorted(i for i in moves if 'push' in moves[i])
outs = sorted(i for i in moves if moves[i] == 'pulls back')
print("  推镜镜号: %s（应 [1,2,3,4,5,7]）: %s" % (ins, ok(ins == [1, 2, 3, 4, 5, 7])))
print("  后退镜号: %s（全片只 1 次，必须是镜6）: %s" % (outs, ok(outs == [6])))
print("  无死停/静止镜: %s" % ok(not re.search(r'holds still|static shot|does not move', " ".join(shots.values()))))
print("  画幅变化交给剪辑: %s" % ok(len(re.findall(r'the camera cuts to', desc_block)) == 6))
print("  镜头不绕行: %s" % ok('never travels around her' in txt and 'has stayed behind her' not in txt))

print("\n=== (4) 脊梁3：天使形状必须可读 ===")
shape = ['shaped as a great two-sided wall of feathers, much wider than it is tall',
         'two colossal wings open to the left and to the right',
         'every tier longer than the one inside it',
         'two high walls of feathers standing edge to edge across the black lawn',
         'filling the whole width of the world', 'Its middle is a slowly turning core of feathers',
         'the left wall out of the left row and the right wall out of the right row']
miss = [k for k in shape if k not in txt]
print("  <Subject 3> 剪影几何写全（7 项）: %s %s" % (ok(not miss), miss))
print("  揭示镜（镜6）零畸变: %s" % ok(
    'The lens is clean and straight in this shot, so the whole silhouette reads without distortion' in shots[6]
    and not re.search(r'wide-angle|distorted|bend outward', shots[6].replace('without distortion', ''))))
print("  畸变镜号（应只有镜7）: %s" % [i for i in shots if re.search(r'wide-angle|distorted|bows down over the top', shots[i])])
print("  揭示镜时长最长（73 帧 = 3.04s）: %s" % ok(max(x[1] for x in SHOTS) == 73 and SHOTS[5][1] == 73))
print("  镜6 全形入画: %s" % ok('pulls back for the only time' in shots[6] and 'By the middle of the shot the pull-back has the whole of <Subject 3> standing clear' in shots[6]))
print("  图3 partially_preserved + 以本文剪影为准: %s" % ok(
    'partially_preserved - the Old Testament angel form of <Picture 3>' in txt
    and 'the shape written in this prompt is the one to build' in txt))
print("  天使=羽毛+眼睛，每只眼各自独立: %s" % ok(
    'built out of layered feathers and eyes' in txt and 'its own outline and its own flat crimson iris' in txt))
bad_eye = [w for w in ['packed glowing eyes', 'eye-covered', 'compound eye', 'repeated at many sizes', 'layered wings', 'wingbeat'] if w in txt]
print("  复眼/笼统翼措辞清零: %s %s" % (ok(not bad_eye), bad_eye or ""))
print("  构成材料以 feather 表述（feather 出现 %d 次，wings 仅指左右两墙 %d 次）: %s" % (
    txt.count('feather'), len(re.findall(r'\bwings?\b', txt)), ok(txt.count('feather') >= 15)))

print("\n=== (5) 分镜表 ===")
for n, f, s, style, note in SHOTS:
    print("  镜%d  %3d 帧  %07.3f s  %-32s %s" % (n, f, s, style, note))
print("  帧数全部 17n+5: %s" % ok(all((x[1] - 5) % 17 == 0 for x in SHOTS)))

print("\n=== (6) 参考图数量与眼睛画风（用户：只留 3 张，背景眼走原神画风）===")
pics = sorted(set(re.findall(r'<Picture (\d)>', txt)))
print("  用到的参考图标签: %s（应 ['1','2','3']）: %s" % (pics, ok(pics == ['1', '2', '3'])))
print("  <Picture 4> 引用残留: %d 处: %s" % (txt.count('<Picture 4>'), ok(txt.count('<Picture 4>') == 0)))
print("  眼睛走平面赛璐珞动画风: %s" % ok('flat cel-shaded anime style' in txt and 'game illustration' in txt))
print("  无写实虹膜/渲染措辞（radiating lines / lashes / wet gloss / soft glow）: %s %s" % (
    ok(not re.search(r'radiating lines|lashes|wet gloss|soft crimson glow', txt)),
    re.findall(r'radiating lines|lashes|wet gloss|soft crimson glow', txt) or ""))
print("  天使为浅色羽毛 + 深红根部（利于在黑红天地间读出剪影）: %s" % ok(
    'white and light grey at their tips, shading to dark crimson at their roots' in txt and 'banded with crimson' in txt))

print("\n=== (7) 配乐 / 声音 ===")
print("  soundscape 覆盖 7 镜: %s" % ok(sorted(snd) == [1, 2, 3, 4, 5, 6, 7]))
ms = [("管风琴+全踏板+低男声合唱", "a large pipe organ with its full pedal division and a low male choir"),
      ("动机参照 Audio1", "follow <Audio 1>"), ("密集音流 9/s", "nine attacks per second"),
      ("急促脉动 188BPM", "188 beats per minute"), ("随羽层加厚", "thickens exactly as the feathers do"),
      ("揭示时最厚最高", "highest as the whole shape of the angel is revealed in [Shot 6]"),
      ("悬置不解决+不截断", "held without resolving")]
for nm, k in ms:
    print("    %s: %s" % (nm, ok(k in MUSIC)))
print("  抽象情绪词: %s" % (re.findall(r'warmth|melancholy|cozy|peaceful|tender|ominous|eerie', MUSIC) or "无 OK"))
print("\n  >>> 脚本只保证结构与已知回归；语义仍需人工通读。")
