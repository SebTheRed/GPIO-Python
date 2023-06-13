from machine import Pin, PWM
import utime as time


class CatAuger:
    def __init__ (self):
        # self.led_pin = Pin(14, Pin.OUT)
        self.servo = PWM(Pin(15))
        self.servo.freq(50)
        self.forwardValue = 8000
        self.stopValue = 0
        self.backwardValue = 2461
    def configServo (self):
        print("in-progress")
    # def blinkTest (self):
    #     while True:
    #       self.led_pin.value(1)
    #       print("hi")
    #       time.sleep(3)
    #       self.led_pin.value(0)
    #       time.sleep(10)
    def spinTest (self):
        print("spin test!")
        stop_value = 5000
        duty_0 = 2461
        duty_180 = 8000
        self.servo.duty_u16(duty_0)
        time.sleep(2)
        print("halfway point?")
        self.servo.duty_u16(stop_value)
        time.sleep(2)
        print("duty switched")
        self.servo.duty_u16(duty_180)
        time.sleep(2)
        print("duty set to 0")
        self.servo.duty_u16(0)
    def dispenseFood(self):
        print("Food Dispensing!")
        self.servo.duty_u16(self.forwardValue)
        time.sleep(4)
        print("halfway point?")
        self.servo.duty_u16(self.stopValue)
        time.sleep(1)
        print("duty switched")
        self.servo.duty_u16(self.backwardValue)
        time.sleep(1)
        print("duty set to 0")
        self.servo.duty_u16(0)

augerInst = CatAuger()
augerInst.dispenseFood()
