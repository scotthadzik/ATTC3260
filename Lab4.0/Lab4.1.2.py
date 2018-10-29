#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

PIN_R = 11
PIN_G = 12
PIN_B = 13

GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location

colorOptions = 256 # The number of colors available in an 8 bit number
redColorDefault   = colorOptions
blueColorDefault  = colorOptions
greenColorDefault = colorOptions

setRedColor   = 73 
setGreenColor = 35
setBlueColor  = 101

redColorOFFTime   = (setRedColor  / redColorDefault)   *100
greenColorOFFTime = (setGreenColor/ greenColorDefault) *100
blueColorOFFTime  = (setBlueColor / blueColorDefault)  *100

#------------------SET THE DUTY CYCLE -----------------------------------------------------
Red_Signal_Duty_Cycle   = 100 - redColorOFFTime   # The duty cycle of the digital signal. This is the on-time
Green_Signal_Duty_Cycle = 100 - greenColorOFFTime # The duty cycle of the digital signal. This is the on-time
Blue_Signal_Duty_Cycle  = 100 - blueColorOFFTime  # The duty cycle of the digital signal. This is the on-time

#------------------SET PIN to OUTPUT -----------------------------------------------------
GPIO.setup(PIN_R, GPIO.OUT) # Set the R pin to mode is output
GPIO.setup(PIN_G, GPIO.OUT) # Set the G pin to mode is output
GPIO.setup(PIN_B, GPIO.OUT) # Set the B pin to mode is output

#------------------Turn pin HIGH so that LED is off -----------------------------------------------------
# GPIO.output (PIN_R, GPIO.HIGH) # Turn off the LED
# GPIO.output (PIN_G, GPIO.HIGH) # Turn off the LED
# GPIO.output (PIN_B, GPIO.HIGH) # Turn off the LED

# ------------------SET THE FREQUENCY -----------------------------------------------------
Red_Signal_Frequency   = 2000 # The frequency of the digital signal
Green_Signal_Frequency = 2000 # The frequency of the digital signal
Blue_Signal_Frequency  = 2000 # The frequency of the digital signal

PWM_R_Pin = GPIO.PWM(PIN_R, Red_Signal_Frequency)   # Set the pin to a pulse width modulation digital signal with a set frequency
PWM_G_Pin = GPIO.PWM(PIN_G, Green_Signal_Frequency) # Set the pin to a pulse width modulation digital signal with a set frequency
PWM_B_Pin = GPIO.PWM(PIN_B, Blue_Signal_Frequency)  # Set the pin to a pulse width modulation digital signal with a set frequency

print ("Set R to " + str(setRedColor)  + ' With a duty cyle of ' + str(Red_Signal_Duty_Cycle)  + ' OFF time ' + str(redColorOFFTime))
print ("Set G to " + str(setGreenColor)+ ' With a duty cyle of ' + str(Green_Signal_Duty_Cycle)+ ' OFF time' + str(greenColorOFFTime ))
print ("Set B to " + str(setBlueColor) + ' With a duty cyle of ' + str(Blue_Signal_Duty_Cycle) + ' OFF time' + str(blueColorOFFTime ))

while True:
    try: # runs until Ctrl+C interupts
        PWM_R_Pin.start(29)   # Start the pwm on the designated pin with a set duty cycle
        PWM_G_Pin.start(Green_Signal_Duty_Cycle)  # Start the pwm on the designated pin with a set duty cycle
        PWM_B_Pin.start(Blue_Signal_Duty_Cycle) # Start the pwm on the designated pin with a set duty cycle

    except KeyboardInterrupt: # runs when Ctrl+C interupts
        break

print ("End of program")        
GPIO.cleanup() # this ensures a clean exit
