from time import sleep
from gpiozero import LED, Servo, Buzzer

class CatFeeder:
    def __init__ (self):
        self.servoMotor = Servo(18)
        self.ledLight = LED(23)
        self.servoValue = 0
    def spinOnTenSeconds (self):
        while True:
            self.ledLight.on()
            self.servoMotor.value = self.servoValue
            sleep(1)
            self.servoMotor.detach()
            self.ledLight.off()
            if self.servoValue == 1:
                self.servoValue = 0
            else:
                self.servoValue += 0.1
            print(self.servoValue)
            sleep(10)
    def testFunc (self):
        while True:
            self.ledLight.on()
            self.servoMotor.min()
            print("min")
            sleep(0.5)
            self.ledLight.off()
            self.servoMotor.detach()
            sleep(2)
            self.ledLight.on()
            self.servoMotor.mid()
            print("mid")
            sleep(0.5)
            self.ledLight.off()
            self.servoMotor.detach()
            sleep(2)
            self.ledLight.on()
            self.servoMotor.max()
            print("max")
            sleep(0.5)
            self.ledLight.off()
            self.servoMotor.detach()
            sleep(2)
    def spinNinety (self):
        while True:
            self.ledLight.on()
            self.servoMotor.value = 0.09
            sleep(0.02)
            self.servoMotor.detach()
            self.ledLight.off()
            sleep(5)

newCatFeeder = CatFeeder()
newCatFeeder.spinNinety()