#!/usr/bin/env python
import RPi.GPIO as GPIO

button = 11
PIN_R = 12
LED_ON = False


def setup():
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(button, GPIO.BOTH, callback=buttonSense, bouncetime=300)

	GPIO.setup(PIN_R, GPIO.OUT)
	GPIO.output(PIN_R, GPIO.LOW)
	
def LED(state):
	global LED_ON
	if LED_ON == False: #	The LED is off
		print('*   Turn LED ON   *')
		GPIO.output(PIN_R, GPIO.HIGH) # Turn on LED
		LED_ON = True
	else: 	#	The button has been released LED_ON == True
		print('*   Turn LED OFF   *')
		GPIO.output(PIN_R, GPIO.LOW) # Turn off LED
		LED_ON = False

def buttonSense(channel):
	print('*   Button Pressed   *')
	LED(GPIO.input(button))

def checkButtonState(buttonState):
	print('The state of the button is ' + str(buttonState))

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
		