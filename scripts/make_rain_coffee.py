#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《雨中咖啡馆》15 秒完整编排 · Ref2VA 六段式
核心要求（用户指定）：
1. 一段完整的音乐 —— non_diegetic_music 写成四段式完整结构（引入→发展→高点→收束），
   情绪递进自然，全用音乐语言（乐器/音区/速度/织体/力度），零抽象情绪词。
2. 运镜平静生动 —— 每镜专属运镜，平静（慢速小幅度）但生动（有动机：跟随目光/雨滴/蒸汽/光）。
3. 角色呈现为主，表情物理描述。
总帧 362 = 5+17×21，约 15.08 秒，5 镜（起承转合完整弧线）。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is a small warm cafe in steady rain at dusk: a dark wooden table by a wide window pane with rain streaming down the glass, amber street lights blurred into soft blobs beyond, a porcelain cup of coffee with a curl of steam, a small cream pitcher, a folded newspaper, and warm golden pendant lamps hanging low over the table. The rain outside is steady at the start and eases toward the end of the video. Warm amber light fills the room and reflects off the wet window."""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light, over a palette of warm amber lamplight "
         "against the deep blue-grey dusk and the rain-streaked window.")

FRAMING = ("The framing across the five shots is deliberately balanced: three shots are tight medium close-ups "
           "or close-ups in which <Subject 1>'s head occupies roughly one third to one half of the frame height "
           "and her face is rendered in full detail, with her pale icy-blue right eye and deeper violet-blue left "
           "eye both clearly readable and her expression shown through specific physical details of brows, eyes, "
           "mouth and breathing; one shot is a full-body shot seen in profile in which her face is turned away "
           "from the lens and not the focus; and one shot is a tight insert of her gloved hands and the cup with "
           "no face in frame. There are no shots between these three scales, and no wide or establishing shots.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, or a wide or establishing shot.")

SHOTS = [
 # 1 全身侧面入场，目光落点窗边（音乐：低音区单音引入）
 "A full-body shot, seen in profile, of <Subject 1> stepping into the warm cafe of <Subject 2> and walking toward the table by the rain-streaked window: she is shown complete from the top of her hat to her boots, moving past the hanging lamps, her face turned toward the window and away from the lens, so her face is not readable and not the focus; the rain streams down the glass and the amber lights blur beyond. The camera starts low near the door and rises slowly as she walks, tracking her with small amplitude at slow speed, ending level with the table as she stops. She does not speak.",
 # 2 坐下，目光跟随雨滴（音乐：引入第二声部）
 "A tight medium close-up of <Subject 1> from the collarbone up, seen from her left, as she sits at the table by the window: her head occupies about half the frame height, her face turned three-quarters toward the glass, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable, her brows level, her lips pressed; her gaze follows a single raindrop sliding down the pane, and the camera pans slowly right with the direction of her gaze, holding the rain-streaked glass in frame for a moment before settling back on her face. The pan is slow, smooth and small in amplitude. She does not speak; her lips stay pressed.",
 # 3 捧杯暖手，蒸汽为运镜参照（音乐：旋律上行发展）
 "A tight insert of <Subject 1>'s WHITE-gloved right hand wrapping around the warm porcelain cup on the table of <Subject 2>, with her chin just out of frame at the top edge: a curl of steam rises from the coffee and drifts across the amber lamplight; the camera pushes in extremely slowly with very small amplitude toward the cup and the steam, the wet window and the blurring lights behind going gently out of focus. Her BLACK-gloved left hand rests beside the cup on the folded newspaper. No face is in frame.",
 # 4 雨渐小，光变暖（音乐：高点，琶音上行+弦乐进入）
 "A medium shot of <Subject 1> from the waist up at the window table, seen from her right: outside the glass the rain visibly eases, the streaks thinning and the amber street lights becoming clearer and warmer; she lifts her head from the cup and looks out at the easing rain, her head occupying about one third of the frame height, her face readable, her brows relaxing, the corners of her lips curving up slightly, her pale icy-blue right eye and deeper violet-blue left eye both catching the warmer light. The camera tilts up slowly with small amplitude from the cup to her face, following her lifted gaze. She does not speak; her lips stay closed.",
 # 5 轻啜，闭眼（音乐：收束，音符拉长渐弱）
 "A tight medium close-up of <Subject 1> from the collarbone up at the table, seen almost straight on: she lifts the porcelain cup with both gloved hands, takes a slow sip, and closes her eyes for a moment, her brows relaxed, her lips curving up into a small satisfied smile around the cup's rim, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable when she opens them and looks down at the cup; the rain outside has nearly stopped, leaving only a thin trickle on the glass. The camera pushes in with very small amplitude at the slowest speed in the video, ending on her face. She does not speak; her lips hold the smile.",
]

RET = """retention_analysis:
<Subject 1> (appears in full in [Shot 1] seen in profile; in full face in [Shot 2], [Shot 4] and [Shot 5] as medium or close shots; and as her gloved hands only in [Shot 3] where her face is out of frame): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, and the dark-blue bow-topped ankle boots are all retained wherever she appears. She wears no headset microphone in this video.
<Subject 2> (appears in every shot): fully_preserved - the small warm cafe at dusk, the dark wooden table by the rain-streaked window, the amber street lights blurred beyond the glass, the porcelain cup with the curl of steam, the small cream pitcher, the folded newspaper, the warm golden pendant lamps, and the rain that is steady at the start and eases toward the end are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous fifteen-second scene in a small warm "
           "cafe during steady rain at dusk, in which <Subject 1> arrives, sits by the window, wraps her hands "
           "around a cup of coffee as steam rises, watches the rain ease outside, and takes a slow sip with a "
           "small satisfied smile. Five shots form one full arc, each with its own calm but vivid camera move: a "
           "slow tracking rise as she enters, a slow pan following her gaze along a raindrop, one very slow push "
           "onto the cup and steam, a slow tilt up from the cup to her face as the rain eases and the light "
           "warms, and the slowest push of the video onto her face as she sips. The whole video carries one "
           "continuous piece of music that builds from a low single-note opening through a rising melody to a "
           "warm peak and resolves to a long quiet note. <Picture 1> supplies identity and costume only and "
           "never serves as a concrete frame anchor.""")

