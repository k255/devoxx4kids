from microbit import *

while True:

    if button_a.was_pressed():
        display.show(Image.HEART)    

    if button_b.was_pressed():
        display.show(Image.HAPPY)    

    if pin2.was_touched():
        display.show(Image.SAD)    
