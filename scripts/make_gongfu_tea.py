#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《深夜茶室 · 功夫茶》8 镜编排 · Ref2VA 六段式
新题材：功夫茶道。与厨房/做菜区分——仪式感、安静、动作链条清晰。
角色呈现 6/8，工序 2/8。每镜专属运镜（跟随水流/环绕茶具/极缓推）。
总帧 345 = 5+17×20，约 14.375 秒。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is a small quiet tea room at night: a low dark wooden tea table with a bamboo tea tray, a small clay teapot, a porcelain gaiwan, two narrow porcelain tasting cups, a brass kettle with a thin spout, a small bamboo tea scoop and a wooden tea caddy, a single warm paper lantern hanging low over the table, thin steam curling up from the kettle, and deep blue-black shadow filling the rest of the room. The space around the table is a narrow enclosed corner with no open background."""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light, over a palette of warm paper-lantern gold on "
         "the tea table against deep blue-black room shadow, with thin white steam catching the light.")

FRAMING = ("The framing mix across the eight shots is deliberately balanced: four shots are tight medium "
           "close-ups or close-ups in which <Subject 1>'s head occupies roughly one third to one half of the "
           "frame height and her face is rendered in full detail, with her pale icy-blue right eye and deeper "
           "violet-blue left eye both clearly readable and her expression shown through specific physical "
           "details of brows, eyes, mouth and breathing; two shots are full-body shots seen in profile or from "
           "behind in which her face is turned away from the lens and not the focus; and two shots are tight "
           "inserts of her gloved hands and the teaware with no face in frame. There are no shots between these "
           "three scales, and no wide or establishing shots.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, or a wide or establishing shot.")

SHOTS = [
 # 1 全身侧面入席
 "A full-body shot, seen in profile, of <Subject 1> stepping up to the low tea table in the tea room of <Subject 2> and kneeling onto a cushion: she is shown complete from the top of her hat to her boots as she settles, her face turned toward the table and away from the lens, so her face is not readable and not the focus; the clay teapot, the gaiwan and the brass kettle are lit ahead of her on the tray, thin steam rising. The camera starts at waist height and tilts down slowly with small amplitude as she kneels, ending level with the table. She does not speak.",
 # 2 温壶·跟随水流
 "A tight insert of <Subject 1>'s WHITE-gloved right hand lifting the brass kettle by its handle over the small clay teapot on the tray of <Subject 2>: a thin arc of hot water pours from the spout into the pot; the camera follows the water arc down with a smooth tilt, holding on the water entering the pot and the steam rising from the rim; her BLACK-gloved left hand steadies the teapot's lid. The tilt is slow and continuous, one single move. No face is in frame.",
 # 3 投茶·闻香（表情：闭眼闻）
 "A tight medium close-up of <Subject 1> from the collarbone up, seen from her right: she lifts the bamboo tea scoop with her BLACK-gloved left hand and tips dark tea leaves into the warm clay pot, then raises the empty scoop toward her nose and draws a slow breath, her eyes closing for a moment, her brows relaxed, her lips slightly parted; her head occupies about half the frame height, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable when she opens them. The camera is a static shot, holding on her face and the scoop. She does not speak; her lips stay slightly parted then close.",
 # 4 高冲·跟随水柱（无脸）
 "A tight insert of the brass kettle pouring from a height into the clay teapot on the tray of <Subject 2>: a tall thin column of hot water falls in a smooth arc, splashing gently against the inner wall of the pot, steam billowing up around the spout; the camera tilts up slowly along the water column from the pot to the spout, then back down, one continuous slow move. <Subject 1>'s WHITE-gloved right hand holds the kettle handle at the top edge of frame. No face is in frame.",
 # 5 出汤·环绕（表情：专注）
 "A medium shot of <Subject 1> from the waist up at the tea table, seen from her left: she grips the clay teapot and pours the golden tea through a small strainer into the porcelain gaiwan, the stream bright and steady; the camera arcs slowly around the table toward a more frontal angle, so the pouring tea and her focused face both pass through the frame; her head occupies about one third of the frame height, her face readable, her brows drawn slightly, her eyes following the tea stream, her lips pressed. The arc has small amplitude at slow speed. She does not speak; her lips stay pressed.",
 # 6 分茶·俯拍推近（无脸）
 "A tight insert from above of <Subject 1>'s BLACK-gloved left hand tilting the gaiwan over the two narrow porcelain tasting cups on the tray of <Subject 2>: the golden tea flows into the first cup, then the second, the camera pushing in slowly with small amplitude from the full tray down toward the two cups as the tea settles, steam rising from both. No face is in frame.",
 # 7 品茶·极缓推（表情：闭眼细品）
 "A tight medium close-up of <Subject 1> from the collarbone up at the table, seen from her right: she lifts one small porcelain cup with both gloved hands, brings it toward her lips, takes a slow sip and closes her eyes, her brows relaxed, her lips curving up into a small satisfied smile, her pale icy-blue right eye and deeper violet-blue left eye both readable when she opens them; she lowers the cup a little and gives a small nod. The camera pushes in extremely slowly with very small amplitude, from her hands to rest on her face. She does not speak; her lips hold the smile.",
 # 8 收尾·背移拉开
 "A full-body shot, seen from behind, of <Subject 1> setting the cup down on the tray and rising from the cushion in the tea room of <Subject 2>: she is shown complete from hat to boots as she stands and turns toward the dark edge of the room, her face not visible, the paper lantern and the steam from the tray behind her; the camera pulls back slowly, widening the gap, the warm lantern light and the rising steam opening up depth around her. The pull is slow and even. She does not speak.",
]

RET = """retention_analysis:
<Subject 1> (appears in full in [Shot 1] and [Shot 8] seen in profile or from behind; in full face in [Shot 3], [Shot 5] and [Shot 7] as medium or close shots; and as her gloved hands only in [Shot 2], [Shot 4] and [Shot 6] where her face is out of frame): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, and the dark-blue bow-topped ankle boots are all retained wherever she appears. She wears no headset microphone in this video.
<Subject 2> (appears in every shot): fully_preserved - the small quiet tea room at night, the low dark wooden tea table, the bamboo tea tray, the small clay teapot, the porcelain gaiwan, the two narrow porcelain tasting cups, the brass kettle with the thin spout, the bamboo tea scoop, the wooden tea caddy, the warm paper lantern, and the thin steam are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous fourteen-second scene in a small quiet "
           "tea room at night, in which <Subject 1> brews a pot of gongfu tea in eight shots, each with its own "
           "camera language bound to the action: a slow tilt down as she kneels at the table, a tilting follow of "
           "the hot water into the teapot, a still shot as she smells the dry leaves with closed eyes, a slow "
           "tilt along the tall water column as she pours from a height, an arc around the table as she pours "
           "the golden tea, a downward push-in onto the two filled cups, one very slow push from her hands to her "
           "satisfied face as she sips, and a slow pull-back as she rises and leaves. The rhythm is slow and "
           "even throughout, releasing on the final tasting shot. <Picture 1> supplies identity and costume only "
           "and never serves as a concrete frame anchor.""")

