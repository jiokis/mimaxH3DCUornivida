#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《若娜瓦 · 崩解》15s 压迫感短片 v6 · Ref2VA 官方六段式
v5 通读修订（逐句核对逻辑一致性 + 官方 ref-en.txt 规范 + 用户反馈）：
 1. 镜7 硬矛盾：删掉 "static shot" / "does not move at all"（与 "pushes in" 相反）→ 唯一一次极小幅推镜
 2. 镜5/镜6「先变暗又变暗」：天空衰减改为严格单调
    low band(镜3) → middle(镜4) → upper(镜5) → 只剩顶边一缕蓝(镜5末) → 全黑红(镜6)
 3. 镜2 声画矛盾：删掉 "grass stiffens black"（镜2 画面明写 field is still green），草变黑归镜3
 4. 镜5 画幅装不下动作：medium close-up(chest up) → medium shot(waist up)，手臂才在画面内
 5. 镜5 破句重写：wings 从她已穿的 blade-streamers 展开（变身连续性）
 6. 镜3 与镜4 前提对齐：明确「身体仍背对 + 头保持回望」，镜4 才接得上
 7. 不再把 <Picture 3> 当定格锚点：镜头正文一律引用 <Subject N>；<Picture N> 只出现在
    subject_definitions（设计出处）与 summary（引用关系），符合官方 §2.2
 8. 云的因果补链：镜3 转污灰 → 镜4 塌成暗渍 → 镜5 被黑红吞掉
 9. 复眼措辞清零：每颗瞳孔都是「独立单眼（图4 的单眼设计）」，各自轮廓/虹膜/大小
10. 元注释与否定比较清理：TIGHTENS... → 自然句；rather than → 正向陈述
11. 天使为活体：翼层持续开合呼吸，变身是「从她自己身体内部展开」
v6 目标修正（用户澄清：图3 遵循度不用太高，要的是形态 + 压迫感）：
12. <Subject 3> 保留级别 fully_preserved → partially_preserved：只沿用图3 的「旧约天使形态」，
    剪影与细节自由（retention 明写 the exact silhouette and the exact detail are free）
13. 天使形态 = 只用两种材料：层叠羽毛 + 眼睛；眼一一散落、各自独立、各自开合
    （她 blade-streamers 上那些闭着的小眼睛 = 天使眼睛的种子）
14. 新增「畸变随压力递增」镜头线索：前 4 镜干净直筒 → 镜5 起逐镜加宽，
    镜6 边缘外弓 + 地平线上翘 → 镜7 极广角畸变最大，把天使撑出画框四周
15. 全篇翼词统一为 feather / feather tier（羽 + 眼是本片的形态语言）
 总帧 358 ≈ 14.9s（7 镜：39/39/39/56/73/73/39，全部 17n+5）
