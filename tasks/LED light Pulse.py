import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
a = 1
i = 0
while True:
    while i < 1:
        a = a * 1.02

        if a > 2:
            i = 2
            led.value = False
        else:
            led.value = True
            time.sleep(0.01 ** a)
            led.value = False
            time.sleep(0.01 - 0.01 ** a)
    while i > 1:
        a = a / 1.02

        if a < 1:
            i = 0
            led.value = True
            time.sleep(0.01)
        else:
            led.value = True
            time.sleep(0.01 ** a)
            led.value = False
            time.sleep(0.01 - 0.01 ** a)
