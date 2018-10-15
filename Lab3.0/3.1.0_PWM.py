#!/usr/bin/env python
import RPi.GPIO as GPIO
import time # import the library time

PIN_R = 12
Signal_Frequency = 1 # The frequency of the digital signal
Signal_Duty_Cycle = 50 # The duty cycle of the digital signal. This is the on-time


GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
GPIO.setup(PIN_R, GPIO.OUT) # Set the R pin to mode is output
PWM_Pin = GPIO.PWM(PIN_R, Signal_Frequency) # Set the pin to a pulse width modulation digital signal with a set frequency



print ("Start of the program")
print ("The duty cycle is ", Signal_Duty_Cycle) # Print out the current Duty Cycle
print ("The frequency is ", Signal_Frequency) # Print out the current Frequency 
print ("The LED ")

while True:
    PWM_Pin.Start(Signal_Duty_Cycle)    # Start the pwm on the designated pin with a set duty cycle
    
print ("End of program")

GPIO.cleanup() # this ensures a clean exit
