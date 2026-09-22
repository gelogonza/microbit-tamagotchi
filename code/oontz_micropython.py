# =====================================================================
#  oontz_micropython.py  —  "oontz.mid" for the micro:bit speaker
# ---------------------------------------------------------------------
#  MicroPython. Paste into https://python.microbit.org or Mu.
#  This will NOT convert to blocks. For the MakeCode Python version
#  used by this project, see code/oontz_microbit.py instead.
#
#  Same arrangement as the MakeCode file: the three MIDI tracks are
#  flattened to one monophonic line, bass raised two octaves so the
#  speaker can reproduce it. See oontz_microbit.py for the full notes.
# =====================================================================

from microbit import *
import music

SIXTEENTH = 156   # 96 BPM
GAP = 15          # staccato gap, keeps the eighth-note pulse audible

A5 = 880
G5 = 784
G3 = 196
A3 = 220
B3 = 247
E4 = 330

# (pitch, length in sixteenth notes)
INTRO = [(A5, 2)] * 11 + [(G5, 2)] * 5 + [(A5, 2)] * 10

LOOP = ([(A5, 2)] + [(G5, 2)] * 3
        + [(G3, 4), (A3, 3), (A5, 1)]
        + [(A5, 2)] * 4
        + [(B3, 4), (E4, 3), (A5, 1)])

OUTRO = [(A5, 2)] + [(G5, 2)] * 4 + [(G5, 16)]

TUNE = INTRO + LOOP * 16 + OUTRO


def play(tune):
    for pitch, sixteenths in tune:
        music.pitch(pitch, sixteenths * SIXTEENTH - GAP)
        sleep(GAP)


play(TUNE)

while True:
    if button_a.was_pressed():
        play(TUNE)
    sleep(50)
