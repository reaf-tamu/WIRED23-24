# import functions
from pkg import pinger, thrusters, vn, mission
from adafruit_servokit import ServoKit


# imports
import cv2
import time
import numpy as np
from vnpy import *

def thruster_setup():
	# initiate thrusters
	kit = ServoKit(channels = 16)

	def set_speed(speed, motor):
		kit.servo[motor].angle = speed
		return

	class Motor:
		def __init__(self, name):
			self.name = name
			self.speed = 90
			self.prev_speed = self.speed
		def setSpeed(self, speed):
			self.speed = speed

		def run(self):
			if self.prev_speed != self.speed:
				# print("boop")
				kit.servo[self.name].angle = self.speed
				self.prev_speed = self.speed
			else:
				return
		def stop(self):
			kit.servo[name] = 90

	# set thrusters as global variables
	global A1, A2, A3, A4, M1, M2, M3, M4	
	global A2
	
	# set thruster pins
	A1 = Motor(0)
	A2 = Motor(1)
	A3 = Motor(3)
	A4 = Motor(2)
	M1 = Motor(4)
	M2 = Motor(5)
	M3 = Motor(7)
	M4 = Motor(6)

#time.sleep(30)

# set up camera, pinger, and thrusters
# camera, model = cam.cam_setup()
#myPing = pinger.ping_setup()
thruster_setup()
#mission.setup()

# set up vector nav
s = VnSensor()
s.connect("/dev/ttyUSB0",115200)

"""
# mission switch
status = 0
while status == 0:
	status = mission.start()
	time.sleep(1)
"""
# record initial orientation
orientation = s.read_yaw_pitch_roll()
origin = orientation.x
print("origin =",origin)


A2.setSpeed(70)
A4.setSpeed(70)
#M2.setSpeed(110)
M4.setSpeed(65)
A2.run()
A4.run()
#M2.run()
M4.run()
time.sleep(5)

"""
# go down to specified depth and hover
goal = 0.28
ping = pinger.depth(myPing)
print(ping)
while ping > goal:
	print(ping)
	print("down")
	A2.setSpeed(70)
	A4.setSpeed(110)
	M2.setSpeed(110)
	M4.setSpeed(70)
	A2.run()
	A4.run()
	M2.run()
	M4.run()
	time.sleep(0.5)
	ping = pinger.depth(myPing)
	print()
"""	
	
"""
print("hovering")
A2.setSpeed(71)
A4.setSpeed(109)
M2.setSpeed(109)
M4.setSpeed(71)
A2.run()
A4.run()
M2.run()
M4.run()
print("hover")
"""

A2.setSpeed(90)
A4.setSpeed(90)
#M2.setSpeed(90)
M4.setSpeed(90)
A2.run()
A4.run()
#M2.run()
M4.run()

count = 5
# go straight using vectornav
c = 0
while True:
	x = vn.orient(s)
	print(x)
	state = vn.direction(origin, x, c)
	#ping = pinger.depth(myPing)
	#pinger.move(ping, goal)
	if state == "R":
		#M3.setSpeed(97)
		M1.setSpeed(93)
		A1.setSpeed(87)
		#A3.setSpeed(83)
		A1.run()
		#A3.run()
		M1.run()
		#M3.run()
		A2.run()
		A4.run()
		M2.run()
		M4.run()
		
			
	elif state == "L":
		print("turning left")
		A1.setSpeed(105)
		#A3.setSpeed(95)
		M1.setSpeed(75)
		#M3.setSpeed(85)
		A1.run()
		#A3.run()
		M1.run()
		#M3.run()
		A2.run()
		A4.run()
		M2.run()
		M4.run()
		
		
	else:
		print("going forward 1")
		A1.setSpeed(70)
		#A3.setSpeed(81)
		M1.setSpeed(69)
		#M3.setSpeed(80)
		A1.run()
		#A3.run()
		M1.run()
		#M3.run()
		A2.run()
		A4.run()
		#M2.run()
		M4.run()
		A2.run()
		A4.run()
		M2.run()
		M4.run()

			
	"""
	ping = pinger.depth(myPing)
	if ping > goal:
		print("down")
		A2.setSpeed(70)
		A4.setSpeed(110)
		M2.setSpeed(110)
		M4.setSpeed(70)
		A2.run()
		A4.run()
		M2.run()
		M4.run()
		time.sleep(1)
	
	else:
		print("float, thrusters off")
	"""
	"""
	check = c % 3
	if check == 0:
		print("up")
		A2.setSpeed(90)
		A4.setSpeed(90)
		M2.setSpeed(90)
		M4.setSpeed(90)
		A2.run()
		A4.run()
		M2.run()
		M4.run()
		
	else:
		print("down")
		A2.setSpeed(70)
		A4.setSpeed(70)
		#M2.setSpeed(110)
		M4.setSpeed(65)
		A2.run()
		A4.run()
		#M2.run()
		M4.run()
	"""
	c += 1
	time.sleep(1)
	#print("going straight?")
	print()
	
	
	
