# =====================================================================
#  micro:bit "BLOCK TOUR"  —  MakeCode Python
#  ---------------------------------------------------------------
#  Paste into https://makecode.microbit.org  ->  Python tab,
#  then click "Blocks".
#
#  This is MakeCode Python (static Python), NOT MicroPython.
#
#  Constructs deliberately avoided because they do NOT convert:
#    - ternary expressions   (x if cond else y)
#    - "is" / "is None"
#    - docstrings (bare strings inside a function)
#    - f-strings, dicts, list comprehensions, try/except
#    - variable names that collide with namespaces (light, text, input...)
# =====================================================================


# =====================================================================
#  1. VARIABLES
# =====================================================================
count = 0
mode = 0
message = ""
readings = [0, 0, 0]
armed = False
game_started = False
player: game.LedSprite = None


# =====================================================================
#  2. FUNCTIONS
# =====================================================================
def show_banner(msg: str, times: number):
    for i in range(times):
        basic.show_string(msg)
        basic.pause(200)


def clamp(value: number, low: number, high: number):
    return min(max(value, low), high)


def log_reading(value: number):
    global readings
    readings.append(value)
    if len(readings) > 8:
        readings.pop()
    serial.write_value("reading", value)


# =====================================================================
#  3. INPUT — BUTTONS
# =====================================================================
def on_button_a():
    global count
    count += 1
    basic.show_number(count)


input.on_button_pressed(Button.A, on_button_a)


def on_button_b():
    global count
    count -= 1
    basic.show_number(count)


input.on_button_pressed(Button.B, on_button_b)


def on_button_ab():
    global count, mode
    count = 0
    mode = (mode + 1) % 3
    basic.show_string("M" + str(mode))


input.on_button_pressed(Button.AB, on_button_ab)


# =====================================================================
#  4. INPUT — GESTURES AND TOUCH PINS
# =====================================================================
def on_shake():
    global count
    count = randint(1, 6)
    basic.show_number(count)


input.on_gesture(Gesture.SHAKE, on_shake)


def on_logo_up():
    basic.show_arrow(ArrowNames.NORTH)


input.on_gesture(Gesture.LOGO_UP, on_logo_up)


def on_pin_p0():
    music.play_tone(Note.C, music.beat(BeatFraction.HALF))


input.on_pin_pressed(TouchPin.P0, on_pin_p0)


def on_pin_p2():
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                       MelodyOptions.ONCE)
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(Note.G, music.beat(BeatFraction.WHOLE))


input.on_pin_pressed(TouchPin.P2, on_pin_p2)


# =====================================================================
#  5. RADIO
# =====================================================================
radio.set_group(7)


def on_received_number(received_number: number):
    basic.show_number(received_number)
    led.plot_bar_graph(received_number, 100)


radio.on_received_number(on_received_number)


def on_received_string(received_string: str):
    global message
    message = received_string
    basic.show_string(message)


radio.on_received_string(on_received_string)


# =====================================================================
#  6. ON START  (top-level code == the 'on start' block)
# =====================================================================
led.set_brightness(200)
music.set_tempo(120)
input.set_accelerometer_range(AcceleratorRange.FOUR_G)
serial.write_line("micro:bit block tour ready")

basic.show_icon(IconNames.HEART)
basic.pause(300)
basic.show_leds("""
    . # . # .
    # # # # #
    # # # # #
    . # # # .
    . . # . .
    """)
basic.pause(300)
basic.clear_screen()

show_banner("GO", 1)


# =====================================================================
#  7. FOREVER LOOP
# =====================================================================
def on_forever():
    global count, player, armed, game_started

    if mode == 0:
        # LED plotting + loops
        for x in range(5):
            led.plot(x, 2)
            basic.pause(60)
            led.unplot(x, 2)
        led.plot_brightness(2, 2, 128)
        if led.point(2, 2):
            led.toggle(2, 2)

    elif mode == 1:
        # Sensors + math + arrays
        light_value = input.light_level()
        temp_value = input.temperature()
        tilt = input.acceleration(Dimension.X)
        heading = input.compass_heading()

        log_reading(light_value)
        led.plot_bar_graph(clamp(light_value, 0, 255), 255)

        if tilt > 300:
            basic.show_arrow(ArrowNames.EAST)
        elif tilt < -300:
            basic.show_arrow(ArrowNames.WEST)

        serial.write_value("temp", temp_value)
        serial.write_value("heading", heading)
        serial.write_value("tilt", abs(tilt))

    else:
        # Game category
        if not game_started:
            player = game.create_sprite(2, 2)
            game_started = True
        if input.button_is_pressed(Button.A):
            player.change(LedSpriteProperty.X, -1)
        if input.button_is_pressed(Button.B):
            player.change(LedSpriteProperty.X, 1)
        player.change(LedSpriteProperty.Y, 1)
        if player.get(LedSpriteProperty.Y) >= 4:
            game.add_score(1)
            player.set(LedSpriteProperty.Y, 0)

    # Pins
    if armed:
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)

    pins.analog_write_pin(AnalogPin.P2, clamp(count * 25, 0, 1023))
    knob = pins.analog_read_pin(AnalogPin.P2)
    if knob > 900:
        pins.servo_write_pin(AnalogPin.P2, 90)

    armed = not armed
    basic.pause(100)


basic.forever(on_forever)


# =====================================================================
#  8. CONTROL — background thread
# =====================================================================
def heartbeat():
    while True:
        radio.send_number(count)
        music.ring_tone(262)
        basic.pause(50)
        music.stop_all_sounds()
        control.wait_micros(500)
        basic.pause(5000)


control.in_background(heartbeat)


# =====================================================================
#  9. micro:bit V2 ONLY — delete this section on a V1 board
# =====================================================================
def on_loud():
    basic.show_icon(IconNames.SURPRISED)
    basic.pause(500)
    basic.clear_screen()


input.on_sound(DetectedSound.LOUD, on_loud)


def on_logo_pressed():
    soundExpression.giggle.play()
    serial.write_value("mic", input.sound_level())


input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
