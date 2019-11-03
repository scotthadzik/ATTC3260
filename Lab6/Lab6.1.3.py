#!/usr/bin/env python
import RPi.GPIO as GPIO

button = 11
PIN_R = 12
channelState = 0


def setup():
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(button, GPIO.BOTH, callback=buttonSense, bouncetime=500)

	GPIO.setup(PIN_R, GPIO.OUT)
	GPIO.output(PIN_R, GPIO.LOW)
    checkButtonState()
	

def buttonSense(channel):
	print('*   Button Pressed   *')
    print('The channel is:  ' + str(channel))
    checkButtonState()
	GPIO.output(PIN_R, GPIO.HIGH)  # Set the R pin to High(3.3V) to turn on led

def checkButtonState():
    print('The state of the button is ' + str(GPIO.input(button))

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
		