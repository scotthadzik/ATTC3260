#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

PIN_R = 11
colorOptions = 256 # The number of colors available in an 8 bit number
# ------------------SET THE FREQUENCY -----------------------------------------------------
Red_Signal_Frequency   = 2000 # The frequency of the digital signal

#Set the color value
setRedColor = int(input("What is the color value for red? (0 to 255) "))

#------------------SET THE DUTY CYCLE -----------------------------------------------------
redColorOFFTime   = (setRedColor  / colorOptions) * 100 # Calculate the off time by dividing the setColor by 256. 
Red_Signal_Duty_Cycle   = 100 - redColorOFFTime   # The duty cycle of the digital signal. This is the on-time

#------------------SET PIN to OUTPUT -----------------------------------------------------
GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
GPIO.setup(PIN_R, GPIO.OUT) # Set the R pin to mode is output
GPIO.output (PIN_R, GPIO.HIGH) # Turn off the LED

PWM_R_Pin = GPIO.PWM(PIN_R, Red_Signal_Frequency)   # Set the pin to a pulse width modulation digital signal with a set frequency

print ("Set R to " + str(setRedColor)  + 
        ' With a duty cycle of ' + str(Red_Signal_Duty_Cycle)  + 
        ' OFF time ' + str(redColorOFFTime))

while True:
    try: # runs until Ctrl+C interupts
        PWM_R_Pin.start(Red_Signal_Duty_Cycle)   # Start the pwm on the designated pin with a set duty cycle
    except KeyboardInterrupt: # runs when Ctrl+C interupts
        break

print ("End of program")        
GPIO.cleanup() # this ensures a clean exit
