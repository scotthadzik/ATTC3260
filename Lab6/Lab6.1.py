#!/usr/bin/env python
import RPi.GPIO as GPIO

pullUPResistorPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pullUPResistorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(pullUPResistorPin, GPIO.BOTH, callback=buttonSense, bouncetime=500)

def buttonSense(chn):
	print('*   Button Pressed   *')

setup()
while True:
	try:
		pass
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		break

GPIO.cleanup()                     # Release resource