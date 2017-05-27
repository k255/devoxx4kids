from microbit import *

obrazki = [Image.HEART, Image.HAPPY, Image.SAD]
i = 0

while True:

    if button_a.was_pressed():
        display.show(obrazki[i])    
        i = i + 1
        if i == 3:
            i = 0
