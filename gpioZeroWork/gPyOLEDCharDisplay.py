from gpiozero import LEDMultiCharDisplay, LEDCharDisplay
import time

class ChallengeFive:
    def __init__ (self):
        self.display = LEDMultiCharDisplay(LEDCharDisplay(22, 23, 24, 25, 21, 20, 16, dp=12),18, 24, 23, 4)
        self.counter = 0
    def runCounter (self):
        while True:
            self.counter += 1
            self.display.text = str(self.counter)

inst = ChallengeFive()
inst.runCounter()