"""
import os
import re

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Ronova (若娜瓦), the Ruler of Death of Teyvat and one of the Four Shades, whose exact design is shown in <Picture 1> and <Picture 2>, two views of the same character wearing the same costume. She has very long flowing white hair that falls well past her waist, and CRIMSON RED eyes; her skin is pale. She wears an ornate black-and-crimson regalia: a tall crimson crown-piece of pointed spikes and swept blades rising from her head, a fitted black high-collared bodice crossed by crimson ribbons and black straps, long black gloves reaching above her elbows, a crimson and black layered skirt with white lace panels and trailing black ribbons, and long crimson blade-streamers hanging from her shoulders that read as swept feather-blades, each carrying a row of small closed eyes along its length. She wears no headset microphone in this video. Her voice, when she speaks, is a low, level, unhurried woman's voice.
<Subject 2> is the world of this video in two opposed states. In its first state it is a vast sunlit meadow: a wide green grassland under a clear blue sky, tall grass moving in slow waves in a warm breeze, small white clouds drifting high, and soft afternoon sunlight across the field. In its second state the same world has come apart: the blue of the sky is eaten away into flat black-red, the green grass blackens and stiffens into a dead black lawn, the clouds go from white to dirty grey, then sag into flat dark stains, and are finally swallowed by the black-red. The air fills with fine drifting black ash. As the sky dies, dark-red pupils open in it and turn to look down. Each pupil is a single eye drawn to the design of the one eye shown in <Picture 4> - a deep black-red sclera, a glowing crimson iris with a thin bright rim, a narrow dark pupil, fine radiating lines around the iris and a soft crimson glow - drawn as a flat cel-shaded shape with a clean dark outline in the same hand-drawn language as her costume. The sky carries many of these pupils, and each one is its own separate eye with its own outline, its own iris and its own size, standing apart from the others in the sky.
<Subject 3> is the Old Testament angel that <Subject 1>'s own body becomes by the end of this video, built out of two things only - layered feathers and eyes - in the colossal Old Testament angel form of <Picture 3>, which is taken as the form to follow, while its exact silhouette and detail are free. The feathers rise in overlapping tiers, from small quill-blades at the core out to vast feather sweeps at the outside, and the whole mass is dark blood-crimson and wetly shining. Eyes open singly all over that mass, scattered one by one among the feathers at every scale, from small eyes the size of her own to wide ones across the outer sweeps; each eye is its own eye with its own outline and its own iris, and each one opens on its own beat. It is alive: the feather tiers keep opening and closing in slow heavy beats, the whole mass breathes and shifts and turns, the dark surface rolls as the feathers move, and eyes keep opening and closing across it. Its feathers grow out of the same crimson blade-streamers that <Subject 1> already wears, so the angel reads as her own body opened out from the inside.
<Audio 1> is the music-style and motive reference for the audience-only score of this video: a dark, heavy cue built on a slow tread under a dense stream of fast equal notes with a fast driving pulse and a modal colour centred on E with the minor shade of G. Only its motives, density, pulse and modal colour are referenced; its signal is not copied."""

SUMMARY = """summary:
[reference generation + audio reference] The target video is a single continuous fifteen-second 2D-animated scene in the official Genshin Impact style in which <Subject 1>, Ronova, stands with her back to the lens in a sunlit meadow in <Subject 2>, looks back over her shoulder at the lens, turns her whole body to face it, and then comes apart from the inside and transforms into a colossal Old Testament angel of layered feathers and eyes while <Subject 2> decays from sunlit grassland into a black lawn under a black-red sky full of separate dark-red eyes drawn to the single eye of <Picture 4>. <Subject 1>'s identity and costume come from <Picture 1> and <Picture 2>, the angel form of layered feathers and eyes follows <Picture 3>, the single-eye design of the pupils opening in the broken sky comes from <Picture 4>, and <Audio 1> supplies the motives, density, pulse and modal colour of the score."""

RET = """retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4] and [Shot 5], and up to the moment her head is absorbed in [Shot 6]): fully_preserved - Ronova's identity, her very long flowing white hair, her crimson red eyes, her pale skin, the tall crimson crown-piece of pointed spikes and swept blades, the fitted black high-collared bodice with crimson ribbons and black straps, the long black gloves above the elbow, the crimson and black layered skirt with white lace panels and trailing black ribbons, and the folded crimson blade-streamers with their rows of small eyes are retained wherever her human form appears.
<Subject 2> (appears in every shot: sunlit and whole in [Shot 1], beginning to break from [Shot 2] onward, and fully decayed in [Shot 6] and [Shot 7]): fully_preserved - the same grassland and the same sky are carried through both states; in the second state the sky carries many separate dark-red eyes drawn to the single-eye design of <Picture 4>, each one its own eye with its own outline.
<Subject 3> (appears in [Shot 6] and [Shot 7] as the final state of <Subject 1>'s own body): partially_preserved - the Old Testament angel form of <Picture 3> is carried over as a colossal mass of layered dark-crimson feathers filled with singly-set eyes, alive and moving with its feather tiers and its eyes opening and closing; the exact silhouette and the exact detail of <Picture 3> are free.
<Audio 1>: reference - its slow tread, its dense stream of fast equal notes, its fast driving pulse and its modal colour centred on E with the minor shade of G guide the score, without copying the original signal."""

