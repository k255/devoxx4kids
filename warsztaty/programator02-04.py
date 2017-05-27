from microbit import *
import radio
radio.on()

moj_nr = '0'
cyfry = '0123456789'
a = 0
b = 0
i = 0

display.show(cyfry[0])

while True:
    if button_a.was_pressed() and pin2.is_touched():
        i = i - 1
        if i == -1:
            i = 9

    if button_a.was_pressed():
        i = i + 1
        if i == 10:
            i = 0
            
        display.show(cyfry[i])    

    if button_b.was_pressed():
        if a:
            b = cyfry[i]
            display.show(a+b)
            radio.send(moj_nr+a+b)
            a, b, i = 0, 0, 0

        else:
            a = cyfry[i]
            i = 0

        display.show(cyfry[0])            