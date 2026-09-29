#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《舌尖 · 红烧肉》15s 编排 · Ref2VA 六段式
风格：参照《舌尖上的中国》—— 微距浅景深、食材光影特写、蒸汽/糖色/刀光、
舒缓叙事节奏、民族管弦乐。角色（芙宁娜）在关键节点出现（看锅/尝味）。
音乐：完整五段式（引子→食材→烹饪→等待→品尝），收尾音完整衰减不截断。
总帧 362 = 5+17×21，约 15.08 秒，7 镜。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She wears a plain white apron over the tailcoat, tied at the waist. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is a small rustic home kitchen in warm evening light: a dark wooden chopping board on a worn stone counter, a piece of pork belly with clear marbled layers of fat and lean, a heavy cleaver, a clay pot on a gas stove with a low flame, a brass wok, a small bowl of rock sugar and soy sauce, wisps of steam rising, warm tungsten light from a hanging lamp, and deep warm shadow filling the rest of the room. The space around the counter is a narrow enclosed corner with no open background."""

STYLE = ("The target video is in official Genshin Impact anime style with a documentary food-film look inspired by "
         "Chinese food documentaries: cel-shaded with rich painterly colour, shallow depth of field that throws "
         "the background into soft warm bokeh, crisp macro detail on the food surfaces - the marbling of the meat, "
         "the amber gloss of the caramel, the beads of steam - and soft volumetric light. The palette is warm "
         "tungsten gold and deep amber against dark warm shadow.")

FRAMING = ("The framing across the seven shots is deliberately balanced around the food: three shots are tight "
           "macro close-ups of the ingredients and cookware with no face in frame, in which the food fills the "
           "frame and the background falls into soft bokeh; two shots are tight medium close-ups in which "
           "<Subject 1>'s head occupies roughly one third to one half of the frame height and her face is "
           "rendered in full detail, with her pale icy-blue right eye and deeper violet-blue left eye both "
           "clearly readable and her expression shown through specific physical details of brows, eyes, mouth and "
           "breathing; and two shots are full-body shots seen in profile in which she is shown complete at the "
           "counter with her face turned away from the lens and not the focus. There are no shots between these "
           "three scales, and no wide or establishing shots.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, or a wide or establishing shot.")

SHOTS = [
 # 1 选肉·刀光横移（舌尖经典：刀光+纹理）
 "A tight macro close-up on the dark wooden chopping board of <Subject 2>: a heavy cleaver presses into a piece of pork belly, the blade slicing through layers of pink lean meat and white fat, the marbling clearly visible, a thin gleam of light running along the blade edge; the background is soft warm bokeh. The camera pans slowly right along the blade with small amplitude at slow speed, following the gleam of light as it travels down the edge, then holds on the exposed grain of the cut meat. No face is in frame.",
 # 2 焯水·蒸汽升腾（舌尖经典：蒸汽光影）
 "A tight macro close-up on the clay pot of <Subject 2> on the stove: cubes of pork belly bob in gently rolling water, foam rising to the surface, thick white steam curling up and catching the warm lamplight, the water surface shimmering; the background falls into dark warm shadow. The camera pushes in extremely slowly with very small amplitude toward the rising steam, then settles back a fraction. No face is in frame.",
 # 3 炒糖色·琥珀光泽（舌尖经典：糖色光影）
 "A tight macro close-up on the brass wok of <Subject 2>: rock sugar melts and bubbles into a deep amber caramel, the surface glossy and catching the warm light, a spoon of soy sauce poured in along the wok's edge sending up a brief hiss of steam; the caramel glistens as it swirls. The camera pans slowly along the surface of the caramel with small amplitude at slow speed, following the swirl. No face is in frame.",
 # 4 下肉上色·全身侧面翻炒（角色入镜）
 "A full-body shot, seen in profile, of <Subject 1> at the stove of <Subject 2> with a wooden spatula in her WHITE-gloved right hand, turning the cubes of pork belly in the caramel in the brass wok, the meat taking on a deep amber glaze, steam rising around her: she is shown complete from the top of her hat to her boots, her face turned toward the wok and away from the lens, not the focus; the warm lamp light is on the wok and her coat. The camera trucks left with small amplitude at slow speed, keeping her and the wok inside the frame. She does not speak.",
 # 5 慢炖·看锅（角色中近景）
 "A tight medium close-up of <Subject 1> from the collarbone up at the stove, seen from her right: she lifts the lid of the clay pot with her BLACK-gloved left hand and looks down into it, a soft cloud of steam rising into her face, her head occupying about half the frame height, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable, her brows level, her lips slightly parted as she watches the meat simmer; the warm lamp light is on her face. The camera pushes in with small amplitude at slow speed toward her face. She does not speak; her lips stay slightly parted then close.",
 # 6 收汁·蒸汽引导 tilt（舌尖经典：浓稠光泽）
 "A tight macro close-up inside the clay pot of <Subject 2>: the sauce has reduced to a deep glossy glaze, large slow bubbles breaking the surface, the cubes of pork belly shiny with amber sauce, a single bubble swelling and popping, thin steam rising; the background is deep warm shadow. The camera tilts up slowly with very small amplitude, following the rising steam from the glistening meat up through the warm light, then holds. No face is in frame.",
 # 7 装盘品尝·满足（角色近景，音乐收尾，微环绕）
 "A tight medium close-up of <Subject 1> from the collarbone up at the table, seen almost straight on: she lifts a small piece of the glazed pork belly with chopsticks toward her mouth, takes it, and closes her eyes to chew slowly, her brows relaxed, the corners of her lips curving up into a satisfied smile, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable when she opens them; the plate of glossy red-brown braised pork sits in the warm light before her. The camera arcs very slowly around her with the smallest amplitude in the video, from a fraction off-center to straight on as she opens her eyes, holding on her face and the plate. She does not speak; her lips hold the smile.",
]

RET = """retention_analysis:
<Subject 1> (appears in full in [Shot 4] seen in profile; in full face in [Shot 5] and [Shot 7] as medium or close shots; and not in [Shot 1], [Shot 2], [Shot 3] and [Shot 6] where only her gloved hands or nothing of her appears): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, the dark-blue bow-topped ankle boots, and the plain white apron tied at the waist are all retained wherever she appears. She wears no headset microphone in this video.
<Subject 2> (appears in every shot): fully_preserved - the rustic home kitchen in warm evening light, the dark wooden chopping board, the piece of pork belly with clear marbled layers, the heavy cleaver, the clay pot on the stove, the brass wok, the bowl of rock sugar and soy sauce, the rising steam, and the warm hanging lamp against deep warm shadow are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous fifteen-second food-documentary style "
           "scene in the style of a Chinese food documentary, in which <Subject 1> braises a plate of red-cooked "
           "pork in seven shots with a calm, patient rhythm: a macro close-up of the cleaver slicing through the "
           "marbled pork belly, the cubes boiling in the clay pot with rising steam, the rock sugar melting into "
           "amber caramel, a full-body profile of her glazing the meat in the wok, a close-up of her lifting the "
           "lid and watching the simmer, a macro close-up of the reduced glossy sauce, and a close-up of her "
           "tasting a piece with a satisfied smile. The camera work is calm and documentary-like: slow pushes, "
           "slow pans and static holds with shallow depth of field. The whole video carries one continuous piece "
           "of music in a Chinese folk style that opens softly, builds through the cooking, and resolves "
           "completely with a final sustained note that decays fully over the last shot without being cut off. "
           "<Picture 1> supplies identity and costume only and never serves as a concrete frame anchor.""")

