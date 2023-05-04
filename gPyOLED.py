from gpiozero import LED, Button
from time import sleep

class ChallengeOne:
    def __init__ (self):
        self.activeLED = LED(17)
        self.activeBUTTON = Button(18)
        self.isButtonActive = False
    def buttonPress (self):
        print("button is: " + str(self.isButtonActive))
        if self.isButtonActive == False:
            self.isButtonActive = True
        elif self.isButtonActive == True:
            self.isButtonActive = False
    def buttonBlink (self):
        print("on")
        while True:
            self.activeBUTTON.when_pressed = self.buttonPress
            while self.isButtonActive == True:
                print("on")
                # self.activeBUTTON.when_pressed = self.buttonPress()
                self.activeLED.on()
                sleep(0.2)
                self.activeLED.off()
                sleep(0.2)
            while self.isButtonActive == False:
                print("off")
                # self.activeBUTTON.when_pressed = self.buttonPress()
                self.activeLED.on()
                sleep(1)
                self.activeLED.off()
                sleep(1)
    
classInst = ChallengeOne()
while True:
    classInst.buttonBlink()
    

#Description for the blink method:
#The first parameter is the on duration. (0.1 seconds on.)
#The second parameter is the off duration. (0.5 seconds off.)
#The third parameter is the amount of times the blinks occur (10 blinks)
#The True parameter indicates that this method should NOT loop indefinitely.

#Challenge #1
'''
Create a program that uses a button to control the blinking of an LED.
The LED should blink at a frequency of 1 Hz when the button is not pressed,
and at a frequency of 5 Hz when the button is pressed.
You can use the sleep() function from the time module to control the blinking frequency.
'''