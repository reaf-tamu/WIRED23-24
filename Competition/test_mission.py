import time
import Jetson.GPIO as GPIO

# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)
# Specify the GPIO pin number you want to read from
pin_number = 18
# Set up the GPIO pin as an input
GPIO.setup(pin_number, GPIO.IN)

status = 0
while status == 0:
	status = GPIO.input(pin_number)
	print(status)
	time.sleep(1)


from vnpy import *

# set up vector nav
s = VnSensor()
s.connect("/dev/ttyUSB0",115200)


# record initial orientation
orientation = s.read_yaw_pitch_roll()
origin = orientation.x
print(origin)

while True:
	print("going")
	time.sleep(1)
