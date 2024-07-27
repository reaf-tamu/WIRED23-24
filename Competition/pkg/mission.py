import time
import Jetson.GPIO as GPIO

def setup():
	# Set the GPIO pin numbering mode
	GPIO.setmode(GPIO.BOARD)
	# Specify the GPIO pin number you want to read from
	pin_number = 18
	# Set up the GPIO pin as an input
	GPIO.setup(pin_number, GPIO.IN)

def start():
	input_status = GPIO.input(pin_number)
	
	return input_status
