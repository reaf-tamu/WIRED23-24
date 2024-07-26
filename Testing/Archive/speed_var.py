from adafruit_servokit import ServoKit
import time

#Forward variables
M4F = 100
M1F = 100
A3F = 100
A1F = 100

#Left variables
M4L = 100
M1L = 100
A3L = 80
A1L = 80

#Right variables
M4R = 80
M1R = 80
A3R = 100
A1R = 100

#Backward variables
M4B = 80
M1B = 80
A3B = 80
A1B = 80

#Up variables
A4U = 100
A2U = 80

#Down variables
A4D = 100
A2D = 75

# [M4, M1, A3, A1]
forward = [100,100,100,100]


# initiate thrusters
# initiate thrusters
kit = ServoKit(channels = 16)


# Turn OFF all thrusters
A1 = kit.servo[0].angle = 90
A2 = kit.servo[1].angle = 90
A3 = kit.servo[2].angle = 90
A4 = kit.servo[3].angle = 90
M1 = kit.servo[7].angle = 90
M2 = kit.servo[9].angle = 90
M3 = kit.servo[10].angle = 90
M4 = kit.servo[13].angle = 90


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
M1 = Motor(7)
M2 = Motor(9)
M3 = Motor(10)
M4 = Motor(13)


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



print("forward")
M4.setSpeed(M4F)
M1.setSpeed(M1F)
A3.setSpeed(A3F)
A1.setSpeed(A1F)
M4.run()
M1.run()
A3.run()
A1.run()

time.sleep(5)

print("stopping")
M4.setSpeed(90)
M1.setSpeed(90)
A1.setSpeed(90)
A2.setSpeed(90)
A3.setSpeed(90)
A4.setSpeed(90)
M4.run()
M1.run()
A1.run()
A2.run()
A3.run()
