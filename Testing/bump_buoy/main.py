# have to run this the first time nano after nano it turned on
# export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v

# import functions
from pkg import cam, pinger, thrusters, photo, vn

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

camera, model = cam.cam_setup()
# myPing = pinger.ping_setup()
thrusters.thruster_setup()
s = VnSensor()
s.connect("/dev/ttyUSB0",115200)

while True:
	# take photo and run through inference function
	result, frame = camera.read()
	direction = cam.infer(frame, model)
	print(direction)
	heading = vn.gyro(s)
	print("gyro =",heading)
	# ping = pinger.depth(myPing)
	# print(f"Direction: {direction}, depth: {ping}")
	
	if direction == "left":
		thrusters.left()
	elif direction == "right":
		thrusters.right()
	elif direction == "centered":
		thrusters.forward()

	time.sleep(0.5)
