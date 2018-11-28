#!/usr/bin/env python
import RPi.GPIO as GPIO
import time



def setup():
    global PIN_R, colorOptions, Red_Signal_Duty_Cycle, Red_Signal_Duty_Cycle, redColorOFFTime, PWM_R_Pin, setRedColor
    PIN_R = 11
    colorOptions = 256 # The number of colors available in an 8 bit number
    setRedColor = 256 # set the default color prior to getting user input

    # ------------------SET THE FREQUENCY and Duty Cycle -----------------------------------------------------
    Red_Signal_Frequency   = 2000 # The frequency of the digital signal
    Red_Signal_Duty_Cycle = 100 # set the default duty cycle prior to getting user input
    redColorOFFTime = 0 # set the default off time prior to getting user input

    #------------------SET PIN to OUTPUT -----------------------------------------------------
    GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
    GPIO.setup(PIN_R, GPIO.OUT) # Set the R pin to mode is output
    GPIO.output (PIN_R, GPIO.HIGH) # Turn off the LED
    PWM_R_Pin = GPIO.PWM(PIN_R, Red_Signal_Frequency)   # Set the pin to a pulse width modulation digital signal with a set frequency
    PWM_R_Pin.start(Red_Signal_Duty_Cycle) # Set the initial duty cycle

def setTheDutyCycle(): 
    global Red_Signal_Duty_Cycle
    global redColorOFFTime
    global PWM_R_Pin  
    #------------------SET THE DUTY CYCLE -----------------------------------------------------
    redColorOFFTime   = (setRedColor  / colorOptions) * 100 # Calculate the off time by dividing the setColor by 256. 
    Red_Signal_Duty_Cycle   = 100 - redColorOFFTime   # The duty cycle of the digital signal. This is the on-time
    PWM_R_Pin.ChangeDutyCycle(Red_Signal_Duty_Cycle)   # Start the pwm on the designated pin with a set duty cycle

def printInfo():
        print ("Set R to " + str(setRedColor)  + 
            ' With a duty cycle of ' + str(Red_Signal_Duty_Cycle)  + 
            ' OFF time ' + str(redColorOFFTime))
setup() # call the setup function
while True:
    
    try: # runs until Ctrl+C interupts
        setRedColor = int(input("What is the color value for red? (0 to 255) ")) 
        setTheDutyCycle() # call the Duty Cycle method
        printInfo() # call the print function
    except KeyboardInterrupt: # runs when Ctrl+C interupts
        break

print ("End of program")        
GPIO.cleanup() # this ensures a clean exit
