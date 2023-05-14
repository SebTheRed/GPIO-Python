from time import sleep
import traceback
import MPU6050
from gpiozero import LEDMultiCharDisplay, LEDCharDisplay

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

class SpeedOmeter:
    def __init__ (self):
        self.speed = [0]*3
        self.gyro = [0]*3
        self.mpu = MPU6050.MPU6050()     # instantiate a MPU6050 class object
        self.display = LEDMultiCharDisplay(LEDCharDisplay(11, 7, 4, 2, 1, 10, 5, dp=3), 22, 27, 17, 18)
    def printStats (self):
        print("Started")
        self.display.source_delay = 0.2
        self.mpu.dmp_initialize()    # initialize MPU6050
        while True:
            self.speed = self.mpu.get_acceleration()      # get accelerometer data
            self.gyro = self.mpu.get_rotation()           # get gyroscope data
            print(f"{RED}SPEED - X: {self.speed[0]} | Y: {self.speed[1]} | Z: {self.speed[2]}")
            print(f"{GREEN}GYROS - X: {self.gyro[0]} | Y: {self.gyro[1]} | Z: {self.speed[2]}{RESET}")
            self.display.source = self.speed[0]
            sleep(0.5)
    def ledTest (self):
        print("Test beginning..")
        while True:
            self.display.source_delay = 0.2
            self.display.value = "8888"

SterlingSpeed = SpeedOmeter()
print("Starting...")
sleep(2)
SterlingSpeed.printStats()


'''
MAPPING:
12: GPIO 22
11: GPIO 5
10: GPIO 6
9: GPIO 27
8: GPIO 17
7: GPIO 13
6: GPIO 18
5: GPIO 19
4: GPIO 26
3: GPIO 16
2: GPIO 20
1: GPIO 21
'''