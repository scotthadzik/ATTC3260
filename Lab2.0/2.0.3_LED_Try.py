#!/usr/bin/env python
import RPi.GPIO as GPIO

LED_PIN_R = 12

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LED_PIN_R, GPIO.OUT)   # Set the R pin to mode is output


try:
    while True:
        GPIO.output(LED_PIN_R, GPIO.HIGH)  # Set the R pin to High(3.3V) to turn on led
except KeyboardInterrupt:
    GPIO.cleanup() #clean up the GPIO when exiting