# import functions
from pkg import cam, pinger, thrusters, vn, mission

# imports
import cv2
import time
import numpy as np
from vnpy import *

# set up camera, pinger, and thrusters
camera, model = cam.cam_setup()
myPing = pinger.ping_setup()
thrusters.thruster_setup()
mission.setup()

# set up vector nav
s = VnSensor()
s.connect("/dev/ttyUSB1",115200)


# mission switch
status = 0
while status == 0:
	status = mission.start()
	time.sleep(1)

# record initial orientation
orientation = s.read_yaw_pitch_roll()
origin = orientation.x

# go down to specified depth and hover
goal = 3
ping = pinger.depth()
while ping > goal:
  	pinger.move(ping, goal)
	time.sleep(1)
	ping = pinger.depth()

# go straight using vectornav
c = 0
while True:
	x = vn.orient()
	state = vn.direction(origin, x, c)
	pinger.move(ping, goal)
	
	time.sleep(1)
