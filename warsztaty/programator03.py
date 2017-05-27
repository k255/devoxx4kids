from microbit import *

obrazki = [Image.HEART, Image.HAPPY, Image.SAD]
i = 0

while True:

    if button_a.was_pressed():
        display.show(obrazki[i])    
        i = i + 1
        
    if button_b.was_pressed():
        display.show(obrazki[1])    

    if pin3.is_touched():
        display.show(obrazki[2])    