DESC = """detailed_description:
The target video is 2D-animated hand-drawn cel-shaded anime in the official Genshin Impact style: bold clean dark outlines, flat vibrant colour blocking with simple two-tone cel shading, painterly highlights, crisp line art and hard dramatic light, drawn with ink lines and flat colour throughout. Every eye that opens in the sky of <Subject 2> is drawn from its single-eye design - a flat cel-shaded shape with a deep black-red sclera, a glowing crimson iris and a soft bleeding glow - and every one of them stands alone in the sky as its own eye with its own outline, its own iris and its own size. The visual arc runs from clean bright daylight in the opening shot into heavy black-red shadow with deep crushed blacks, so the image grows darker and heavier as the world comes apart. The world of <Subject 2> decays in one direction only, step by step across the seven shots, and its collapse is complete only in the sixth and seventh shots, at the same moment that her transformation completes: the darkening never retreats, and it never repeats a stage it has already passed. The camera takes its position behind her back at the start and keeps to that one side for the whole video without ever travelling around her, so her face comes into view only because she turns to face the lens. Inside that rule the camera does move - it pushes in, pulls out, tilts, pedestals and holds - and every move is slow. Lens distortion grows with the pressure: the first four shots are drawn through a clean straight lens, and from the moment the feathers unfold the lens widens step by step, so the mass bows outward past the edges of the frame, the horizon and the lawn curve up at the sides, and the last two shots are seen through a heavy wide-angle that stretches the angel past the frame on every side.
[Shot 1] An extreme wide shot of the first state of <Subject 2> frames the whole sunlit meadow from a low position, with <Subject 1> standing small at the centre of the frame with her back to the lens: her long white hair and the folded crimson blade-streamers on her back move slowly in the warm breeze, tall green grass runs away in slow silver waves toward the horizon, and small white clouds drift high in the clear blue sky. Her face is turned away from the lens. The world is still whole and bright in this shot: clear blue sky, green grass running all the way to the horizon, and clean white clouds. The camera pushes in with small amplitude at slow speed, so she grows slowly larger against the sky. The sound is only the soft dry hiss of wind through tall grass and one distant bird. She does not speak.
[Shot 2] At 00:01.625, the camera cuts to a close-up of <Subject 1> from the shoulders up, seen from just over her left shoulder and slightly below: she turns her head back over her shoulder and looks at the lens from the side, her chin held low, her gaze coming to the viewer sidelong from the corners of her crimson eyes while her shoulders and body stay exactly where they were, and her white hair slides across her shoulder as the head comes round. The first sign of the collapse appears only at the far edge of this shot: a single thin dark seam opens low on the horizon far behind her and bleeds one thread of dull dark red along it, a few grains of black ash drift across the light, and the first blades of her folded blade-streamers stir and lift slightly away from her back. The sky above her is still blue and the field around her is still green. The camera pushes in with small amplitude at slow speed, creeping closer on her face, and the glance reaches the lens because her head turns, not because the camera goes round her. The sound is the wind thinning into a low dry rattle and a very low far-off rumble under the ground. Her lips stay closed and she does not speak.
[Shot 3] At 00:03.250, the camera cuts to a full shot of <Subject 1> standing in the meadow of <Subject 2>, shown complete from the crown of her head to her feet: her body still faces away from the lens and her head stays turned back over her shoulder from the glance of the previous shot, so one crimson eye is visible in profile. Her blade-streamers are now fully lifted and parted behind her shoulders in a dark crimson fan, and the small eyes set along their edges open one by one from the tips inward. Behind her the seam on the horizon has widened into a low band of dull black-red that has just begun to climb the lower sky, the grass has started to blacken in patches immediately around her feet, and the white clouds overhead have dulled to a dirty grey. The far half of the field behind her is still green and the upper sky is still blue. The camera pulls out with small amplitude at slow speed, opening the frame to take in her whole figure and the widening band behind her. The sound is the low rumble rising, a faint dry rustle as the blades part, and a dead, airless silence underneath. Her lips stay closed and she does not speak.
[Shot 4] At 00:04.875, the camera cuts to a medium shot of <Subject 1> from the waist up, from the same low position behind her, and it holds still for the whole shot. Her head is still turned back over her shoulder from the glance of the previous shot; she now lets the turn run down into her body and rotates slowly and evenly on the spot - her shoulders, then her chest, then her hips come round after the head in one slow continuous rotation, even from start to finish - so that the audience, watching from the camera that has not moved, sees her back give way to her profile and then to her front as she comes all the way round. By the end of the shot she stands squared to the lens with both crimson eyes clearly readable and open, her brows level and her lips closed and still, and her expression has not changed at all. Behind her the collapse keeps working while she turns, and it is nowhere near finished: the band of black-red has climbed to the middle of the sky, the white clouds have sagged into flat dark stains, and the blackening has run out through the near half of the field, while the upper sky is still blue and the far field is still green. The sound is the low rumble continuing under an airless silence and the light rustle of the blades settling. Her lips stay closed and she does not speak.
[Shot 5] At 00:07.208, the camera cuts to a medium shot of <Subject 1> from the waist up, and the unfolding begins in earnest: the parted blade-streamers she already wears spread outward and upward and open into the first full tier of feathers, and more tiers unfold from behind them tier under tier, each one larger and wider than the last, so a stack of opening feather tiers rises behind and above her shoulders out of the crimson blades on her back. Her arms are then absorbed into that mass first - the crimson feathers close over them and swallow the black gloves and the flared cuffs into the dark crimson surface - while her white-haired head and shoulders stay clear above the wall of feathers and her gaze stays fixed on the lens. As the feathers unfold the collapse speeds up with them: the black-red climbs through the upper sky, the clouds are swallowed into it, the blackening runs out across almost the whole field, and fine ash thickens in the air, so that by the end of this shot only one last strip of green at the far edge of the field and one last patch of blue at the very top of the frame are left; the first dark-red pupils begin to open in the part of the sky that has already gone black-red, above and behind her, each one a separate eye drawn to the single-eye design of <Subject 2>, and they turn slowly toward the lens. The camera tilts up with small amplitude at slow speed, following the rising feathers, and the lens widens slightly so the new tiers bow outward at the top corners of the frame. The sound is a dense low rumble swelling, a dry layered rustle as each new tier of feathers unfolds, and a chorus of low voices entering underneath. Her lips stay closed and she does not speak.
[Shot 6] At 00:10.250, the camera cuts to a low wide shot looking up as the feathers now fill and overflow the frame around her: her torso is taken next - the black bodice, the crossed ribbons and the crimson skirt pull apart and run into the same dark crimson surface - so that only her white-haired head and the last of her shoulders are left above the wall of unfolding feathers, and then her head is the final human part to go as the tall crown-piece tips slowly back and the head is closed over and absorbed by the feathers from behind and above, the white hair drawn into the dark crimson surface last of all, with her gaze held on the lens until the surface closes over her. What stands there then is <Subject 3>: the blade-streamers that have been opening all along are its feathers, grown into tier after tier of a colossal feathered mass, and eyes open singly all over it, one by one, as the mass spreads outward and upward until it fills the sky. The collapse finishes in that same moment: the last patch of blue at the top of the frame is swallowed, the last strip of green at the far edge of the field blackens, the sky turns fully flat black-red, and separate dark-red pupils open across all of it, each one a single eye drawn to the design of <Subject 2>, while the meadow becomes a dead black lawn running to the black horizon. The camera pedestals up with small amplitude at slow speed, rising with the mass as it towers out of her own position and fills the frame, and the lens widens further so the mass bows outward past the edges of the frame and the black horizon curves up at both sides. The sound is the dense low rumble at its heaviest with a slow heavy beat of the mass deep in it and the low voices rising. She does not speak.
[Shot 7] At 00:13.292, the camera cuts to a low shot on part of the mass of <Subject 3> with the black-red sky behind it, and from this cut onward the camera creeps in and never stops: the nearest part of the mass fills the frame, its feather tiers still opening and closing in slow heavy beats and eyes opening and closing across them, while the dead black lawn below and the separate dark-red eyes of <Subject 2> high in the sky above both stay visible at the edges of the frame. The lens is at its widest and most distorted here, stretching the feather mass past the frame on every side so the black lawn curves up along the bottom edge and the whole sky of eyes bulges down over the top, and the camera pushes in with the smallest amplitude in the whole video, so the pressure keeps tightening all the way to the last frame. The sound is the low rumble and the low voices holding a single sustained note that does not resolve. Nothing speaks."""

