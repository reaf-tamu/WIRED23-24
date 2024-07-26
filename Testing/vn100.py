from vnpy import *
import time

s = VnSensor()
s.connect("/dev/ttyUSB0",115200)

"""
def sign(num):
	if num < 0:
		pos = 360 + num
	else:
		pos = num
	return pos
	

def direction(head, x):
	if x > (head + 10):
		if (x - (head + 10)) < 180:
			print("right")
		else:
			print("left")
	elif x < (head - 10):
		if ((head - 10) - x) > 180:
			print("left")
		else:
			print("right")
	else:
		print("forward")
		"""
		
def direction(head, x):
	if head < 0:
		x -= head
	else: 
		x += head
	
	
	if x < -10:
		print("right")
	elif x > 10:
		print("left")
	else:
		print("centered")

orientation = s.read_yaw_pitch_roll()
origin = orientation.x
print("origin =", origin)

if origin > 0:
	back = origin - 180
else:
	back = origin + 180
print("back = ", back)

a = 0
while True:
	# reads the sensors
	orientation = s.read_yaw_pitch_roll()
	x = orientation.x
	print(x)
	
	direction(origin,x)
	
	a += 1
	time.sleep(1)

"""
a = 0
while a < 10:
	# reads the sensors
	orientation = s.read_yaw_pitch_roll()
	x = sign(orientation.x)
	print(x)
	
	direction(back,x)
	
	a += 1
	time.sleep(1)
	"""
