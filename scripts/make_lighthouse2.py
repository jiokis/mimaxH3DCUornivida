#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《灯塔守夜 v2》—— 意象物理化改写
v1 问题：抽象情绪词（释怀/宁静/私密微笑）模型渲染不了 → 意象模糊、结尾突兀。
v2 原则：每镜 = 一个明确物理动作 + 道具 + 光的物理变化；情绪由动作呈现，不写心理词。
变化链：门闩→火苗→光束→闪电→灰蓝晨光→吹熄，全程「手→物→光」物理衔接。
总帧 362 = 5+17×21，约 15.08 秒，6 镜。
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is the lamp room at the top of an old seaside lighthouse at night: a ring of tall glass panes looking out over a dark ocean, a great brass Fresnel lens mounted in the centre on a spindle with a crank handle, a small brass oil lamp with a knob on the desk beside an open leather logbook and a fountain pen, a wooden spiral stairhead behind, and a low ceiling of dark beams. A thin line of moonlight lies on the sea; a storm front is gathering on the horizon. Inside, warm amber lamplight glints off the brass and glass."""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light, over a palette of warm amber lamplight "
         "against deep blue-black night and a thin silver line of moonlight on the sea.")

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
 # 1 开门：动作=拧门闩推门
 "A medium close-up of the brass door latch of the lamp room of <Subject 2>, with <Subject 1>'s WHITE-gloved right hand turning the round brass handle: the latch clicks, the heavy door swings inward, and a narrow blade of warm amber lamplight from inside widens across the dark stair behind her. Her BLACK-gloved left hand grips the door edge. The camera is a static shot, holding on the hand, the turning latch and the spreading light. No face is in frame.",
 # 2 点灯：动作=拧油灯旋钮
 "A tight close-up on the brass oil lamp on the desk of <Subject 2>: <Subject 1>'s WHITE-gloved right hand reaches in and turns the small brass knob on the lamp's base; the wick catches with a soft whoosh and a warm flame rises, throwing a growing pool of amber light across the open leather logbook and the fountain pen beside it. Her BLACK-gloved left hand holds the lamp's stem steady. The camera is a static shot, holding on the hand, the knob, the rising flame and the spreading light on the page. No face is in frame.",
 # 3 光束：动作=转透镜曲柄，光束扫海
 "A medium close-up of <Subject 1>, framed from the collarbone up, standing at the crank of the big brass Fresnel lens of <Subject 2>: she grips the wooden crank with her BLACK-gloved left hand and turns it, and the lens rotates so its beam sweeps across her face and out through the glass panes onto the black sea, where a thin blade of light travels across the water. Her pale icy-blue right eye and deeper violet-blue left eye catch the passing beam as it crosses her face. The camera pushes in with small amplitude at slow speed. She does not speak; her lips are pressed.",
 # 4 风暴：动作=抹玻璃水雾，看闪电
 "A tight close-up on the glass pane of <Subject 2> from inside: a flash of lightning brightens the sea beyond the glass; <Subject 1>'s WHITE-gloved right hand rises into frame and wipes a streak of condensation from the pane, clearing a small clear patch through which the black sea and the distant storm cloud are visible; a second flash throws her silhouette's edge of light. The camera is a static shot, holding on the hand, the wiped streak and the lightning beyond. Her face is out of frame at the top edge.",
 # 5 黎明：动作=拧小油灯，光束转灰蓝
 "A medium close-up of <Subject 1>, framed from the chest up, at the lamp table of <Subject 2>: she reaches with her WHITE-gloved right hand and turns the lamp knob back down a quarter turn; the flame drops low, and the light in the room shifts from amber toward grey-blue as the first flat dawn light comes through the panes behind her. The big lens has stopped turning. Her pale icy-blue right eye and deeper violet-blue left eye are both readable in the changed light; she lifts the fountain pen with her BLACK-gloved left hand and writes one short line in the open logbook. The camera is a static shot. She does not speak; her lips stay closed.",
 # 6 收尾：动作=合上日志本，吹熄油灯
 "A tight close-up on the desk of <Subject 2>: <Subject 1>'s WHITE-gloved right hand closes the leather logbook with a soft thump and lays the fountain pen across its cover; her BLACK-gloved left hand then pinches the brass knob of the oil lamp and turns it fully, and the flame gutters and goes out with a thin wisp of smoke, the amber glow dying and the room falling into flat grey-blue dawn light from the panes. The camera holds on the closed book, the still smoking wick and the cold morning light. No face is in frame.",
]

RET = """retention_analysis:
<Subject 1> (appears in full - head and face - in [Shot 3] and [Shot 5], and as her gloved hands only in [Shot 1], [Shot 2], [Shot 4] and [Shot 6] where her face is out of frame): fully_preserved - Furina's identity, her short wavy platinum silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared cuffs, the BLACK left glove and WHITE right glove, the bare legs with white ruffled ankle cuffs, and the dark-blue bow-topped ankle boots are all retained wherever she appears. She wears no headset microphone in this video.
<Subject 2> (appears in every shot): fully_preserved - the lamp room, the brass Fresnel lens on its spindle with the crank handle, the brass oil lamp with the knob, the open leather logbook and fountain pen, the glass panes, the black sea with the thin moonlight line, and the gathering storm are all retained throughout."""

SUMMARY = ("[reference generation] The target video is a single continuous fifteen-second scene in the lamp room "
           "of an old seaside lighthouse at night, told entirely through six physical actions in a clear chain: "
           "she turns the brass latch and opens the door into the lamp room, turns the oil lamp knob and lights "
           "the flame, turns the lens crank so the beam sweeps across the sea, wipes a streak of condensation "
           "from the glass as lightning flashes, turns the lamp low as grey dawn arrives and writes a line in the "
           "logbook, and finally closes the logbook and turns the lamp out, leaving the room in flat morning "
           "light. Six hard-cut shots, each keyed to one action and one change of light. <Picture 1> supplies "
           "identity and costume only and never serves as a concrete frame anchor.""")