SOUND = """overall_soundscape:
An open, airy meadow becomes a sealed, airless, low space. [Shot 1] only the soft dry hiss of wind through tall grass and one distant bird, with the air wide and open. [Shot 2] the wind thinning into a low dry rattle, a soft dry stir as her folded blades lift, and a very low far-off rumble coming up under the ground. [Shot 3] the rumble rising, a faint dry rustle as the blades part, a first low crackle as the near grass stiffens black, a thin dry crackle overhead as the clouds go grey, and a dead airless silence underneath. [Shot 4] the low rumble continuing under the silence and the light rustle of the blades settling, and a low soft crack overhead as the clouds sag. [Shot 5] a dense low rumble swelling, a dry layered rustle as each new tier of feathers unfolds, a wide crackle running outward through the field as it blackens, and fine ash drifting audibly past. [Shot 6] the rumble at its heaviest with a slow heavy beat of the mass deep in it, the last crackle of the field going black, and the layered rustle of the feathers closing over her. [Shot 7] the rumble and a single unbroken low tone holding without resolving, and nothing else at all."""

MUSIC = """non_diegetic_music:
One complete piece of audience-only score runs through the whole video, written as a single continuous escalation with a clear opening, a turning point, a transformation and a held final chord, and played on a large pipe organ with its full pedal division and a low male choir over it. Its motives, its density, its pulse and its modal colour centred on E with the minor shade of G follow <Audio 1>; its instrumentation is the pipe organ and the low male choir.
- Opening ([Shot 1]): one thin high organ stop alone in the upper register, widely spaced single notes over a barely audible low pedal point; there is no pulse and the dynamics are piano, so the daylight is empty and open.
- Turning point ([Shot 2], [Shot 3] and [Shot 4]): the pedals enter with a slow heavy tread and the manuals add a quiet repeated figure that grows in step with the turn: it stays most sparse through the glance in [Shot 2], adds one note as the blades part in [Shot 3], and takes hold properly as the body completes the rotation in [Shot 4], settling into a steady tread at the moment her gaze locks; the dynamics rise to mezzo-piano.
- Unfolding ([Shot 5] and [Shot 6]): the manuals break into a dense continuous stream of fast repeated notes at roughly nine attacks per second, with fast driving pulses near 188 beats per minute, over full pedals that roll under each new tier of feathers in step with the picture; the organ adds thick added-note clusters and the low male choir enters on one sustained note; each time a new tier of feathers opens, one more rank is drawn and the register climbs, so the organ thickens exactly as the feathers do; the dynamics rise through forte and the texture is at its fullest as her head is absorbed.
- Held ending ([Shot 7]): the fast figures stop and the organ lands on one massive low chord centred on E with the full pedal division and the choir holding it, with no return to the home cadence; this single chord is held without resolving across the final shot and decays naturally over the final two seconds of the video, ending exactly with the frame. The piece is complete in itself and is never cut off."""

