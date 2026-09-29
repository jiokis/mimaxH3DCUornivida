#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《片场总控》20 秒导演题材 · 10 镜多线程编排 · Ref2VA 六段式
比 director_v2 更复杂：多部门调度 + 群演 + 轨道摄影 + 对讲系统。
编排核心「指挥涟漪」：她一次指令，灯光/摄影/群演/场记依次响应。
总帧 500 = 5+17×29，约 20.83 秒。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She wears a small black headset microphone hooked over one ear and speaks into it. Her voice is a clear, bright, theatrically commanding young woman's voice.
<Subject 2> is a busy film soundstage at night: a raised wooden platform with a painted backdrop of a moonlit courtyard, three softbox lamps on C-stands around it, a matte-black field monitor on a trolley, a dolly track laid across the concrete floor with a camera on a wheeled dolly, a folding wooden clapperboard in a stand, a grey folding director's chair, coiled cables and sandbags, a small PA speaker on a stand, and a row of indistinct crew figures in dark coats standing at the edges. Warm tungsten light from the left, a cool blue fill from the right, and a hard rim light from behind."""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light, over a soundstage palette of deep blue-grey "
         "shadow cut by warm tungsten gold from the left, a cool blue fill from the right, and a hard white rim "
         "light from behind, with bright aqua accents in her hair.")

FRAMING = ("The framing discipline for this video is a deliberate mix, exactly as follows: four shots are wide "
           "full-body shots in which <Subject 1> is shown complete from the top of her hat to her boots with "
           "clear space above her head and the set around her, and in these wide shots she is turned or looking "
           "down or away from the lens so her face is not the focus; the other six shots are tight medium "
           "close-ups or tight inserts in which her head or her gloved hands fill a large part of the frame and "
           "her face, when shown, is rendered in full detail with her pale icy-blue right eye and deeper "
           "violet-blue left eye both clearly readable. There are no shots between these two scales.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces. The indistinct crew figures must remain indistinct and in the "
       "background, never entering the foreground.")

SHOTS = [
 # —— 开场：全景，进入片场 ——
 "A wide full-body shot: <Subject 1> is shown complete from the top of her hat to her boots, seen from the side, walking four paces across the dark soundstage of <Subject 2> toward the dolly track, her coat and long filigreed back panel swinging, her boots crossing the concrete between sandbags and cables. The three softbox lamps and the moonlit backdrop stand behind her. She is in profile, looking ahead, not at the lens. The camera trucks right with small amplitude at slow speed. She does not speak; her lips are closed.",
 # —— 插镜：场记板 ——
 "A tight insert, seen from the side, of the folding wooden clapperboard in its stand on the soundstage of <Subject 2>: a hand in a white glove lifts the slate and snaps it shut with a hard click, the striped bars flashing. The camera is a static shot. No face is in frame.",
 # —— 全景：站定指挥灯光组 ——
 "A wide full-body shot: <Subject 1> is planted behind the dolly, shown complete from hat to boots, her white-gloved right arm raised pointing at the softbox lamps while her black-gloved left hand rests on the monitor trolley. She leans forward, chin down, face angled away from the lens. The camera holds her whole figure with the lamps, the backdrop and the crew silhouettes around her. Her mouth opens and she calls into the headset, <d>[Chinese] 灯光组，第三号灯全开！</d> the words short and hard.",
 # —— 近景：监视器 ——
 "A tight medium close-up of <Subject 1> from the collarbone up: she stands at the matte-black monitor, its cool glow on her face, her headset mic arcing across her cheek, her pale icy-blue right eye and deeper violet-blue left eye both readable. She flicks her gaze from the monitor up toward the lamps. The camera pushes in with small amplitude at slow speed. Her mouth opens and she calls, <d>[Chinese] 摄影组，轨道推起来！</d> the words clipped and level.",
 # —— 插镜：轨道与摄影机 ——
 "A tight insert on the dolly track and the camera: the wheeled dolly begins to glide smoothly along the track across the soundstage floor of <Subject 2>, the camera body glinting in the tungsten light, a gloved hand steadying the rig. The camera is a static shot. No face is in frame.",
 # —— 全景：指挥群演 ——
 "A wide full-body shot: <Subject 1> stands at the edge of the platform, both arms swept up and out, ushering the indistinct dark-coated crew figures into the lamplight, her boots planted wide, her coat flaring. She is turned three-quarters away from the lens. The camera trucks left with small amplitude at slow speed, keeping her whole figure and the lit platform inside the frame. Her mouth opens and she calls, <d>[Chinese] 群演，进画面！</d> the words crisp.",
 # —— 近景：检查监视器 ——
 "A tight medium close-up of <Subject 1> from the chest up: she leans toward the matte-black monitor, one hand on its edge, the cool screen light washing up her face, her pale icy-blue right eye and deeper violet-blue left eye both clearly readable. She studies the frame, brow drawn, then gives a small nod. The camera is a static shot. She does not speak; her lips are pressed.",
 # —— 插镜：追光与喇叭 ——
 "A tight insert on the PA speaker and a moving spotlight: the small PA speaker hums, and a bright spotlight swings across the platform, catching the painted moonlit backdrop. The camera tilts up with small amplitude at slow speed. No person is in frame.",
 # —— 近景：最后指令 ——
 "A tight medium close-up of <Subject 1> from the collarbone up: she raises her black-gloved left hand to shoulder height with fingers open, the soundstage dark behind her, her headset mic at her cheek, her pale icy-blue right eye and deeper violet-blue left eye both sharp. The camera pushes in with small amplitude at slow speed. Her mouth opens and she calls, <d>[Chinese] 各部门就位！</d> the words level and held.",
 # —— 高潮：拍板 ——
 "A tight close-up of <Subject 1>'s face filling most of the frame, the soundstage black behind her, her pale icy-blue right eye and deeper violet-blue left eye both sharp. Her raised hand snaps down out of frame, her chin comes down, her eyes lock down the lens, and she barks ONE SHORT HARD CLIPPED WORD - a single sharp commanding burst, punched and cut off, NOT drawn out, with no trailing vowel: <d>[Chinese] Action！</d> Her jaw snaps shut and she holds the wide-eyed commanding expression, lips pressed, for the rest of the shot. The camera is a static shot.",
]

