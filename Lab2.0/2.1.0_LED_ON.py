#!/usr/bin/env python
import RPi.GPIO as GPIO

PIN_R = 12

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical pin location
GPIO.setup(PIN_R, GPIO.OUT)   # Set the physical pin 12 to mode is output

GPIO.output(PIN_R, GPIO.HIGH)  # Set the R pin to High(3.3V) to turn on led
