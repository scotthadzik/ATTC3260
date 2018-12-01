#!/usr/bin/env python
import RPi.GPIO as GPIO

ButtonInputPin = 7

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(ButtonInputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(ButtonInputPin, GPIO.BOTH, callback=detect, bouncetime=200)

def detect(chn):
	print('*   Button Pressed!   *')

setup()
while True:
	try:
		pass
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

GPIO.cleanup()                     # Release resource
