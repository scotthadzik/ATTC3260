#!/usr/bin/env python
import RPi.GPIO as GPIO

pullUPResistorPin = 11
PIN_R = 12


def setup():
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(pullUPResistorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(pullUPResistorPin, GPIO.BOTH, callback=buttonSense, bouncetime=500)

	GPIO.setup(PIN_R, GPIO.OUT)
	

def buttonSense(chn):
	print('*   Button Pressed   *')
	GPIO.output(PIN_R, GPIO.HIGH)  # Set the R pin to High(3.3V) to turn on led

setup()

while True:
	try:
		pass
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		pass
	finally:
		GPIO.cleanup()