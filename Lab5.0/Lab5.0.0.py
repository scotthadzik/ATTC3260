#!/usr/bin/env python
import RPi.GPIO as GPIO

inputPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(inputPin, GPIO.IN)

setup()
while True:
	try:
		print (GPIO.input(inputPin))
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		break

GPIO.cleanup()                     # Release resource


