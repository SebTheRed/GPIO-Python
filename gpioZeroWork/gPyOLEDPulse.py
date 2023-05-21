from gpiozero import PWMLED, AnalogInputDevice
from time import sleep

class ChallengeTwo:
    def __init__ (self):
        self.led = PWMLED(17, frequency=1000)
        self.pot = AnalogInputDevice(25, max_voltage=3.3)
        self.led.source = self.pot
    def ledStepPulse (self):
        while True:
            self.led.value = 0.1
            sleep(2)
            self.led.value = 0.2
            sleep(0.2)
            self.led.value = 0.3
            sleep(0.2)
            self.led.value = 0.4
            sleep(0.2)
            self.led.value = 0.5
            sleep(0.2)
            self.led.value = 0.6
            sleep(0.2)
            self.led.value = 0.7
            sleep(0.2)
            self.led.value = 0.8
            sleep(0.2)
            self.led.value = 0.9
            sleep(0.2)
            self.led.value = 1
            sleep(2)
            self.led.value = 0.9
            sleep(0.2)
            self.led.value = 0.8
            sleep(0.2)
            self.led.value = 0.7
            sleep(0.2)
            self.led.value = 0.6
            sleep(0.2)
            self.led.value = 0.5
            sleep(0.2)
            self.led.value = 0.4
            sleep(0.2)
            self.led.value = 0.3
            sleep(0.2)
            self.led.value = 0.2
            sleep(0.2)
    def ledPulse (self):
        while True:
            self.led.value = 1
            self.led.pulse()

initClass = ChallengeTwo()
initClass.ledStepPulse()


#Challenge #2
'''
Create a program that reads the value from a potentiometer connected to a Raspberry Pi GPIO pin,
and uses that value to control the brightness of an LED connected to a PWM pin.
The LED should be completely off when the potentiometer is turned all the way to the left,
and completely on when the potentiometer is turned all the way to the right.
You can use the AnalogInputDevice class to read the value of the potentiometer,
and the PWMLED class to control the brightness of the LED.

Hint: You can use the value property of the AnalogInputDevice object
to read the raw value of the potentiometer, and the scale() method to convert it
to a value between 0 and 1.
'''