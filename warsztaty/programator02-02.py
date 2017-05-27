from microbit import *

cyfry = '0123456789'
a = 0
b = 0
i = 0

display.show(cyfry[0])

while True:
    if button_a.was_pressed():
        i = i + 1
        if i == 10:
            i = 0
            
        display.show(cyfry[i])    

    if button_b.was_pressed():
        if a:
            b = cyfry[i]
            display.show(a+b)
            a, b, i = 0, 0, 0
        else:
            a = cyfry[i]
            i = 0

        display.show(cyfry[0])            