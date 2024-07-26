# have to run this the first time nano after nano it turned on
# export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v

# import functions
from pkg import cam_around, pinger, thrusters, vn

# imports
import cv2
import time
import numpy as np
from vnpy import *


# set up camera, pinger, and thrusters
camera, model = cam_around.cam_setup()
myPing = pinger.ping_setup()
thrusters.thruster_setup()

# set up vector nav
s = VnSensor()
s.connect("/dev/ttyUSB1",115200)



# record initial orientation and back
orientation = s.read_yaw_pitch_roll()
origin = orientation.x
print("origin =", origin)

#record going back orientation
if origin > 0:
	back = origin - 180
else:
	back = origin + 180
print("back = ", back)



# go down for specified time, then hover
thrusters.down()
time.sleep(3)
thrusters.hover()



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



