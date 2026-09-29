#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成《煲汤》六镜 H3 Ref2VA 提示词。
每镜 124 帧 (5.167s) = 一个二采段 ⇒ 硬切点与接缝按构造精确重合。
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/prompts"
os.makedirs(OUT, exist_ok=True)

SUBJECTS = """subject_definitions:
<Subject 1> (S1) is Furina (芙宁娜), the Hydro Archon of Fontaine in Genshin Impact, whose exact design is shown in <Picture 1>, a single full-body standing view. Her hair is short and wavy, platinum silver-white, falling to her jaw with longer strands at the sides, and it carries only a few faint pale-aqua streaks close to her face rather than any full colour gradient; a single thin white curl springs up from the top of her head, and one longer lock falls across one eye. She has HETEROCHROMATIC eyes: her right eye is a pale icy blue and her left eye is a deeper violet-blue; her skin is pale. She wears a small dark-navy crown-shaped hat topped with tall gold spikes and a blue ribbon, tilted to one side of her head. Her outfit is a navy-blue tailcoat with gold-trimmed lapels and a row of gold buttons down each side, a white ruffled shirt front, a large blue-and-gold bow holding a round blue gem at her chest, a second matching bow with hanging tassels at her left hip, small blue teardrop gems hanging from gold fittings, black shorts with a dark garter strap around one thigh, and a long dark-navy back panel with gold filigree hanging behind her. Her sleeves end in large ornate gold-and-white flared cuffs. She wears a BLACK glove on her left hand and a WHITE glove on her right hand. Her legs are bare, her ankles carry white ruffled cuffs, and she wears small dark-blue ankle boots, each with a blue bow on the front. She has NO headset microphone in this video. Her voice is a clear, bright young woman's voice.
<Subject 2> is the kitchen she is cooking in: a warm traditional Chinese kitchen at dusk, with terracotta-tiled walls, a heavy dark-stained wooden counter, a black iron gas range with a low blue flame ring, a dark earthenware clay pot with a heavy lid, a stainless steel pot, a bamboo cutting board, glazed ceramic jars of dried goods, a bamboo steamer, bundles of dried herbs and a string of red chillies hanging from a wooden rail, and copper ladles on hooks. Soft honeyed late-afternoon light comes in from a tall window on the left and lays a warm bar of light across the counter; the air carries visible steam. The palette is terracotta, honey amber, deep brown shadow and the cool aqua accents of her hair.
"""

STYLE = ("The target video is in official Genshin Impact anime style: cel-shaded with vibrant painterly "
         "colours, crisp clean line art and soft volumetric light, over a warm kitchen palette of terracotta, "
         "honeyed amber and deep brown shadow cut by the soft window light from the left, with cool aqua accents "
         "in her hair. Steam is present in the air and catches the light.")

FRAMING = ("The framing discipline for this video is absolute: EVERY shot is a medium shot or a close shot. "
           "There are no wide shots, no full-body shots and no long shots anywhere in this video. The frame is "
           "always filled by one of three things - her upper body together with her face, her hands together with "
           "the ingredients, or the pot together with the stove. Whenever she is in shot her head occupies a large "
           "part of the frame and her face is rendered in full detail, with her pale icy-blue right eye and her "
           "deeper violet-blue left eye both clearly readable.")

