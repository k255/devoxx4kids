from microbit import *
import radio
import music
radio.on()
display.show(Image.HEART_SMALL)
while True:

    if button_a.was_pressed():
        print('sending')
        radio.send("G2:4")

    note = radio.receive()
    if note:
        display.show(Image.SURPRISED)
        music.play(note)

        display.show(Image.HEART)
