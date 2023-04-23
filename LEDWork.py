from gpiozero import LED, Button
from time import sleep

blueButton = Button("GPIO21")
yellowButton = Button("GPIO6")
greenButton = Button("GPIO5")
redButton = Button("GPIO16")

class LEDOps:
	def __init__(self):
		self.yellowLED = LED("GPIO19")
		self.greenLED = LED("GPIO13")
		self.redLED = LED("GPIO20")
		self.blueLED = LED("GPIO26")
	def lightShow(self):
		print("Welcome to the light show!")
		while True:
			self.redLED.off()
			self.greenLED.on()
			sleep(0.1)
			self.greenLED.off()
			self.yellowLED.on()
			sleep(0.1)
			self.yellowLED.off()
			self.blueLED.on()
			sleep(0.1)
			self.blueLED.off()
			self.redLED.on()
			sleep(0.1)
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
	def blueBtnDown (self):
		self.blueLED.on()
	def blueBtnUp (self):
		self.blueLED.off()
	def yellowBtnDown (self):
		self.yellowLED.on()
	def yellowBtnUp (self):
		self.yellowLED.off()
	def greenBtnDown (self):
		self.greenLED.on()
	def greenBtnUp (self):
		self.greenLED.off()
	def redBtnDown (self):
		self.redLED.on()
	def redBtnUp (self):
		self.redLED.off()
    
		

instanceLEDOps = LEDOps()
methodOption = int(input("Please choose which method you would like to run:\n1. Light Show\n2. Blink\n3. Buttons\n"))
if methodOption == 1:
	instanceLEDOps.lightShow()
elif methodOption == 2:
	blinkInput = int(input("Please enter which LED you would like to see blink.\n1. Yellow\n2. Green\n3. Blue\n4. Red\n"))
	instanceLEDOps.chooseALight(blinkInput)
elif methodOption == 3:
  while True:
    blueButton.when_pressed = instanceLEDOps.blueBtnDown
    blueButton.when_released = instanceLEDOps.blueBtnUp

    yellowButton.when_pressed = instanceLEDOps.yellowBtnDown
    yellowButton.when_released = instanceLEDOps.yellowBtnUp

    greenButton.when_pressed = instanceLEDOps.greenBtnDown
    greenButton.when_released = instanceLEDOps.greenBtnUp

    redButton.when_pressed = instanceLEDOps.redBtnDown
    redButton.when_released = instanceLEDOps.redBtnUp
