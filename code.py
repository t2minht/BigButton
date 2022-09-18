import time
import board
import usb_hid
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

# ----- Keyboard setup ----- #
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)


# ----- Key setup ----- #
switch_in = board.D4                # Creates object for pin
switch = DigitalInOut(switch_in)    # Creates object to represent input for pin object
switch.direction = Direction.INPUT
switch.pull = Pull.UP

led_pin = board.D6                  # Creates object for pin
led = DigitalInOut(led_pin)         # Creates object to represent input for pin object
led.direction = Direction.OUTPUT



pressed = False

while True:

    if switch.value is False and not pressed:
        pressed = True
        led.value = True
        time.sleep(.05)
        keyboard.press(Keycode.LEFT_SHIFT)
        keyboard.press(Keycode.GRAVE_ACCENT)
        if switch.value is True:
            led.value = False

    if switch.value is True and pressed:
        pressed = False
        led.value = False
        keyboard.release(Keycode.GRAVE_ACCENT)
        keyboard.release(Keycode.LEFT_SHIFT)


# Single key press
# keyboard.press(Keycode.ENTER)
# keyboard.release(Keycode.ENTER)

# Types out a whole line and then goes to next line
# keyboard_layout.write(line)