SOUNDSCAPE = """overall_soundscape:
A warm small kitchen room tone throughout - a low hiss of the gas flame, a faint bubbling, and a soft evening quiet. [Shot 1] the crisp rhythmic sound of the cleaver cutting through the meat and the slight thock of the blade on the board. [Shot 2] the gentle bubbling of the boiling water and the soft rise of steam. [Shot 3] the low simmer of the caramel, a soft pop of a bubble, and the hiss of the soy sauce hitting the hot wok. [Shot 4] the soft scrape of the spatula turning the meat and the rising sizzle. [Shot 5] the soft thock of the clay lid being lifted and the quiet bubbling underneath. [Shot 6] the slow wet pops of the reducing sauce and the deep simmer. [Shot 7] the small clink of the chopsticks, the soft sounds of her chewing, and one small satisfied breath."""

MUSIC = """non_diegetic_music:
One continuous piece of music runs through the entire video in five phrases, scored for a small Chinese folk ensemble - a bamboo flute (dizi), a two-stringed fiddle (erhu), a plucked zither (guzheng) and a soft drum - written only in instruments, register, tempo, texture and dynamics, with no mood words. It sits in a warm pentatonic key at a slow, unhurried tempo throughout.
- Opening phrase ([Shot 1]): a single bamboo flute note in the low register, sustained softly, joined by a single low guzheng pluck; the texture is two voices, sparse, the dynamics are piano.
- Ingredient phrase ([Shot 2] and the start of [Shot 3]): the guzheng adds a gentle plucked figure in the middle register, repeating and lightly varying, the flute weaves a slow stepwise line above it; the texture grows to three voices, still quiet.
- Cooking phrase ([Shot 3] end and [Shot 4]): the drum enters with a soft steady pulse, the erhu joins with a warm melodic line that rises in the middle register, and the ensemble swells slightly; the dynamics rise from piano to mezzo-piano, the texture is at its fullest.
- Simmer phrase ([Shot 5] and [Shot 6]): the drum and erhu soften and recede, the flute returns with a slow descending line, the guzheng plucks a sparse low accompaniment; the dynamics fall back to piano, the texture thins to three voices.
- Tasting and resolve phrase ([Shot 7]): the flute and erhu return together with the opening theme at a warm mezzo-piano, the drum gives one soft final pulse, and the piece ends with the flute holding a single long high note that decays slowly and completely over the final two seconds of the shot, the guzheng sounding one last low pluck underneath it, ending exactly with the frame and never cut off."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for i, s in enumerate(SHOTS):
    lines.append("[Shot %d] %s" % (i + 1, s))
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "braised_pork.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("7 镜 × 362 帧 = 15.08s · 舌尖风格 · 五段式完整音乐")

# 审计
import re
print("\n=== 舌尖风格元素 ===")
for k in ["macro close-up", "shallow depth of field", "warm bokeh", "steam", "caramel", "amber gloss"]:
    all_text = ' '.join(SHOTS) + STYLE
    print(f"  {k}: {'✓' if k in all_text else '✗'}")
print("\n=== 音乐完整性 ===")
for ph in ["Opening phrase", "Ingredient phrase", "Cooking phrase", "Simmer phrase", "Tasting and resolve phrase"]:
    print(f"  {ph}: {'✓' if ph in MUSIC else '✗'}")
print(f"  'never cut off': {'✓' if 'never cut off' in MUSIC else '✗'}")
print(f"  乐器齐全: {'✓' if all(x in MUSIC for x in ['flute','erhu','guzheng','drum']) else '✗'}")
print("\n=== 抽象情绪词（应为 0）===")
print("  命中:", re.findall(r"warmth|melancholy|cozy|peaceful|tender|nostalgic|sweet|delicious", MUSIC))
print(f"static 数: {len(re.findall(r'static shot', ' '.join(SHOTS)))}")
