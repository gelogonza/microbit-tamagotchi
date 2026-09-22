SIXTEENTH = 156
GAP = 15

LEAD_HIGH = 880
LEAD_LOW = 784
BASS_1 = 196
BASS_2 = 220
BASS_3 = 247
BASS_4 = 330

HOW_MANY_LOOPS = 16


def play_note(pitch, sixteenths):
    length = sixteenths * SIXTEENTH
    music.play_tone(pitch, length - GAP)
    music.rest(GAP)


def play_pulse(pitch, how_many):
    for i in range(how_many):
        play_note(pitch, 2)


def play_intro():
    play_pulse(LEAD_HIGH, 11)
    play_pulse(LEAD_LOW, 5)
    play_pulse(LEAD_HIGH, 10)


def play_loop():
    play_note(LEAD_HIGH, 2)
    play_pulse(LEAD_LOW, 3)
    play_note(BASS_1, 4)
    play_note(BASS_2, 3)
    play_note(LEAD_HIGH, 1)
    play_pulse(LEAD_HIGH, 4)
    play_note(BASS_3, 4)
    play_note(BASS_4, 3)
    play_note(LEAD_HIGH, 1)


def play_outro():
    play_note(LEAD_HIGH, 2)
    play_pulse(LEAD_LOW, 4)
    play_note(LEAD_LOW, 16)


def play_oontz():
    play_intro()
    for i in range(HOW_MANY_LOOPS):
        led.plot(2, 2)
        play_loop()
        led.unplot(2, 2)
    play_outro()
    basic.clear_screen()


# Button A: play "oontz"
def on_button_pressed_a():
    play_oontz()


input.on_button_pressed(Button.A, on_button_pressed_a)


# Button A+B: PRELUDE in the background
def on_button_pressed_ab():
    music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
        music.PlaybackMode.IN_BACKGROUND)


input.on_button_pressed(Button.AB, on_button_pressed_ab)


# Button B: start recording
def on_button_pressed_b():
    record.start_recording(record.BlockingState.BLOCKING)


input.on_button_pressed(Button.B, on_button_pressed_b)


# Shake: square-wave blip
def on_gesture_shake():
    music.set_volume(255)
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            1,
            4788,
            255,
            255,
            500,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)


input.on_gesture(Gesture.SHAKE, on_gesture_shake)


# Logo touch: play back the recording
def on_logo_pressed():
    record.play_audio(record.BlockingState.BLOCKING)


input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)


# On start
images.icon_image(IconNames.GHOST).show_image(0, 400)
music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
    music.PlaybackMode.UNTIL_DONE)


def on_forever():
    pass


basic.forever(on_forever)