SHOTS = [
 dict(
  n=1, tag="备料",
  summary="She prepares the ingredients for a clear slow-simmered soup at the counter, laying them out and slicing ginger.",
  desc="[Shot 1] A medium close-up, framed from the chest up and seen slightly from her right side: <Subject 1> stands at the heavy dark wooden counter of <Subject 2>, her head and shoulders filling the left half of the frame, her body turned three-quarters toward the camera. On the bamboo cutting board in front of her the ingredients for a clear soup are laid out in small neat groups: a pile of blanched pork ribs, three segments of sweet corn, thick orange carrot rounds, a knuckle of ginger, a handful of dark red dates and a scatter of goji berries in a small white dish. Her WHITE-gloved right hand lifts a slice of ginger between thumb and forefinger and sets it down on the board; her BLACK-gloved left hand rests flat and steady on the wood beside the board. Her pale icy-blue right eye and her deeper violet-blue left eye are both clearly visible and catch the warm window light from the left. She looks down at the board with a small, absorbed, quietly pleased expression, her lips pressed. The camera pushes in with small amplitude at slow speed, tightening gently on her hands and her face. She does not speak in this shot; her lips stay closed.",
  sound="A quiet kitchen room tone with a low gas hiss and a faint bubbling simmer from a pot just out of frame. In this shot: the soft wooden knock of the knife and the ginger slice meeting the bamboo board, the small ceramic clink of the white dish, the rustle of her coat cuff, and the thin high ring of the clay pot warming on the stove.",
  music="A warm, unhurried solo guzheng figure over a soft low drone at a slow tempo, with a single deep wooden percussion tap on the first beat. It enters gently under her first hand movement and stays level, leaving space for the kitchen sound.",
 ),
 dict(
  n=2, tag="焯水",
  summary="A tight insert shot of pork ribs going into boiling water, foam blooming and steam pouring up.",
  desc="[Shot 2] A tight close-up on the pot, seen from slightly above and to one side, with no face and no person's body in frame: a stainless steel pot of water has just come to a hard rolling boil on the black iron range. <Subject 1>'s WHITE-gloved right hand comes into frame and drops the pork ribs into the water one piece at a time; each piece breaks the surface and the water surges up around it. Grey-white foam blooms and swirls outward across the surface in slow rings, and thick steam pours straight up past the lens and fogs the upper corner of the frame. Her BLACK-gloved left hand holds a pair of long wooden chopsticks steady above the rim, and the chopsticks nudge one rib down under the surface. The camera is a static shot, holding tight on the churning water, the blooming foam and the rising steam.",
  sound="A close, loud, wet sound: the hard rolling boil of the water, the soft heavy plop of each rib breaking the surface, the hiss and roar of the gas flame under the pot, and the fine high sizzle of steam escaping. The kitchen room tone sits far behind it.",
  music="The guzheng figure continues but thins to a bare repeating two-note cell, and a soft low string swell rises underneath the boiling, tightening the texture without ever becoming loud.",
 ),
 dict(
  n=3, tag="入锅",
  summary="She layers the blanched ingredients into the clay pot and pours in clear water.",
  desc="[Shot 3] A medium close-up, seen from her left at counter height: a dark earthenware clay pot with its heavy lid set aside sits on the range, and <Subject 1>, framed from the waist up with her face in the upper right of the frame, leans in over it. Her WHITE-gloved right hand lays the blanched pork ribs into the bottom of the pot, then the corn segments, the carrot rounds, the ginger and the red dates, each going in one after another and settling with a small soft sound; her BLACK-gloved left hand steadies the pot's rim. She then lifts a glazed ceramic jug and pours a thin clear stream of water down the inside wall of the pot, and the water rises up the sides and covers the ingredients. Her pale icy-blue right eye and her deeper violet-blue left eye are both clearly readable in the warm light; she watches the pot with narrowed, concentrated eyes and her brow is slightly drawn. The camera tilts down with small amplitude at slow speed, following her hands into the pot. She does not speak in this shot; her lips stay closed.",
  sound="The dry ceramic knock of each ingredient meeting the clay pot, the soft wet thud of the ribs, the light clink of the jug's lip, and a long smooth pour of water rising in pitch as the pot fills. Underneath, the steady low gas hiss and the kitchen room tone.",
  music="The two-note cell opens back out into the full guzheng figure, and the low drone warms and rises a step as the water goes in, marking the turn of the dish.",
 ),
 dict(
  n=4, tag="大火",
  summary="A tight insert shot of the roaring flame and the hard rolling boil under the clay pot.",
  desc="[Shot 4] A tight close-up, low and to one side, with no face in frame: the blue-and-orange gas flame roars up around the base of the dark clay pot, licking at its curved belly and washing the terracotta tiles behind it in a moving orange light. The water inside has come to a hard rolling boil; the heavy lid chatters against the rim and lifts a fraction on a jet of steam, then drops back. Beads of condensation run down the glazed side of the pot and hiss into vapour when they reach the flame. The camera pushes in with small amplitude at slow speed, closing on the flame ring and the trembling lid.",
  sound="A hard, close, roaring sound: the deep rushing roar of the gas ring, the dense bubbling of a fast boil inside the clay pot, the metallic chatter of the heavy lid on the rim, and the sharp hiss of condensation flashing off the pot's side.",
  music="The guzheng drops out entirely and the score becomes a single low held string note with a slow tremolo, letting the flame and the boil carry the shot.",
 ),
 dict(
  n=5, tag="转小火",
  summary="A tight insert shot of the flame being turned down to a low blue ring, and the lid lifted a fraction.",
  desc="[Shot 5] A tight close-up on the range controls and the base of the clay pot, with no face in frame: <Subject 1>'s BLACK-gloved left hand reaches into the frame and turns the dark metal knob down. The roaring ring of flame collapses inward and settles into a low, steady, quiet blue circle that barely touches the pot, and the orange light on the terracotta tiles behind it dies back to a soft warm glow. In the same shot her WHITE-gloved right hand lifts the heavy lid a fraction and sets it back down on the rim, and a slow gentle plume of steam curls up out of the gap and drifts across the lens. The camera is a static shot, holding steady on the low blue flame and the settling steam.",
  sound="The mechanical click and soft grind of the knob turning, the roar of the flame dropping away into a quiet low hiss, the heavy ceramic settle of the lid going back onto the rim, and then a much softer, slower bubbling from inside the pot. The kitchen room tone comes forward again into the new quiet.",
  music="The low held string note softens and lengthens, and the warm drone returns underneath it at a slower tempo, settling the film into its long simmer.",
 ),
 dict(
  n=6, tag="盛汤",
  summary="She ladles the clear golden broth into a bowl, tastes it, and smiles.",
  desc="[Shot 6] A medium close-up, framed from the chest up and seen slightly from her right: <Subject 1> stands at the counter and lifts a full copper ladle of clear golden broth up out of the clay pot, then pours it slowly into a white ceramic bowl in which the corn, carrot and ribs are already arranged. The broth runs off the ladle in a single unbroken glossy ribbon, and steam curls up between her face and the bowl, softening the lower half of the frame. Her pale icy-blue right eye and her deeper violet-blue left eye are both clearly readable in the warm light. She sets the ladle down, lifts the bowl in both gloved hands, blows once gently across the surface so the steam bends away, takes a small sip, and her eyes soften and narrow into a small, warm, satisfied smile. The camera pushes in with small amplitude at slow speed, ending close on her face. Her mouth opens and she says, <d>[Chinese] 好了。</d> and then her lips close on the smile and she holds the expression.",
  sound="The long wet pour of broth into the ceramic bowl, the light ring of the copper ladle set down on the counter, the small ceramic tick of the bowl lifted in both hands, one soft breath blown across the surface, and a quiet sip. Behind it all the low steady simmer of the pot and the warm kitchen room tone.",
  music="The full guzheng figure returns warmly and resolves upward as the broth is poured, holds through her sip, and then settles onto a single soft plucked note that decays under the held final expression.",
 ),
]

