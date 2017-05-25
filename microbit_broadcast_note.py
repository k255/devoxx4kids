import music
import radio
from microbit import button_a

radio.on()

while True:
    if button_a.was_pressed():
        radio.send("C4:4")

    note = radio.receive()
    if note:
        music.play([note])
