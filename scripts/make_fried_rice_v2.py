#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《深夜厨房 · 蛋炒饭 v2》9 镜快切 · 运镜生动版 · Ref2VA 六段式
相对 v1 的核心改进：每镜运镜专属且与动作/情绪绑定（不再 static 偷懒）。
运镜动机：跟随动作轨迹 / 情绪推近 / 蒸汽与光作为运镜参照物。
总帧 345 = 5+17×20，约 14.375 秒。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She wears a plain white apron over the tailcoat, tied at the waist. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is a small home kitchen at night: a dark wooden counter with a steel wok on a gas stove, a blue flame, a white porcelain bowl of beaten eggs, a rice bowl, a small dish of chopped spring onions, a wooden spatula, warm tungsten light from a hanging lamp over the counter, and deep blue shadow filling the rest of the room. The space around the counter is a narrow, enclosed kitchen corner with no open background."""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light, over a palette of warm tungsten gold on the "
         "counter against deep blue-black kitchen shadow.")

FRAMING = ("The framing mix across the nine shots is deliberately balanced: four shots are tight medium "
           "close-ups or close-ups in which <Subject 1>'s head occupies roughly one third to one half of the "
           "frame height and her face is rendered in full detail, with her pale icy-blue right eye and deeper "
           "violet-blue left eye both clearly readable and her expression shown through specific physical "
           "details of brows, eyes, mouth and breathing; two shots are full-body shots seen in profile or from "
           "behind in which her face is turned away from the lens and not the focus; and three shots are tight "
           "inserts of her gloved hands and the cookware with no face in frame. There are no shots between these "
           "three scales, and no wide or establishing shots.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, or a wide or establishing shot.")

SHOTS = [
 # 1 低机位跟随入场
 "A full-body shot, seen in profile, of <Subject 1> walking into the narrow kitchen of <Subject 2> with a white porcelain bowl of eggs in her hands: she is shown complete from the top of her hat to her boots, stepping past the counter, her face turned away from the lens toward the stove, so her face is not readable and not the focus; the blue flame and the steel wok are lit ahead of her. The camera starts low near the counter edge, tracking left beside her legs, then rises smoothly as she stops, ending at chest height, the whole move slow and gliding with small amplitude. She does not speak.",
 # 2 下摇跟随蛋液弧线
 "A tight insert, seen from the side, of <Subject 1>'s WHITE-gloved right hand cracking a pale egg against the rim of the white porcelain bowl on the counter of <Subject 2>: the shell splits and the yolk drops; the camera tilts down in a smooth arc following the falling yolk through the air into the bowl, where it lands with a small splash, then holds on the yolk settling in the bowl; her BLACK-gloved left hand holds the shell halves over the bowl. The tilt is slow and continuous, one single move. No face is in frame.",
 # 3 微距环绕碗
 "A tight medium close-up of <Subject 1> from the collarbone up, seen from her left, as she stirs the eggs: the camera arcs slowly around the bowl, moving from her left side around to a more frontal angle, so the swirling egg liquid and her focused face both pass through the frame during the arc; her head occupies about half the frame height at the arc's end, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable, her brows drawn slightly down, her eyes fixed on the bowl, her lips pressed together. The arc is smooth with small amplitude at slow speed. She does not speak; her lips stay pressed.",
 # 4 俯冲推近油花
 "A tight insert on the steel wok on the stove of <Subject 2>: a blue gas flame licks the wok's side and a shallow pool of oil shimmers; as the first wisp of smoke rises and a small drop of egg mixture falls in and sizzles, the camera pushes in sharply with small amplitude toward the shimmering oil surface, the flame and the sizzle filling more of the frame, then holds. The push is a single quick deliberate move that lands as the sizzle peaks. No person is in frame.",
 # 5 颠勺同步起伏（arc shot）
 "A medium shot of <Subject 1> from the waist up at the stove, seen from her right: she holds the wok handle with her BLACK-gloved left hand and tosses the rice and egg with the spatula in her WHITE-gloved right hand, steam and wok hei rising around her; the camera performs a gentle arc shot, dipping slightly as she lifts the wok and rising as she settles it, so the vertical rhythm of the toss is echoed by the camera; her head occupies about one third of the frame height, her face readable, the corners of her lips curved up slightly, her eyes following the food in the wok. The arc has small amplitude at medium speed, matched to her tosses. She does not speak; her lips stay closed.",
 # 6 侧移穿越蒸汽
 "A tight insert of <Subject 1>'s BLACK-gloved left hand scattering chopped spring onions from a small dish into the wok on the counter of <Subject 2>: the green pieces fall into the steam; the camera tracks laterally right across the front of the wok, passing through the rising steam so the frame is briefly veiled and then clears as the steam drifts, the spatula in her WHITE-gloved right hand folding the onions into the rice. The lateral move is slow and continuous. No face is in frame.",
 # 7 环绕半圈看表情
 "A tight medium close-up of <Subject 1> from the collarbone up, seen at first from her left: she lifts her head from the wok and draws a slow breath through her nose, her eyes closing for a moment; the camera arcs around her, ending almost straight on as she opens her eyes and looks toward the lens, the corners of her lips curving up into a small open smile, her cheeks lifting, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable in the warm light, steam rising from the wok below frame. The arc is smooth with small amplitude at slow speed, the smile arriving as the camera reaches the front. She does not speak; her lips hold the smile.",
 # 8 背移拉开纵深
 "A full-body shot, seen from behind, of <Subject 1> carrying the plate of fried rice across the small kitchen of <Subject 2> toward a dark table just inside the frame edge: she is shown complete from hat to boots, walking away from the lens, her face not visible, the steam rising from the plate, her back panel and apron swaying with her steps. The camera pulls back slowly, widening the gap between her and the lens, so the warm lamplight and the plate's steam open up depth behind her. The pull is slow and even. She does not speak.",
 # 9 极缓推焦点变化
 "A tight medium close-up of <Subject 1> from the collarbone up at the table, seen from her right: she lifts a small spoonful of fried rice toward her mouth with her WHITE-gloved right hand; the camera pushes in extremely slowly, starting on the spoon and the rising steam, then as she takes the bite and closes her eyes to chew, the push carries up past the spoon to rest on her face, her brows relaxed, her lips curving up into a satisfied smile around the spoon, her pale icy-blue right eye and deeper violet-blue left eye both readable when she opens them; she gives a small nod. The push is the slowest move in the whole video, with very small amplitude. She does not speak.",
]

RET = """retention_analysis:
<Subject 1> (appears in full in [Shot 1] and [Shot 8] seen in profile or from behind; in full face in [Shot 3], [Shot 5], [Shot 7] and [Shot 9] as medium or close shots; and as her gloved hands only in [Shot 2] and [Shot 6]): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, the dark-blue bow-topped ankle boots, and the plain white apron tied at the waist are all retained wherever she appears. She wears no headset microphone in this video.
<Subject 2> (appears in every shot): fully_preserved - the narrow home kitchen at night, the dark wooden counter, the steel wok on the gas stove with the blue flame, the white porcelain bowl, the rice bowl, the dish of chopped spring onions, the wooden spatula, and the warm hanging lamp against deep blue shadow are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous fourteen-second scene in a small home "
           "kitchen at night, in which <Subject 1> cooks a plate of egg fried rice in nine quick-cut shots, each "
           "with its own camera language bound to the action: a low tracking rise as she enters, a tilting "
           "follow of the falling yolk, a slow arc around the mixing bowl, a sharp push toward the sizzling oil, "
           "an arc shot that dips and rises with her tosses, a lateral glide through the steam, a half-circle arc "
           "onto her smiling face, a slow pull-back as she carries the plate away, and one very slow push from the "
           "spoon to her satisfied eyes. The rhythm accelerates through the middle shots and releases on the "
           "final tasting shot. <Picture 1> supplies identity and costume only and never serves as a concrete "
           "frame anchor.""")

