import time
from adafruit_servokit import ServoKit

# initiate thrusters
kit = ServoKit(channels = 16)

# Turn OFF all thrusters
A1 = kit.servo[0].angle = 90   
A2 = kit.servo[1].angle = 90   
A3 = kit.servo[2].angle = 90   
A4 = kit.servo[3].angle = 90   
M1 = kit.servo[4].angle = 90    
M2 = kit.servo[5].angle = 90    
M3 = kit.servo[6].angle = 90   
M4 = kit.servo[7].angle = 90    

# servo.angle == 90

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
			print("boop")
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



# forward for 30 seconds
print("going forward")
A1.setSpeed(100)
A3.setSpeed(100)
M1.setSpeed(100)
M3.setSpeed(100)
A1.run()
A3.run()
M1.run()
M3.run()
time.sleep(30)


# right for 10 seconds
print("turning right")
A1.setSpeed(100)
A3.setSpeed(100)
M1.setSpeed(80)
M3.setSpeed(80)
A1.run()
A3.run()
M1.run()
M3.run()
time.sleep(10)
	
	
# left for 10 seconds
print("turning left")
M1.setSpeed(100)
M3.setSpeed(100)
A1.setSpeed(80)
A3.setSpeed(80)
A1.run()
A3.run()
M1.run()
M3.run()


"""
# observe down speeds
print("down")
A2.setSpeed(85)
A4.setSpeed(85)
M2.setSpeed(85)
M4.setSpeed(85)
A2.run()
A4.run()
M2.run()
M4.run()
time.sleep(10)

A2.setSpeed(80)
A4.setSpeed(80)
M2.setSpeed(80)
M4.setSpeed(80)
A2.run()
A4.run()
M2.run()
M4.run()
time.sleep(10)

A2.setSpeed(75)
A4.setSpeed(75)
M2.setSpeed(75)
M4.setSpeed(75)
A2.run()
A4.run()
M2.run()
M4.run()
time.sleep(10)

A2.setSpeed(70)
A4.setSpeed(70)
M2.setSpeed(70)
M4.setSpeed(70)
A2.run()
A4.run()
M2.run()
M4.run()
time.sleep(10)

A2.setSpeed(65)
A4.setSpeed(65)
M2.setSpeed(65)
M4.setSpeed(65)
A2.run()
A4.run()
M2.run()
M4.run()
time.sleep(10)
"""