SOUNDSCAPE = """overall_soundscape:
A small quiet tea room tone with the soft hiss of the brass kettle and a faint hum of nothing else - a near silence with a low room hum. [Shot 1] the small sound of her settling onto the cushion and the rustle of her coat. [Shot 2] the soft pour of hot water and the faint clink of the spout against the pot. [Shot 3] the tiny rustle of the tea leaves from the scoop and her slow breath drawn in. [Shot 4] the higher, thinner sound of the water column falling from a height and the soft bubble of the pot. [Shot 5] the steady pour of the tea into the gaiwan and a small clink of the strainer. [Shot 6] the two short pours into the cups and the settling of the tea. [Shot 7] the small clink of the cup against the tray and her slow sip. [Shot 8] the soft sound of her rising and the rustle of her coat."""

MUSIC = """non_diegetic_music:
A very slow, spare piece for a single bamboo flute over a soft low drone, with a gentle plucked guzheng note on each pour. It enters as she kneels in [Shot 1], holds a calm level through [Shot 2] to [Shot 6] with one soft accent per pour, thins to a bare drone under her sip in [Shot 7], and ends on a single low decaying note as she rises in [Shot 8]."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for i, s in enumerate(SHOTS):
    lines.append("[Shot %d] %s" % (i + 1, s))
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "gongfu_tea.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("8 镜 × 345 帧 = 14.375s · 角色呈现 6/8 · 每镜专属运镜")

# 审计
import re
audit = {
    "1": "tilt down as she kneels", "2": "tilt follow water", "3": "static (smell)",
    "4": "tilt along water column", "5": "arc around table", "6": "downward push-in",
    "7": "very slow push", "8": "pull-back",
}
print("\n=== 运镜审计 ===")
for n, m in audit.items():
    print(f"  Shot {n}: {m}")
print(f"static 数: {len(re.findall(r'static shot', ' '.join(SHOTS)))}")
print(f"角色呈现镜: {len(re.findall(r'eyes both clearly readable', ' '.join(SHOTS)))} 脸镜 + 2 全身")