RET = """retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 3], [Shot 4], [Shot 6], [Shot 7], [Shot 9] and [Shot 10] in full or as a close-up, and as her gloved hands only in [Shot 2], [Shot 5] and [Shot 8]): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, the dark-blue bow-topped ankle boots, and the small black headset microphone over her ear are all retained wherever she appears.
<Subject 2> (appears in every shot): fully_preserved - the soundstage, the raised platform with the moonlit backdrop, the three softbox lamps on C-stands, the matte-black monitor on its trolley, the dolly track with the camera rig, the clapperboard in its stand, the grey director's chair, the coiled cables and sandbags, the PA speaker, and the indistinct dark-coated crew figures at the edges are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous twenty-one-second scene on a busy film "
           "soundstage, in which <Subject 1>, Furina, directs the final setup before a take with a widening ripple "
           "of commands: she walks onto the set, the clapperboard is struck, she orders the lighting crew to open "
           "the lamps, orders the camera crew to push the dolly, ushers the crew into frame, checks the monitor, "
           "calls all departments to readiness, and finally drops her hand and barks the word that starts the "
           "take. Ten hard-cut shots alternating deliberately between four wide full-body shots and six close or "
           "insert shots. <Picture 1> supplies identity and costume only and never serves as a concrete frame "
           "anchor.""")

SOUNDSCAPE = """overall_soundscape:
A dry, busy soundstage room tone with a low hum from the lamp ballasts, the faint ring of the wooden platform, and distant indistinct chatter. [Shot 1] her boots and the trailing hem of her coat crossing the concrete. [Shot 2] the hard click of the clapperboard snapping shut. [Shot 3] the light scuff of her boots as she plants herself, and the soft electrical pop of the lamps brightening. [Shot 4] the small tick of the monitor and the rustle of her collar. [Shot 5] the smooth glide of the dolly wheels on the track and a low squeak of the rig. [Shot 6] several sets of footsteps arriving into the light. [Shot 7] the low hum of the monitor and her small breath. [Shot 8] the warm hum of the PA speaker and the clunk of the spotlight. [Shot 9] the slow audible intake of her breath. [Shot 10] the hard slap of her glove and then a short, dry, dead silence after the bark."""

MUSIC = """non_diegetic_music:
A tight percussive score of muted pizzicato strings and a single low taiko pulse at a fast tempo. It enters with her footsteps in [Shot 1], locks to the hard cuts with one accent per cut through [Shot 2] to [Shot 9], thins to a bare ticking pulse under her breath in [Shot 9], and then cuts out dead on the bark in [Shot 10], leaving only a single sustained low string note that decays as the frame holds."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for i, s in enumerate(SHOTS):
    lines.append("[Shot %d] %s" % (i + 1, s))
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "set_control.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("10 镜 × 500 帧 = 20.83s · 4全景 + 6近景/插镜")
