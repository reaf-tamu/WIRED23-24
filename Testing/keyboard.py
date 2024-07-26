# copied from jetson after test
# imports
import time
from adafruit_servokit import ServoKit
from pynput import keyboard


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
			#print("boop")
			kit.servo[self.name].angle = self.speed
			self.prev_speed = self.speed
		else:
			return
	def stop(self):
		kit.servo[name] = 90

# set thruster pins
A1 = Motor(0)
A2 = Motor(1)
A3 = Motor(2)
A4 = Motor(3)
M1 = Motor(4)
M2 = Motor(5)
M3 = Motor(6)
M4 = Motor(7)

M4.setSpeed(90)
M4.run()
M3.setSpeed(90)
M3.run()
M2.setSpeed(90)
M2.run()
M1.setSpeed(90)
M1.run()
A4.setSpeed(90)
A4.run()
A3.setSpeed(90)
A3.run()
A2.setSpeed(90)
A2.run()
A1.setSpeed(90)
A1.run()


# FIXME: foward/backward need to be switched, left/right need to be switched
print("ready")
def on_key_release(key):
	if key == keyboard.Key.esc:
		return False  # Stop the listener
	try:
		# forward
		if key.char == "w":
			print("forward")
			A1.setSpeed(81)
			A3.setSpeed(81)
			M1.setSpeed(80)
			M3.setSpeed(80)
			A1.run()
			A3.run()
			M1.run()
			M3.run()
		
		if key.char == "e":
			print("forward")
			A1.setSpeed(80)
			A3.setSpeed(80)
			M1.setSpeed(80)
			M3.setSpeed(80)
			A1.run()
			A3.run()
			M1.run()
			M3.run()


		# backward
		if key.char == "s":
			print("backward")


		# up
		if key.char == "p":
			print("up")


		# down
		if key.char == "l":
			print("down")
			A2.setSpeed(71)
			A4.setSpeed(109)
			M2.setSpeed(109)
			M4.setSpeed(71)
			A2.run()
			A4.run()
			M2.run()
			M4.run()

		# left
		if key.char == "d":
			print("right")
			M1.setSpeed(100)
			M3.setSpeed(100)
			A1.setSpeed(80)
			A3.setSpeed(80)
			A1.run()
			A3.run()
			M1.run()
			M3.run()

		# right
		if key.char == 'a':
			print("left")
			A1.setSpeed(100)
			A3.setSpeed(100)
			M1.setSpeed(80)
			M3.setSpeed(80)
			A1.run()
			A3.run()
			M1.run()
			M3.run()

		# stop
		if key.char == "x":
			print("stopping")
			M1.setSpeed(90)
			M2.setSpeed(90)
			M3.setSpeed(90)						
			M4.setSpeed(90)
			A1.setSpeed(90)
			A2.setSpeed(90)
			A3.setSpeed(90)
			A4.setSpeed(90)
			M1.run()
			M2.run()
			M3.run()
			M4.run()
			A1.run()
			A2.run()
			A3.run()
			A4.run()

	except AttributeError:
		pass

# Collect events until released
with keyboard.Listener(on_release=on_key_release) as listener:
	listener.join()
