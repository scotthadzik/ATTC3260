#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

inputPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

setup()
while True:
	try:
		pinState = GPIO.input(inputPin)
		if pinState == True:
			print('The pin is high')
		elif pinState == False:
			print('The pin is low')
		time.sleep(5)
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		break

GPIO.cleanup()                     # Release resource
