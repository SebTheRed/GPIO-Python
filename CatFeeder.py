from time import sleep
from gpiozero import LED, Servo, Buzzer

class CatFeeder:
    def __init__ (self):
        self.servoMotor = Servo(18)
        self.ledLight = LED(23)
        self.buzzerSpeaker = Buzzer(17)
        self.servoValue = -1
    def spinOnTenSeconds (self):
        while True:
            self.ledLight.on()
            self.servoMotor.value = self.servoValue
            sleep(1)
            self.servoMotor.detach()
            self.ledLight.off()
            if self.servoValue == 1:
                self.servoValue = -1
            else:
                self.servoValue += 1
            print(self.servoValue)
            sleep(10)
    def testFunc (self):
        while True:
            self.ledLight.on()
            self.servoMotor.min()
            self.buzzerSpeaker.on()
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

newCatFeeder = CatFeeder()
newCatFeeder.testFunc()