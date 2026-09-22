# Changes — button A now plays "oontz"

**2026-08-31**

Source file: `code/oontz_project.py`
Origin: `~/Downloads/oontz.mid`

---

## Changed

**Button A.** Was the built-in NYAN melody:

```python
def on_button_pressed_a():
    music.play(music.built_in_playable_melody(Melodies.NYAN),
        music.PlaybackMode.UNTIL_DONE)
```

Now calls the arrangement:

```python
def on_button_pressed_a():
    play_oontz()
```

This is the only edit to existing behavior. Button B, button A+B, shake, logo
touch, the GHOST/POWER_UP start sequence, and the empty `forever` loop are
unchanged.

**Comments.** Reduced to one line above each feature. The arrangement notes that
used to sit in the file header are recorded below instead.

## Added

Eleven constants and six functions above the handlers, all supporting button A:

| Name | Purpose |
|---|---|
| `SIXTEENTH = 156` | Length of a sixteenth note in ms. 96 BPM. |
| `GAP = 15` | Silence at the end of every note. |
| `LEAD_HIGH`, `LEAD_LOW` | 880 Hz, 784 Hz — A5 and G5. |
| `BASS_1`–`BASS_4` | 196, 220, 247, 330 Hz — G3, A3, B3, E4. |
| `HOW_MANY_LOOPS = 16` | Repeats of the 2-bar loop. |
| `play_note(pitch, sixteenths)` | One note plus its gap. |
| `play_pulse(pitch, how_many)` | A run of repeated eighth notes. |
| `play_intro`, `play_loop`, `play_outro` | The three sections. |
| `play_oontz` | The whole piece, with a centre-pixel blink per loop. |

## Why the arrangement looks like this

`oontz.mid` is 4/4, 96 BPM, 192 ticks per quarter note, four tracks. Tracks 1
and 3 are byte-identical duplicates, so there are really two voices:

- **Lead** — eighth-note *dyads*: C5+A5 eleven times, then B4+G5 five times,
  repeating 18 times.
- **Bass** — enters at bar 4: G1, A1, rest, B1, E2, on a 2-bar cycle.

The speaker is monophonic, so the dyads cannot survive. Three decisions:

1. **Keep the upper note of each lead dyad** (A5 / G5), discard the lower.
2. **The bass wins wherever it sounds.** It is the actual riff; the lead is a
   two-note ostinato. Exception: under the final held note the lead wins, so the
   piece ends high rather than on a low drone.
3. **The bass is raised two octaves** (G1 → G3). At its written pitch it is
   about 49 Hz, below what the on-board speaker can reproduce.

Every duration in the MIDI is a multiple of 48 ticks, so everything lands on a
sixteenth-note grid with no quantizing. The flattened result is a 26-event
intro, a 32-sixteenth loop played 16 times, and a 6-event ending — 590
sixteenths, about 92 seconds.

`GAP` is load-bearing. The lead re-articulates the *same pitch* on every eighth;
that repetition is the "oontz". With `GAP = 0` the notes run together into one
continuous tone and the pulse disappears.

## Behavior worth knowing before testing

- **Button A blocks for about 92 seconds.** `music.play_tone` is blocking.
  During playback, shake and logo touch do not respond. Pressing A again
  **queues a second full playthrough** rather than restarting or being ignored.
  Set `HOW_MANY_LOOPS` to 2 or 3 for testing; the intro and ending stay intact.
- **Shake permanently raises volume.** `music.set_volume(255)` in the shake
  handler has no matching reset, so after any shake, oontz plays at full volume
  for the rest of the session. Pre-existing behavior, but far more noticeable
  now that button A runs for a minute and a half.

## Identifier status

Resolved by the existing working code — `knowledge/platform-notes/microbit-makecode.md`
lists both of these under "Known-unverified in this repo":

- `TouchButtonEvent.PRESSED` — in use, works.
- `music.set_volume` — in use, works.

Still unverified, introduced by this change:

- `music.play_tone(frequency, ms)`
- `music.rest(ms)`

Both came from an LLM, not from the editor. Per the platform notes, drag the
"play tone" and "rest" blocks onto the canvas and read what the Python tab
generates. That is the authority.

## Related files

- `code/oontz_microbit.py` — the arrangement alone, MakeCode Python, still
  fully commented.
- `code/oontz_micropython.py` — MicroPython version for python.microbit.org or
  Mu. Will not convert to blocks.