content = "\n\n".join([SUBJECTS, SUMMARY, RET, DESC, SOUND, MUSIC]) + "\n"
p = os.path.join(OUT, "ronova_collapse.txt")
open(p, "w", encoding="utf-8").write(content)
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("7 镜 x 358 帧 ~ 14.9s | 官方六段式 | 管风琴配乐")

# ---------- 对照官方规范 + 逻辑一致性自检 ----------
txt = content
desc_block = txt.split("detailed_description:")[1].split("overall_soundscape:")[0]
print("\n=== (1) 官方格式合规（只有六段）===")
secs = re.findall(r"^(subject_definitions|summary|retention_analysis|detailed_description|overall_soundscape|non_diegetic_music):", txt, re.M)
print("  段落顺序: %s" % secs)
print("  恰为官方六段: %s" % ("OK" if secs == ['subject_definitions','summary','retention_analysis','detailed_description','overall_soundscape','non_diegetic_music'] else "FAIL"))
print("  非官方 NEG 块: %s" % ("已删除 OK" if 'Keep every frame free of' not in txt else "FAIL 仍存在"))
print("  summary 任务类型前缀: %s" % ("OK" if txt.split('summary:')[1].strip().startswith('[reference generation + audio reference]') else "FAIL"))
print("  官方时间戳格式: %d 处（应 6）" % len(re.findall(r'At 00:[0-9]{2}[.][0-9]{3}, the camera cuts to', txt)))

