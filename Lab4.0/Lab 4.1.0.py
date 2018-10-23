#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]
PIN_R = 12

Signal_Frequency = 2000 # The frequency of the digital signal
Signal_Duty_Cycle = 75 # The duty cycle of the digital signal. This is the on-time

GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
GPIO.setup(PIN_R, GPIO.OUT, initial=GPIO.LOW) # Set the R pin to mode is output

PWM_R_Pin = GPIO.PWM(PIN_R, Signal_Frequency) # Set the pin to a pulse width modulation digital signal with a set frequency


while True:
    PWM_R_Pin.start(Signal_Duty_Cycle)    # Start the pwm on the designated pin with a set duty cycle

print ("End of program")

GPIO.cleanup() # this ensures a clean exit



# def setup(Rpin, Gpin, Bpin):
# 	global pins
# 	global p_R, p_G, p_B
# 	pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}
# 	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
# 	for i in pins:
# 		GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
# 		GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led
	
# 	p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
# 	p_G = GPIO.PWM(pins['pin_G'], 1999)
# 	p_B = GPIO.PWM(pins['pin_B'], 5000)
	
# 	p_R.start(100)      # Initial duty Cycle = 0(leds off)
# 	p_G.start(100)
# 	p_B.start(100)

# def map(x, in_min, in_max, out_min, out_max):
# 	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# def off():
# 	for i in pins:
# 		GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds

# def setColor(col):   # For example : col = 0x112233
# 	R_val = (col & 0xff0000) >> 16
# 	G_val = (col & 0x00ff00) >> 8
# 	B_val = (col & 0x0000ff) >> 0

# 	R_val = map(R_val, 0, 255, 0, 100)
# 	G_val = map(G_val, 0, 255, 0, 100)
# 	B_val = map(B_val, 0, 255, 0, 100)
	
# 	p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
# 	p_G.ChangeDutyCycle(100-G_val)
# 	p_B.ChangeDutyCycle(100-B_val)

# def loop():
# 	while True:
# 		for col in colors:
# 			setColor(col)
# 			time.sleep(1)

# def destroy():
# 	p_R.stop()
# 	p_G.stop()
# 	p_B.stop()
# 	off()
# 	GPIO.cleanup()

# if __name__ == "__main__":
# 	try:
# 		setup(R, G, B)
# 		loop()
# 	except KeyboardInterrupt:
# 		destroy()
