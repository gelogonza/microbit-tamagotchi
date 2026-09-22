# =====================================================================
#  oontz_microbit.py  —  "oontz.mid" arranged for the micro:bit speaker
# ---------------------------------------------------------------------
#  MakeCode Python (static Python), NOT MicroPython.
#  Paste into https://makecode.microbit.org -> Python tab -> Blocks.
#
#  Source: oontz.mid — 4/4, 96 BPM, 192 ticks per quarter note.
#    Track 1 + Track 3  identical lead, a stream of eighth-note dyads
#                       (C5+A5 eleven times, then B4+G5 five times)
#    Track 2            bass riff: G1 A1 . . B1 E2, entering at bar 4
#
#  The micro:bit speaker is MONOPHONIC — one tone at a time. So the
#  three tracks are flattened into one line by two rules:
#    1. Of each lead dyad, keep the upper note (A5 / G5).
#    2. Where the bass sounds, the bass wins — except under the final
#       held note, where the lead wins so the piece ends up high.
#  The bass is raised two octaves (G1 -> G3). At its written pitch it is
#  ~49 Hz, which the on-board speaker cannot reproduce.
#
#  Result: 26-event intro, a 2-bar loop played 16 times, 6-event ending.
#  Runs about 92 seconds.
# =====================================================================

# ---- Timing ----------------------------------------------------------
# 96 BPM -> a quarter note is 625 ms -> a sixteenth is 156 ms.
SIXTEENTH = 156

# Silence at the end of every note. This is what makes the repeated
# eighth notes read as a pulse instead of one long smeared tone.
GAP = 15

# ---- Pitches (Hz) ----------------------------------------------------
LEAD_HIGH = 880   # A5   the "oontz" ostinato
LEAD_LOW = 784    # G5
BASS_1 = 196      # G3   written G1, raised two octaves
BASS_2 = 220      # A3
BASS_3 = 247      # B3
BASS_4 = 330      # E4

HOW_MANY_LOOPS = 16


# ---- One note, measured in sixteenths --------------------------------
def note(pitch, sixteenths):
    length = sixteenths * SIXTEENTH
    music.play_tone(pitch, length - GAP)
    music.rest(GAP)


# ---- A run of repeated eighth notes on one pitch ----------------------
def pulse(pitch, how_many):
    for i in range(how_many):
        note(pitch, 2)


# ---- Intro: lead only, before the bass enters ------------------------
def play_intro():
    pulse(LEAD_HIGH, 11)
    pulse(LEAD_LOW, 5)
    pulse(LEAD_HIGH, 10)


# ---- The 2-bar loop: 32 sixteenths -----------------------------------
def play_loop():
    note(LEAD_HIGH, 2)
    pulse(LEAD_LOW, 3)
    note(BASS_1, 4)
    note(BASS_2, 3)
    note(LEAD_HIGH, 1)
    pulse(LEAD_HIGH, 4)
    note(BASS_3, 4)
    note(BASS_4, 3)
    note(LEAD_HIGH, 1)


# ---- Ending ----------------------------------------------------------
def play_outro():
    note(LEAD_HIGH, 2)
    pulse(LEAD_LOW, 4)
    note(LEAD_LOW, 16)


# ---- The whole piece -------------------------------------------------
def play_oontz():
    play_intro()
    for i in range(HOW_MANY_LOOPS):
        led.plot(2, 2)
        play_loop()
        led.unplot(2, 2)
    play_outro()
    basic.clear_screen()


# ---- Button A: play it again -----------------------------------------
def on_button_a():
    play_oontz()


input.on_button_pressed(Button.A, on_button_a)


# ---- On start --------------------------------------------------------
music.set_volume(200)
play_oontz()
