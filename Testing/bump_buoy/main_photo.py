# have to run this the first time nano after nano it turned on
# export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v

# import functions
from pkg import pinger, thrusters, photo

# imports
# import a utility function for loading Roboflow models
from inference import get_roboflow_model
# import supervision to visualize our results
import supervision as sv
# import cv2 to help load our image
import cv2
import time
import numpy as np

model = get_roboflow_model(model_id="bouy-bg2fz/1")
# myPing = pinger.ping_setup()
thrusters.thruster_setup()

i = 1

time.sleep(180)

while True:
	# define the image url to use for inference
	image_file = "frame (" + str(i+1) + ").jpg"
	image = cv2.imread(image_file)
	print(image_file)
	
	direction = photo.infer(image, model)
	print(direction)
	
	
	if direction == "left":
		thrusters.left()
	elif direction == "right":
		thrusters.right()
	elif direction == "centered":
		thrusters.forward()


	i += 1
	print()
	time.sleep(1)