SOUNDSCAPE = """overall_soundscape:
A small kitchen room tone with the low hiss of the gas stove and a faint hum of the hanging lamp. [Shot 1] her boots on the tiled floor and the soft rustle of the apron. [Shot 2] the sharp crack of the eggshell and the small splash of the yolk into the bowl. [Shot 3] the light scrape of the spatula against the porcelain bowl. [Shot 4] the soft whoosh of the flame and the first sharp sizzle of the oil. [Shot 5] the rhythmic scrape and toss of the rice in the wok and the rising sizzle of the steam. [Shot 6] the tiny rustle of the spring onions falling and the continuing wok sizzle. [Shot 7] her slow audible breath drawn in through her nose. [Shot 8] her footsteps on the tiled floor crossing the kitchen. [Shot 9] the small clink of the spoon, the soft sounds of her chewing, and one small breath."""

MUSIC = """non_diegetic_music:
A light, fast pizzicato string line with a soft brushed drum at a brisk tempo. It enters with her first step in [Shot 1], quickens its pace across [Shot 2] to [Shot 6] with one crisp accent on each cut, thins to a single ticking pulse under her breath in [Shot 7], holds quiet under her footsteps in [Shot 8], and ends on a single soft plucked note as she nods in [Shot 9]."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for i, s in enumerate(SHOTS):
    lines.append("[Shot %d] %s" % (i + 1, s))
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "fried_rice_v2.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("9 镜 × 345 帧 = 14.375s · 每镜专属运镜")

# 运镜审计
import re
moves = {
    "1": "track+rise", "2": "tilt-down follow", "3": "arc around bowl",
    "4": "sharp push-in", "5": "arc shot w/ toss rhythm", "6": "lateral glide",
    "7": "half-circle arc", "8": "pull-back", "9": "very slow push",
}
print("\n=== 运镜生动化审计 ===")
for n, m in moves.items():
    print(f"  Shot {n}: {m}")
print(f"static 数: {len(re.findall(r'static shot', ' '.join(SHOTS)))} (应为 0)")
