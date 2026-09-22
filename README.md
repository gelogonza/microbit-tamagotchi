# micro:bit Tamagotchi

This project turns a BBC micro:bit into a task-tracking digital pet. Completing
real tasks improves the pet's condition, while ignoring it causes its needs and
mood to decline.

## Hardware

- BBC micro:bit V2
- Two-AAA battery pack
- Optional cat-shaped enclosure

No breadboard or external screen is required. The pet uses the micro:bit's LED
matrix, buttons, accelerometer, and speaker.

## Controls and points

| Action | Result |
| --- | --- |
| Press A — small task | Food +8, happiness +10, care +1 |
| Press B — big task | Happiness +25, care +2, food -3, energy -5 |
| Shake — play | Happiness +8, care +1, food -2, energy -4 |
| Press A+B — rest | Energy +25 and food -2 |

Every five cumulative care points increases the pet's level. Each action has a
short LED animation and sound, including a fairy-style big-task chime and a
retro level-up fanfare.

## Needs and emotions

Food starts at 80, happiness at 70, and energy at 80. Every 30 seconds they
decrease by 4, 2, and 3 respectively. If food or energy reaches zero,
happiness loses another 5 per decay cycle. The average controls the face:
Fabulous at 85+, Happy at 55+, Confused below 55, Sad when any need is below
20, and Skull when the overall score reaches zero.

The MakeCode Python program is in [`tamagotchi.py`](tamagotchi.py). Paste it
into a micro:bit MakeCode Python project and download it to the board.
