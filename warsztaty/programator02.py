from microbit import *

obrazki = [Image.HEART, Image.HAPPY, Image.SAD]

while True:

    if button_a.was_pressed():
        display.show(obrazki[0])    

    if button_b.was_pressed():
        display.show(obrazki[1])    

    if pin2.is_touched():
        display.show(obrazki[2])    
