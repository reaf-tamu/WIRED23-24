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
	A3 = Motor(2)
	A4 = Motor(3)
	M1 = Motor(4)
	M2 = Motor(5)
	M3 = Motor(6)
	M4 = Motor(7)

# set up camera, pinger, and thrusters
# camera, model = cam.cam_setup()
myPing = pinger.ping_setup()
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

"""
# go down to specified depth and hover
goal = 500
ping = pinger.depth(myPing)
while ping > goal:
	pinger.move(ping, goal)
	time.sleep(1)
	ping = pinger.depth(myPing)
	print("going down")
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
# go straight using vectornav
c = 0
while True:
	x = vn.orient(s)
	print(x)
	state = vn.direction(origin, x, c)
	#ping = pinger.depth(myPing)
	#pinger.move(ping, goal)
	if state == "L":
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
		"""
		print("turning left")
		M3.setSpeed(100)
		#M1.setSpeed(100)
		#A1.setSpeed(80)
		A3.setSpeed(80)
		#A1.run()
		A3.run()
		#M1.run()
		M3.run()
	elif state == "R":
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
		"""
		print("turning right")
		#A1.setSpeed(100)
		A3.setSpeed(100)
		#M1.setSpeed(80)
		M3.setSpeed(80)
		#A1.run()
		A3.run()
		#M1.run()
		M3.run()
	else:
		if c % 2 == 0:
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
			"""
			print("going forward 1")
			#A1.setSpeed(81)
			A3.setSpeed(81)
			#M1.setSpeed(80)
			M3.setSpeed(80)
			#A1.run()
			A3.run()
			#M1.run()
			M3.run()
		else:
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
			"""
			print("going forward 2")
			#A1.setSpeed(80)
			A3.setSpeed(80)
			#M1.setSpeed(80)
			M3.setSpeed(80)
			#A1.run()
			A3.run()
			#M1.run()
			M3.run()
	
	time.sleep(1)
	#print("going straight?")
	print()
	
	
	
