#!/usr/bin/env python
import RPi.GPIO as GPIO

pullDownResistorPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pullDownResistorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(pullDownResistorPin, GPIO.BOTH, callback=buttonPressedSense, bouncetime=500)

def pullDownSense(chn):
	print('*   Button Pressed   *')

setup()
while True:
	try:
		pass
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		break

GPIO.cleanup()                     # Release resource