SOUNDSCAPE = """overall_soundscape:
A small warm cafe room tone throughout - a soft steady patter of rain against the window that slowly eases, the low hiss of the espresso machine somewhere behind, and a faint murmur of the room. [Shot 1] her boots on the wooden floor and the soft creak of a floorboard. [Shot 2] the rain against the glass and a small ceramic ring as the cup is set down. [Shot 3] the very quiet hiss of the steam and the rustle of the newspaper under her hand. [Shot 4] the rain audibly thinning outside and the small sound of her breath drawn in. [Shot 5] the small clink of the cup against the saucer, a slow sip, and the rain nearly gone to a thin trickle."""

MUSIC = """non_diegetic_music:
One continuous piece of music runs through the entire video in four phrases, using only instruments, register, tempo, texture and dynamics - no mood words. It is scored for a solo piano with a single cello line and a soft string pad, at a slow tempo throughout, in a warm major key.
- Opening phrase ([Shot 1] and the first half of [Shot 2]): a single low piano note, C3, struck twice softly in a sparse rhythm, with a low sustained cello drone under it at very low volume; the texture is one voice, the dynamics are piano.
- Development phrase (second half of [Shot 2] and [Shot 3]): the piano adds a rising two-note figure in the middle register, A3 then B3, repeated and gently varied, the cello joins with a slow melodic line moving by steps, and the string pad enters at very low volume underneath; the texture grows to two voices over the pad, still quiet.
- Peak phrase ([Shot 4]): the piano plays a soft rising arpeggio from D4 up to A4, the cello line rises to its highest note and holds, the string pad swells slightly, and the tempo holds but the dynamic rises from piano to mezzo-forte; the texture is at its fullest, three voices together.
- Resolution phrase ([Shot 5]): the piano returns to the low register with a single note, G2, struck once and allowed to ring, the cello descends by steps to its opening drone, and the string pad fades to near silence over the final held note; the dynamics fall back to piano and the final piano note decays over the last two seconds of the video, ending exactly with the frame."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for i, s in enumerate(SHOTS):
    lines.append("[Shot %d] %s" % (i + 1, s))
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "rain_coffee.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("5 镜 × 362 帧 = 15.08s · 完整四段式音乐")

# 审计
print("\n=== 音乐结构审计 ===")
import re
for ph in ["Opening phrase", "Development phrase", "Peak phrase", "Resolution phrase"]:
    print(f"  {ph}: {'✓' if ph in MUSIC else '✗'}")
print(f"  乐器: 钢琴/大提琴/弦乐垫 全部出现: {'✓' if all(x in MUSIC for x in ['piano','cello','string pad']) else '✗'}")
print(f"  动态标记: {'✓' if all(x in MUSIC for x in ['piano','mezzo-forte']) else '✗'}")
print(f"  音区变化: {'✓' if all(x in MUSIC for x in ['low register','middle register','rising arpeggio']) else '✗'}")
print("\n=== 抽象情绪词（应为 0）===")
print("  命中:", re.findall(r"warmth|melancholy|cozy|peaceful|calm|tender|nostalgic|sweet", MUSIC))
print("\n=== 运镜审计 ===")
moves = ["tracking rise", "pan slowly", "push in extremely slowly", "tilts up slowly", "pushes in with very small amplitude"]
for m in moves:
    print(f"  {m}: {'✓' if m in ' '.join(SHOTS) else '✗'}")
print(f"  static 数: {len(re.findall(r'static shot', ' '.join(SHOTS)))}")
