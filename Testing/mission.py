import time
import Jetson.GPIO as GPIO

# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)
# Specify the GPIO pin number you want to read from
pin_number = 18
# Set up the GPIO pin as an input
GPIO.setup(pin_number, GPIO.IN)

print("Starting to monitor GPIO pin status")
while True:
    status = GPIO.input(pin_number)
    print(f"Pin {pin_number} status: {status}")
    time.sleep(1)

