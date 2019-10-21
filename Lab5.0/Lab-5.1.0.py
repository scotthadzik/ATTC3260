#!/usr/bin/env python
import RPi.GPIO as GPIO

pullUpResistorPin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pullUpResistorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(pullUpResistorPin, GPIO.FALLING, callback=pullUpSense, bouncetime=500)

def pullUpSense(chn):
	print('*   Button Pressed   *')

setup()
while True:
	try:
		pass
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		break

GPIO.cleanup()                     # Release resource