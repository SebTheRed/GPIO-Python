from gpiozero import LED
from time import sleep

activeLED = LED(17)

while True:
    activeLED.on()