SOUNDSCAPE = """overall_soundscape:
A small lamp-room room tone throughout - a low mechanical hum of the rotating lens, the soft creak of the wooden beams, and a distant low roar of the sea. [Shot 1] the click of the brass latch and the heavy creak of the door swinging open. [Shot 2] the soft whoosh of the wick catching and the faint crackle of the flame. [Shot 3] the ratchet click of the crank turning and the steady hum of the lens. [Shot 4] the soft wet sound of the glove wiping the glass and a low rumble of thunder. [Shot 5] the small click of the lamp knob and the scratch of the fountain pen on the page. [Shot 6] the soft thump of the logbook closing, the low guttering of the flame and its thin hiss as it goes out."""

MUSIC = """non_diegetic_music:
A slow, spare score of a single cello line over a soft low drone. It enters as the door opens in [Shot 1], adds a gentle woodwind phrase as the lamp flame rises in [Shot 2], swells as the beam sweeps the sea in [Shot 3], holds through the lightning in [Shot 4], softens as the dawn light arrives in [Shot 5], and resolves onto a single low held note that decays as the flame goes out in [Shot 6]."""

lines = [
    SUBJECTS, "",
    "summary:", SUMMARY, "",
    RET, "",
    "detailed_description:", STYLE + " " + FRAMING,
]
for i, s in enumerate(SHOTS):
    lines.append("[Shot %d] %s" % (i + 1, s))
lines += ["", SOUNDSCAPE, "", MUSIC, "", NEG]

p = os.path.join(OUT, "lighthouse2.txt")
open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote %s  %d B" % (os.path.basename(p), os.path.getsize(p)))
print("6 镜 × 362 帧 = 15.08s · 全程物理动作链条")
