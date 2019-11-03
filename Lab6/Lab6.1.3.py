#!/usr/bin/env python
import RPi.GPIO as GPIO

pullUPResistorPin = 11
PIN_R = 12


def setup():
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(pullUPResistorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(pullUPResistorPin, GPIO.BOTH, callback=buttonSense, bouncetime=500)

	GPIO.setup(PIN_R, GPIO.OUT)
	GPIO.output(PIN_R, GPIO.LOW)

def LED (state):
    if state == 0:                  # if the state is low
        GPIO.output(PIN_R, GPIO.LOW)         # turn off LED
    if state == 1:                  #if the sate is high
        GPIO.output(PIN_R, GPIO.HIGH)        #Turn on LED

def buttonSense(chn):
	print('*   Button Pressed   *')
	GPIO.output(PIN_R, GPIO.HIGH)  # Set the R pin to High(3.3V) to turn on led

def loop():
	while True:
		pass

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
		