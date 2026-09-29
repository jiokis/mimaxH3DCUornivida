#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《灯塔守夜》15 秒完整编排 · Ref2VA 六段式
新题材：灯塔守夜。5 镜（比之前的 3-5 镜更完整的起承转合）：
  登塔→点灯→光束扫海→风暴逼近→黎明
总帧 362 = 5+17×21，约 15.08 秒。编排核心：「光为叙事主视角」。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is the lamp room at the top of an old seaside lighthouse at night: a ring of tall glass panes looking out over the dark ocean, a great brass Fresnel lens mounted in the centre slowly rotating, a small brass lamp table with an oil lamp and a logbook, a wooden spiral stairhead behind, and a low ceiling of dark beams. Outside, the sea is black with a thin line of moonlight, and a storm front is gathering on the horizon. Inside, warm amber lamplight fills the small room and glints off the brass and glass.
"""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light, over a palette of warm amber lamplight "
         "against deep blue-black night and a thin silver of moonlight on the sea.")

FRAMING = ("The framing discipline for this video is absolute: EVERY shot is a medium shot or a close shot. "
           "There are no wide shots, no full-body shots and no long shots anywhere in this video. Whenever her "
           "face is in shot her head occupies a large part of the frame and is rendered in full detail, with her "
           "pale icy-blue right eye and her deeper violet-blue left eye both clearly readable. The camera makes "
           "exactly one slow deliberate move within each shot and then holds; there is no camera shake and no "
           "fast cutting inside a shot.")

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, or a wide or full-body shot.")

SHOTS = [
 "A medium close-up, framed from the chest up, seen from her right: <Subject 1> climbs the last steps of the wooden spiral stair and steps into the lamp room of <Subject 2>, her head and shoulders rising into the warm amber light, the great brass Fresnel lens turning slowly behind her and flashing light across the glass panes. Her pale icy-blue right eye and deeper violet-blue left eye catch the warm glow as she looks up at the lens. The camera is a static shot, holding on her face and the rotating light passing across it. She does not speak; her lips stay closed.",
 "A tight close-up on the brass lamp table, no face in frame: <Subject 1>'s WHITE-gloved right hand lifts a brass oil lamp and sets it onto the small lamp table beside the open logbook; her BLACK-gloved left hand turns a small brass wheel and the lamp flame brightens, throwing warm light across the logbook and the turning Fresnel lens behind. The camera is a static shot, holding on the hands, the lamp and the brightening flame.",
 "A medium close-up, framed from the collarbone up, seen almost straight on: <Subject 1> stands before the great glass panes of <Subject 2>, the rotating beam sweeping past her face in regular flashes; the black sea and the thin moonlight line are visible through the glass beyond her shoulder. Her pale icy-blue right eye and deeper violet-blue left eye are both readable as each beam passes. She lifts her head and watches the beam sweep out over the sea. The camera pushes in with small amplitude at slow speed. She does not speak; her lips are slightly parted.",
 "A tight close-up on her face seen through the glass, the storm behind her: <Subject 1> stands at the pane as the storm front darkens the horizon, a first flicker of distant lightning washing grey over the sea; her pale icy-blue right eye and deeper violet-blue left eye are both readable in the lamplight against the dark. She does not flinch; her expression is steady and watchful. The camera is a static shot, holding on her face with the storm light flickering behind her. She does not speak.",
 "A medium close-up, framed from the chest up, seen from her left: <Subject 1> turns from the window as the first grey dawn light begins to show on the horizon, the Fresnel lens slowing to a stop; she rests her WHITE-gloved hand on the brass rail and lets out a slow breath, the lamplight paling against the new daylight. Her pale icy-blue right eye and deeper violet-blue left eye are both readable in the mixed amber-and-grey light, a small tired smile at the corner of her lips. The camera holds. She does not speak; her lips close on the smile.",
]

RET = """retention_analysis:
<Subject 1> (appears in full - head, body and face - in [Shot 1], [Shot 3], [Shot 4] and [Shot 5], and as her gloved hands only in [Shot 2]): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, and the dark-blue bow-topped ankle boots are all retained wherever she appears. She wears no headset microphone in this video.
<Subject 2> (appears in every shot): fully_preserved - the lamp room, the rotating brass Fresnel lens, the brass lamp table with the oil lamp and logbook, the glass panes, the black sea with the thin moonlight line, and the gathering storm are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous fifteen-second scene in the lamp room "
           "of an old seaside lighthouse at night, in which <Subject 1> arrives at the top of the stairs, lights "
           "the oil lamp, watches the rotating beam sweep out over the dark sea, faces the gathering storm without "
           "flinching, and meets the first grey dawn light with a tired smile. Five hard-cut shots of unequal "
           "length, ordered as one night of watch duty. <Picture 1> supplies identity and costume only.")

SOUNDSCAPE = """overall_soundscape:
The whole video sits inside a small lamp-room room tone - a low mechanical hum of the rotating Fresnel lens, the soft creak of the wooden stair and beams, and a distant, constant low roar of the sea. [Shot 1] her boots on the wooden steps and the creak of the stairhead. [Shot 2] the small brass click of the lamp being set down, the tick of the brass wheel and a soft whoosh as the flame brightens. [Shot 3] the steady mechanical hum of the lens and the sea below. [Shot 4] a first low rumble of distant thunder and the rain beginning to tap the glass panes. [Shot 5] the hum winding down as the lens slows, a long slow breath, and the rain easing into the grey dawn."""

MUSIC = """non_diegetic_music:
A slow, spare score of a single cello line over a soft low drone, with a gentle woodwind phrase that enters as the lamp is lit and returns as the dawn light arrives. The music holds level and patient through the storm shot, then resolves softly downward as she smiles at dawn."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for i, s in enumerate(SHOTS):
    lines.append("[Shot %d] %s" % (i + 1, s))
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "lighthouse.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("5 镜 × 362 帧 = 15.08s")
