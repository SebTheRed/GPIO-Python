from gpiozero import LED, Button
from time import sleep

redButton = Button("GPIO18")

class LEDOps:
	def __init__(self):
		self.yellowLED = LED("GPIO19")
		self.greenLED = LED("GPIO16")
		self.redLED = LED("GPIO21")
		self.blueLED = LED("GPIO13")
	def lightShow(self):
		print("Welcome to the light show!")
		while True:
			self.redLED.off()
			self.yellowLED.on()
			sleep(0.5)
			self.yellowLED.off()
			self.greenLED.on()
			sleep(0.5)
			self.greenLED.off()
			self.blueLED.on()
			sleep(0.5)
			self.blueLED.off()
			self.redLED.on()
			sleep(0.5)
	def chooseALight(self, inputVal):
		chosenLED = ""
		if inputVal == 1:
			chosenLED = self.yellowLED
			print("Yellow it is!")
		elif inputVal == 2:
			chosenLED = self.greenLED
			print("Green it is!")
		elif inputVal == 3:
			chosenLED = self.blueLED
			print("Blue it is!")
		elif inputVal == 4:
			chosenLED = self.redLED
			print("Green it is!")
		else:
			chosenLED = self.yellowLED
			print("You didn't follow the instructions, but here's Yellow anyway.")
		while True:
			chosenLED.on()
			sleep(1)
			chosenLED.off()
			sleep(1)
	def buttonDown (self):
		self.redLED.on()
	def buttonUp (self):
		self.redLED.off()
		

instanceLEDOps = LEDOps()
methodOption = int(input("Please choose which method you would like to run:\n1. Light Show\n2. Blink\n3. Button\n"))
if methodOption == 1:
	instanceLEDOps.lightShow()
elif methodOption == 2:
	blinkInput = int(input("Please enter which LED you would like to see blink.\n1. Yellow\n2. Green\n3. Blue\n4. Red\n"))
	instanceLEDOps.chooseALight(blinkInput)
elif methodOption == 3:
  redButton.when_pressed = instanceLEDOps.buttonDown()
  redButton.when_released = instanceLEDOps.buttonUp()