NEG = ("Do not render storyboard line art, sketch lines, labels, captions, watermarks, on-screen text, "
       "duplicated or mirror-image figures, extra limbs, extra hands or extra fingers, distorted or "
       "photorealistic live-action faces, or a wide or full-body shot.")

for s in SHOTS:
    body = []
    body.append(SUBJECTS)
    body.append("")
    body.append("summary:")
    body.append("[reference generation] The target video is a single continuous five-second shot from a "
                "Genshin Impact anime-style cooking sequence titled Slow-Simmered Soup, set entirely inside "
                "<Subject 2>. " + s["summary"] + " The shot runs the full five seconds without any internal cut, "
                "and the camera makes exactly one slow move. <Picture 1> supplies identity and costume only and "
                "never serves as a concrete frame anchor.")
    body.append("")
    body.append("retention_analysis:")
    body.append("<Subject 1> (appears in [Shot 1]): fully_preserved - Furina's identity, her short wavy platinum "
                "silver-white hair with faint pale-aqua streaks near the face, the thin white curl on top, the lock "
                "across one eye, her pale icy-blue right eye and deeper violet-blue left eye, the dark-navy "
                "crown-shaped hat with tall gold spikes and blue ribbon, the navy tailcoat with gold-trimmed lapels "
                "and gold buttons, the white ruffled shirt front, the blue-and-gold bow with the round blue gem at "
                "her chest and the matching tasselled bow at her hip, the hanging blue teardrop gems, the black "
                "shorts and thigh garter strap, the long navy filigreed back panel, the large gold-and-white flared "
                "cuffs, and the BLACK left glove and WHITE right glove are all retained. She wears no headset "
                "microphone in this video.")
    body.append("<Subject 2> (appears in [Shot 1]): fully_preserved - the terracotta-tiled walls, the heavy dark "
                "wooden counter, the black iron gas range, the dark earthenware clay pot, the stainless steel pot, "
                "the bamboo cutting board, the glazed ceramic jars, the hanging dried herbs and red chillies, the "
                "copper ladles on hooks, and the warm bar of window light from the left are all retained.")
    body.append("")
    body.append("detailed_description:")
    body.append(STYLE + " " + FRAMING)
    body.append(s["desc"])
    body.append("")
    body.append("overall_soundscape:")
    body.append(s["sound"])
    body.append("")
    body.append("non_diegetic_music:")
    body.append(s["music"])
    body.append("")
    body.append(NEG)
    p = "%s/soup_s%d.txt" % (OUT, s["n"])
    open(p, "w", encoding="utf-8").write("\n".join(body) + "\n")
    print("wrote %-34s %5d bytes  [S%d %s]" % (p, os.path.getsize(p), s["n"], s["tag"]))
print("\n共 %d 镜 × 124 帧 = %d 帧 = %.2f 秒" % (len(SHOTS), len(SHOTS)*124, len(SHOTS)*124/24.0))
