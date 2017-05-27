from microbit import *
from neopixel import NeoPixel
import radio
import random
from math import floor

np = NeoPixel(pin0, 60)
locked = (100, 0, 0)
hit = (0, 100, 0)
small = (60, 0, 60)
medium = (100, 50, 0)
large = (0, 60, 60)
codes = []


# def check_number_d(bank, number):
#     diff = abs(codes[bank] - number)

#     if diff == 0:
#         return hit
#     elif diff > 50:
#         return large
#     elif diff > 10:
#         return medium
#     else:
#         return small


def check_number(bank, number):
    diff = abs(codes[bank] - number)

    if number == codes[bank]:
        return (0, hit)
    elif number > codes[bank]:
        return (1, modcolor(diff, large))
    else:
        return (-1, modcolor(diff, small))


def modcolor(diff, color):
    r, g, b = color
    c = (max(1,floor(r - (r / 60 * diff))),max(1,floor(g - (g / 60 * diff))),max(1,floor(b - (b / 60 * diff))))
    print(c)
    return c


def lightup(bank, color):
    bankpixels = range(bank * 10, bank * 10 + 10)
    for p in bankpixels:
        np[p] = color
    np.show()


def process(msg):
    if msg:
        bank = int(msg[0])
        number = int(msg[1:3])
        state, color = check_number(bank, number)
        lightup(bank, color)

        if color != hit and state > 0:
            sleep(1000)
            lightup(bank, locked)
            radio.send("0")
        elif color != hit and state < 0:
            for i in range(0, 3):
                lightup(bank, color)
                sleep(250)
                lightup(bank, (0,0,0))
                sleep(250)
	    lightup(bank, locked)
            radio.send("0")
        else:
            radio.send("1")
        display.show(Image.HAPPY)


# Main

for n in range(0, 6):
    codes.append(random.randrange(0, 100))

print(codes)
for p in range(0, len(np)):
    np[p] = locked
    sleep(50)
    np.show()

radio.on()
display.show(Image.PACMAN)

while True:
    incoming = radio.receive()
    process(incoming)
