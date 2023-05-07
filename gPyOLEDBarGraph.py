from gpiozero import LEDBarGraph
from ADCDevice import *
import time

class ChallengeThree:
    def __init__ (self):
        self.adc = ADCDevice()
        self.ledBar = LEDBarGraph(17, 27, 18, 23, 24, 25, 12, 16, 20, 21)
        self.ledBar.value = 1
        if(self.adc.detectI2C(0x4b)): # Detect the ads7830
                self.adc = ADS7830()
    def adjustBarGraph (self):
        while True:
            analogVal = self.adc.analogRead(0)    # read the ADC value of channel 0
            # voltage = value / 255.0 * 3.3  # calculate the voltage value
            # print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
            scaledVal = analogVal / 256
            if scaledVal > 0.95:
                 scaledVal = 1
            self.ledBar.value = scaledVal
            print(scaledVal)
            time.sleep(0.1)
            

inst = ChallengeThree()
inst.adjustBarGraph()

#Challenge 3
'''
Create an LEDBarGraph with 10 LEDs connected to pins.
and control it using a potentiometer connected to pin 2.
The brightness of the LEDBarGraph should change as you turn the potentiometer.
'''