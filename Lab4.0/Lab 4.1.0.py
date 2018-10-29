#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

PIN_R = 12

Signal_Frequency = 2000 # The frequency of the digital signal
Signal_Duty_Cycle = 50 # The duty cycle of the digital signal. This is the on-time

GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
GPIO.setup(PIN_R, GPIO.OUT) # Set the R pin to mode is output

GPIO.output (PIN_R, GPIO.HIGH) # Turn off the LED

PWM_R_Pin = GPIO.PWM(PIN_R, Signal_Frequency) # Set the pin to a pulse width modulation digital signal with a set frequency

while True:
    PWM_R_Pin.start(Signal_Duty_Cycle)    # Start the pwm on the designated pin with a set duty cycle
	
print ("End of program")

GPIO.cleanup() # this ensures a clean exit