print("\n=== (2) 参考标签用法（官方 §2.2 不建独立 Picture 条目）===")
print("  独立 <Picture N> 条目: %d 个（应 0）" % len(re.findall(r'^<Picture [0-9]>', txt, re.M)))
shot_bodies = " ".join([b for b in re.findall(r'\[Shot \d\](.*?)(?=\[Shot \d\]|$)', desc_block, re.S)])
pic_in_shots = re.findall(r'<Picture [0-9]>', shot_bodies)
print("  镜头正文里出现 <Picture N>: %s（应为空——图不作逐镜锚点）" % (pic_in_shots or "无 OK"))
print("  <Audio 1> 定义 + retention reference: %s" % ("OK" if '<Audio 1> is the music-style' in txt and '<Audio 1>: reference' in txt else "FAIL"))

print("\n=== (3) 逻辑一致性（v5 通读修订点）===")
desc_block = txt.split("detailed_description:")[1].split("overall_soundscape:")[0]
shots = {}
for m in re.finditer(r'\[Shot (\d)\](.*?)(?=\[Shot \d\]|$)', desc_block, re.S):
    shots[int(m.group(1))] = m.group(2)
snd = {}
for m in re.finditer(r'\[Shot (\d)\] (.*?)(?=\[Shot \d\]|$)', SOUND.split("overall_soundscape:")[1], re.S):
    snd[int(m.group(1))] = m.group(2)

def ok(b):
    return "OK" if b else "FAIL"

