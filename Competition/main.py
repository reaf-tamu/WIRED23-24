# have to run this the first time nano after nano it turned on
# export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v

# import functions
from pkg import cam, pinger, thrusters, vn

# imports
import cv2
import time
import numpy as np
from vnpy import *


# set up camera, pinger, and thrusters
camera, model = cam.cam_setup()
myPing = pinger.ping_setup()
thrusters.thruster_setup()

# set up vector nav
s = VnSensor()
s.connect("/dev/ttyUSB1",115200)


# mission switch

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



# look for gate by spinning (coin toss)
gate = 0
while gate == 0:
	result, frame = camera.read()
	results = cam.infer(frame, model)
	gate, X = cam.detect_gate(results)
	thrusters.right()
	
	time.sleep(0.5)



# move toward gate and pass through gate
#FIX ME: HOW DO I GET OUT OF THE LOOP
while True:
	# see gate
	result, frame = camera.read()
	results = cam.infer(frame, model)
	gate, X = cam.detect_gate(results)
	
	# center and move to gate
	cam.move(X)
	
	time.sleep(0.5)



# maybe pick a side by looking at arrows
# maybe spin (style points) (keep track using vn)



# look for buoy
buoy = 0
while buoy == 0:
	result, frame = camera.read()
	results = cam.infer(frame, model)
	buoy, X = cam.detect_buoy(results)
	thrusters.right()
	
	time.sleep(0.5)

# drive toward buoy and bump buoy
#FIX ME: HOW DO I GET OUT OF THE LOOP
while True:
	# see buoy
	result, frame = camera.read()
	results = cam.infer(frame, model)
	buoy, X = cam.detect_buoy(results)
	
	# center and move to buoy
	cam.move(X)
	
	time.sleep(0.5)
	
# maybe go around buoy


# bins

# octagon

# grabber
	

# maybe use some of this code
"""
# pass through gate by going straight for specified time
c = 0
while c <= 6:
	# check vector nav
	vn.orient()
	vn.direction(origin, x)

	# run straight thrusters if ready
	if state == "F":
		thrusters.forward(c)
	else:
		continue
	
	c += 1
	time.sleep(1)



# start looking for buoy
buoy = 0
c = 0
while buoy == 0:
	# take photo and run through inference function
	result, frame = camera.read()
	seen = cam_around.infer(frame, model)
	
# continue straight for now
thrusters.forward(c)

c += 1
time.sleep(1)



# go around buoy until facing backwards
around = False
while around == False:
	# check vector nav
	vn.orient()
	if ((x > (back - 10)) or (x < (back + 10)):
		around = True
	
	# is buoy still there
	seen = cam_around.infer(frame, model)
	if seen == 0:
		# turn if no buoy
		thrusters.right()
	else:
		# thrusters determined by function
		cam_around.move()



# pass through gate again by going straight for specified time
c = 0
while c <= 6:
	# check vector nav
	vn.orient()
	vn.direction(back, x)

	# run straight thrusters if ready
	if state == "F":
		thrusters.forward(c)
	else:
		continue
	
c += 1
	time.sleep(1)
"""
