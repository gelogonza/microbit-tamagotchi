# TAMAGOTCHI MICRO:BIT 
# A = small task, B = big task, shake = play, A+B = rest.
# Food, happiness, and energy are separate stats kept between 0 and 100.

##############################################      POINT SYSTEM      ##################################################################   
# A small task gives food +8, happiness +10, and 1 care point.
# A big task gives happiness +25 and 2 care points, but costs food -3 and energy -5.
# Playing gives happiness +8 and 1 care point, but costs food -2 and energy -4.
# Resting gives energy +25, costs food -2, and does not give a care point.
# Every 5 total care points raises the pet one level; care points do not reset.
# Every 30 seconds, food loses 4, happiness loses 2, and energy loses 3.
# If food or energy reaches 0, happiness loses an additional 5 each decay cycle.
# The average of the three stats controls the pet's mood.

# ---------- Tuning ----------
DECAY_SECONDS = 30
MAX_STAT = 100
SMALL_TASK_BOOST = 10
BIG_TASK_BOOST = 25
PLAY_BOOST = 8
REST_BOOST = 25

# ---------- inital pet state  ----------
food = 80
happiness = 70
energy = 80
level = 1
care_points = 0
seconds_since_decay = 0
reacting = False


def clamp_stat(value: number):
    return min(MAX_STAT, max(0, value))


def pet_score():
    return (food + happiness + energy) // 3


def draw_pet():
    score = pet_score()
    if score == 0:
        basic.show_icon(IconNames.SKULL)
    elif food < 20 or happiness < 20 or energy < 20:
        basic.show_icon(IconNames.SAD)
    elif score >= 85:
        basic.show_icon(IconNames.FABULOUS)
    elif score >= 55:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.CONFUSED)


def show_reaction(icon: IconNames, note: number):
    global reacting
    reacting = True
    basic.show_icon(icon)
    music.play_tone(note, music.beat(BeatFraction.EIGHTH))
    basic.pause(350)
    reacting = False


# Small task
def show_small_task_reaction():
    global reacting
    reacting = True
    music.play_tone(Note.C, music.beat(BeatFraction.SIXTEENTH))
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.pause(80)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
    basic.pause(80)
    basic.show_icon(IconNames.YES)
    basic.pause(150)
    reacting = False


# Big task
def show_big_task_reaction():
    global reacting
    reacting = True
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    music.play_tone(587, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(740, music.beat(BeatFraction.SIXTEENTH))
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
    music.play_tone(880, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(1109, music.beat(BeatFraction.SIXTEENTH))
    basic.show_icon(IconNames.HEART)
    music.play_tone(1319, music.beat(BeatFraction.EIGHTH))
    music.play_tone(1175, music.beat(BeatFraction.SIXTEENTH))
    basic.pause(150)
    reacting = False


# Shake
def show_cat_chirp_reaction():
    global reacting
    reacting = True
    basic.show_icon(IconNames.SURPRISED)
    music.play_tone(784, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(988, music.beat(BeatFraction.SIXTEENTH))
    basic.pause(120)
    reacting = False


# level up
def play_level_up_fanfare():
    music.play_tone(659, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(784, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(988, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(1175, music.beat(BeatFraction.EIGHTH))
    music.play_tone(1047, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(1319, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(1568, music.beat(BeatFraction.QUARTER))


def add_care(points: number):
    global care_points, level, reacting
    care_points += points
    if care_points >= level * 5:
        level += 1
        reacting = True
        basic.show_icon(IconNames.DIAMOND)
        play_level_up_fanfare()
        basic.show_number(level)
        basic.pause(500)
        reacting = False


def on_button_a():
    global food, happiness
    food = clamp_stat(food + 8)
    happiness = clamp_stat(happiness + SMALL_TASK_BOOST)
    show_small_task_reaction()
    add_care(1)


input.on_button_pressed(Button.A, on_button_a)


def on_button_b():
    global food, happiness, energy
    food = clamp_stat(food - 3)
    happiness = clamp_stat(happiness + BIG_TASK_BOOST)
    energy = clamp_stat(energy - 5)
    show_big_task_reaction()
    add_care(2)


input.on_button_pressed(Button.B, on_button_b)


def on_shake():
    global food, happiness, energy
    food = clamp_stat(food - 2)
    happiness = clamp_stat(happiness + PLAY_BOOST)
    energy = clamp_stat(energy - 4)
    show_cat_chirp_reaction()
    add_care(1)


input.on_gesture(Gesture.SHAKE, on_shake)


def on_button_ab():
    global food, energy
    food = clamp_stat(food - 2)
    energy = clamp_stat(energy + REST_BOOST)
    show_reaction(IconNames.ASLEEP, Note.C)


input.on_button_pressed(Button.AB, on_button_ab)


def update_pet():
    global food, happiness, energy, seconds_since_decay
    seconds_since_decay += 1

    if seconds_since_decay >= DECAY_SECONDS:
        seconds_since_decay = 0
        food = clamp_stat(food - 4)
        happiness = clamp_stat(happiness - 2)
        energy = clamp_stat(energy - 3)

        if food == 0 or energy == 0:
            happiness = clamp_stat(happiness - 5)

    if not reacting:
        draw_pet()

    basic.pause(1000)


music.start_melody(music.built_in_melody(Melodies.BA_DING),
    MelodyOptions.ONCE)
basic.forever(update_pet)
