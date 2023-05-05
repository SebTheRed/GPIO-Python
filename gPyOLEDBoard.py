from gpiozero import LEDBoard
from time import sleep

class ChallengeThree:
    def __init__ (self):
        self.boardOLeds = LEDBoard(27, 6, 13, 19, 26, pwm=False)
    def lightShow (self):
        while True:
            for light in self.boardOLeds:
                light.on()
                sleep(0.3)
                light.off()
                sleep(0.1)

classInst = ChallengeThree()
classInst.lightShow()

# Challenge #3
'''
Challenge: Create a LEDBoard with 5 LEDs connected to pins 20, 21, 22, 23, and 24 respectively,
and control them using a for loop to make them blink in sequence.
'''