import time
from adafruit_servokit import ServoKit

def thruster_setup():
	# initiate thrusters
	kit = ServoKit(channels = 16)

	"""
	# Turn OFF all thrusters
	A1 = kit.servo[0].angle = 90   
	A2 = kit.servo[1].angle = 90   
	A3 = kit.servo[2].angle = 90   
	A4 = kit.servo[3].angle = 90   
	M1 = kit.servo[7].angle = 90    
	M2 = kit.servo[9].angle = 90    
	M3 = kit.servo[10].angle = 90   
	M4 = kit.servo[13].angle = 90    
	"""

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

def hover():
	print("hovering")
	A2.setSpeed(71)
	A4.setSpeed(109)
	M2.setSpeed(109)
	M4.setSpeed(71)
	A2.run()
	A4.run()
	M2.run()
	M4.run()

def right():
	hover()
	print("turning right")
	A1.setSpeed(100)
	A3.setSpeed(100)
	M1.setSpeed(80)
	M3.setSpeed(80)
	A1.run()
	A3.run()
	M1.run()
	M3.run()
	
def left():
	hover()
	print("turning left")
	M1.setSpeed(100)
	M3.setSpeed(100)
	A1.setSpeed(80)
	A3.setSpeed(80)
	A1.run()
	A3.run()
	M1.run()
	M3.run()
	
def forward1():
	hover()
	print("going forward 1")
	A1.setSpeed(81)
	A3.setSpeed(81)
	M1.setSpeed(80)
	M3.setSpeed(80)
	A1.run()
	A3.run()
	M1.run()
	M3.run()
	
def forward2():
	hover()
	print("going forward 2")
	A1.setSpeed(80)
	A3.setSpeed(80)
	M1.setSpeed(80)
	M3.setSpeed(80)
	A1.run()
	A3.run()
	M1.run()
	M3.run()
	
	time.sleep(1)
	

def down():
	print("going down")
	A2.setSpeed(70)
	A4.setSpeed(110)
	M2.setSpeed(110)
	M4.setSpeed(70)
	A2.run()
	A4.run()
	M2.run()
	M4.run()

def up():
	print("going up")
	