print("  (1) 镜7 静止/推镜自相矛盾: %s" % ok(not ('static' in shots[7].lower() and 'pushes in' in shots[7])))
print("  (2) 天空单调——镜5 不得写 'the top of the sky' 被吞: %s" % ok('the top of the sky' not in shots[5]))
print("      镜5 只留顶边一缕蓝: %s | 镜6 吞掉顶边蓝: %s" % (ok('at the very top of the frame' in shots[5]), ok('last patch of blue at the top of the frame is swallowed' in shots[6])))
print("      镜3 低空带 / 镜4 天中 / 镜5 高空: %s" % ok(all(k in shots[i] for i, k in [(3,'climb the lower sky'), (4,'climbed to the middle of the sky'), (5,'climbs through the upper sky')])))
print("  (3) 镜2 声画矛盾（画面绿/声说草黑）: %s" % ok('stiffens black' not in snd[2] and 'still green' in shots[2]))
print("  (4) 镜5 画幅装得下手臂: %s" % ok('from the waist up' in shots[5] and 'absorbed' in shots[5]))
print("  (5) 镜5 破句重写: %s" % ok('so a stack of opening feather tiers rises behind and above her shoulders out of the crimson blades on her back' in shots[5]))
print("  (6) 镜3 身体背对+头保持回望（接得上镜4）: %s" % ok("her body still faces away from the lens and her head stays turned back over her shoulder" in shots[3]))
print("  (7) 镜7 不再拿图3当定格锚点: %s" % ok('built as in' not in shots[7]))
print("  (8) 云三态补链 镜3灰/镜4暗渍/镜5被吞: %s" % ok(all(k in shots[i] for i, k in [(3,'dulled to a dirty grey'), (4,'sagged into flat dark stains'), (5,'clouds are swallowed into it')])))
bad_compound = [w for w in ['packed glowing eyes', 'eye-covered', 'compound eye', 'repeated at many sizes', 'eyes covering'] if w in txt]
print("  (9) 复眼措辞清零: %s%s" % (ok(not bad_compound), "" if not bad_compound else " 残留=" + str(bad_compound)))
print("      单眼设计声明处数: %d（应 >=4）" % len(re.findall(r'single eye|single-eye', txt)))
print("  (10) 元注释/否定比较清理: %s" % ok('TIGHTENS IN STEP' not in txt and 'rather than a still image' not in txt and 'rather than an orchestra' not in txt))
print("  (11) 天使是活体（非定格）: %s" % ok('It is alive:' in txt and 'built out of two things only' in txt))
print("  (12) 相机不绕行规则自洽（不是'全程在她背后'）: %s" % ok('without ever travelling around her' in txt and 'has stayed behind her' not in txt))
print("  (13) 镜2 机位在肩后（回头斜睨物理成立）: %s" % ok('just over her left shoulder' in shots[2]))
print("  (14) 天使段无自造否定清单（no human face/head/limbs）: %s" % ok(not re.search(r'no human (face|head|limbs|silhouette)', txt)))
print("  (15) 图3 遵循度已降级为 partially_preserved: %s" % ok('partially_preserved - the Old Testament angel form of <Picture 3>' in txt))
print("      且写明只沿用形态不锁细节: %s" % ok('taken as the form to follow, while its exact silhouette and detail are free' in txt))
print("  (16) 天使 = 羽毛 + 眼睛: %s" % ok('layered feathers and eyes' in txt and 'Eyes open singly all over that mass' in txt))
print("      每只眼各自独立（非复眼整体）: %s" % ok('each eye is its own eye with its own outline and its own iris' in txt))
print("  (17) 畸变随压力递增（前4镜干净 / 后3镜加宽）: %s" % ok(
    'Lens distortion grows with the pressure' in txt
    and 'the first four shots are drawn through a clean straight lens' in txt
    and all(k in shots[i] for i, k in [(5,'the lens widens slightly'), (6,'the lens widens further'), (7,'at its widest and most distorted')])))
print("  (18) 全篇翼词已统一为 feather/feather tier: %s" % ok(not re.search(r'\bwings?\b|wingbeat', txt)))

print("\n=== (4) 运镜（按你指定；每镜一个动机明确的慢速移动）===")
moves = re.findall(r"camera (pushes in|pulls out|tilts up|pedestals up|holds still|arcs)", txt)
print("  运镜序列: %s" % moves)
plan = [("[镜1] 大远景含背影", "An extreme wide shot of the first state of <Subject 2>"),
        ("[镜2] 近景回头斜睨", "her gaze coming to the viewer sidelong"),
        ("[镜3] 全身", "a full shot of <Subject 1> standing in the meadow"),
        ("[镜4] 转身（镜头不动）", "it holds still for the whole shot"),
        ("[镜5-6] 变形（腰以上→仰拍广角）", "the unfolding begins in earnest"),
        ("[镜7] 定格压迫（极小幅推）", "the pressure keeps tightening all the way to the last frame")]
for name, key in plan:
    print("  %s: %s" % (name, ok(key in txt)))

print("\n=== (5) 管风琴配乐 ===")
org = [("管风琴+全踏板+低男声合唱", "a large pipe organ with its full pedal division and a low male choir"),
       ("动机参照 Audio1", "follow <Audio 1>"),
       ("编制为管风琴（正向）", "its instrumentation is the pipe organ and the low male choir"),
       ("密集音流 9/s", "nine attacks per second"),
       ("急促脉动 188BPM", "188 beats per minute"),
       ("随羽层加厚", "the organ thickens exactly as the feathers do"),
       ("悬置不解决+不截断", "held without resolving")]
for name, key in org:
    print("  %s: %s" % (name, ok(key in MUSIC)))
print("  抽象情绪词: %s" % (re.findall(r'warmth|melancholy|cozy|peaceful|tender|ominous|eerie', MUSIC) or "无 OK"))
print("\n  >>> 全部通过后仍需人工通读一遍再入库。" )
