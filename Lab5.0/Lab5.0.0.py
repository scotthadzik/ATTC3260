#!/usr/bin/env python
import RPi.GPIO as GPIO

pullUpResistorPin = 11
pullDownResistorPin = 13

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pullUpResistorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(pullDownResistorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(pullUpResistorPin, GPIO.BOTH, callback=pullUpSense, bouncetime=200)
	GPIO.add_event_detect(pullDownResistorPin, GPIO.BOTH, callback=pullDownSense, bouncetime=200)

def pullUpSense(chn):
	print('*   Pull UP Sense   *')

def pullDownSense(chn):
	print('*   Pull DOWN Sense   *')

setup()
while True:
	try:
		pass
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		break

GPIO.cleanup()                     # Release resource


