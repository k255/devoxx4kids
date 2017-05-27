from microbit import *

cyfry = '0123456789'
i = 0

display.show(cyfry[0])

while True:
    if button_a.was_pressed():
        i = i + 1
        if i == 10:
            i = 0
            
        display.show(cyfry[i])