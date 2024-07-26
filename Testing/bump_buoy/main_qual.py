# have to run this the first time nano after nano it turned on
# export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v

# import functions
from pkg import cam_around, pinger, thrusters, vn

# imports
# import a utility function for loading Roboflow models
from inference import get_roboflow_model
# import supervision to visualize our results
import supervision as sv
# import cv2 to help load our image
import cv2
import time
import numpy as np
from vnpy import *


# set up sensors
camera, model = cam_around.cam_setup()
# myPing = pinger.ping_setup()
thrusters.thruster_setup()
s = VnSensor()
s.connect("/dev/ttyUSB0",115200)



# go down for specified time, then hover
thrusters.down()
time.sleep(3)
thrusters.hover()



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



# pass through gate by going straight for specified time
# runs each forward thruster command for 1 second
count = 0
while count <= 6:
	# check vector nav
	vn.orient()
	vn.direction(origin, x)
	# run straight thrusters
	thrusters.forward1()
	
	count += 1
	time.sleep(1)
	
	# check vector nav
	vn.orient()
	vn.direction(origin, x)
	# run straight thrusters
	thrusters.forward1()
	
	count += 1
	time.sleep(1)



# start looking for buoy, continue going straight?
around = False
while around = False:
	# take photo and run through inference function
	result, frame = camera.read()
	direction = cam_around.infer(frame, model)
	
	# thrusters directed by camera model
	# may need to change direction to go straight if buoy is not seen
	if direction == "left":
		#print("left")
		thrusters.left()
	elif direction == "right":
		#print("right")
		thrusters.right()
	elif direction == "centered":
		#print("forward")
		thrusters.forward1()

	time.sleep(0.5)

	# check vn until it is facing backwards
	vn.orient()
	if (x > (back - 10)) or (x < (back + 10):
		around = True
		

# go back to gate by going straight for specified time
count = 0
while count <= 6:
	# check vector nav
	vn.orient()
	vn.direction(back, x)
	# run straight thrusters
	thrusters.forward1()
	
	count += 1
	time.sleep(1)
	
	# check vector nav
	vn.orient()
	vn.direction(back, x)
	# run straight thrusters
	thrusters.forward1()
	
	count += 1
	time.sleep(1)

"""
# start going straight back to gate
origin = vn.gyro(s)
print("origin =", origin)
origin_left = origin + 10
origin_right = origin - 10
count = 0
while count < 3:
	heading = vn.gyro(s)
	print(heading)
	if heading > origin_left:
		#print("left")
		thrusters.left()
	elif heading < origin_right:
		#print("right")
		thrusters.right()
	else:
		#print("centered")
		thrusters.forward()
	print()
	count += 1
	time.sleep(1)


back = origin - 180
print(back)
back_left = origin + 10
back_right = origin - 10


while True:
	# take photo and run through inference function
	result, frame = camera.read()
	direction = cam_around.infer(frame, model)
	# print(direction)
	heading = vn.gyro(s)
	# print("gyro =",heading)
	# ping = pinger.depth(myPing)
	# print(f"Direction: {direction}, depth: {ping}")
	
	
	# check if it has done a full circle
	if heading < (back + 20) or heading > (back - 20):
		#break
	
	
	if direction == "left":
		#print("left")
		thrusters.left()
	elif direction == "right":
		#print("right")
		thrusters.right()
	elif direction == "centered":
		#print("forward")
		thrusters.forward()

	time.sleep(0.5)



# pass through gate by going straight for specified time
while count < 15:
	heading = vn.gyro(s)
	if heading < back_left:
		print("left")
	elif heading > back_right:
		print("right")
	else:
		print("centered")
	count += 1
	time.sleep(1)
"""
