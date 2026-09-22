# =====================================================================
#  hello_microbit.py  —  INFO-I 341 default starter project
# ---------------------------------------------------------------------
#  MakeCode Python (static Python), NOT MicroPython.
#  Paste into https://makecode.microbit.org -> Python tab -> Blocks.
#
#  What it does:
#    Button A      count up and show the number
#    Button B      reset the count to zero
#    Shake         show a face
#    Forever       blink one pixel in the top-right corner (a "still alive" light)
#
#  This is deliberately small. It is your starting point, not your project.
#  Change it, break it, test it, and record what you find.
# =====================================================================

# ---- Variables ------------------------------------------------------
count = 0


# ---- Button A: count up ---------------------------------------------
def on_button_a():
    global count
    count += 1
    basic.show_number(count)


input.on_button_pressed(Button.A, on_button_a)


# ---- Button B: reset -------------------------------------------------
def on_button_b():
    global count
    count = 0
    basic.show_icon(IconNames.NO)
    basic.pause(300)
    basic.clear_screen()


input.on_button_pressed(Button.B, on_button_b)


# ---- Shake -----------------------------------------------------------
def on_shake():
    basic.show_icon(IconNames.SURPRISED)
    basic.pause(500)
    basic.clear_screen()


input.on_gesture(Gesture.SHAKE, on_shake)


# ---- On start --------------------------------------------------------
basic.show_icon(IconNames.HEART)
basic.pause(500)
basic.clear_screen()


# ---- Forever: heartbeat pixel ---------------------------------------
def on_forever():
    led.plot(4, 0)
    basic.pause(500)
    led.unplot(4, 0)
    basic.pause(500)


basic.forever(on_forever)
