from gpiozero import PWMLED
from ADCDevice import *
import time

class PotentioClass:
    def __init__ (self):
        self.adc = ADCDevice()
    def onRunFunc (self):
        if(self.adc.detectI2C(0x4b)): # Detect the ads7830
                self.adc = ADS7830()
                print("match")
    def potentioLoop (self):
        while True:
            value = self.adc.analogRead(0)    # read the ADC value of channel 0
            voltage = value / 255.0 * 3.3  # calculate the voltage value
            print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
            time.sleep(0.1)

classInst = PotentioClass()
classInst.onRunFunc()
classInst.potentioLoop()