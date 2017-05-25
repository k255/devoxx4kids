import music
import radio
from microbit import display, Image, button_a

radio.on()
radio.config(length=251)

while True:
    if button_a.was_pressed():
        image_box = '00000:09090:00000:90009:09990:'
        radio.send(image_box)
        music_box = ';'.join(music.DADADADUM)
        radio.send(music_box)

    box = radio.receive()
    if box and ';' not in box:
        display.show(Image(box))
    elif box and ';' in box:
        music.play(box.split(';'))
