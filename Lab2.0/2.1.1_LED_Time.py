#!/usr/bin/env python
import RPi.GPIO as GPIO
import time                    # import the library time

PIN_R = 12

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(PIN_R, GPIO.OUT)   # Set the R pin to mode is output

time.sleep(3)        # wait for 3 seconds
GPIO.output(PIN_R, GPIO.HIGH)  # Set the R pin to High(3.3V) to turn on led
time.sleep(3)        # wait for 3 seconds
GPIO.output(PIN_R, GPIO.LOW)  # Set the R pin to Low(0V) to turn off led

GPIO.cleanup()  # this ensures a clean exit