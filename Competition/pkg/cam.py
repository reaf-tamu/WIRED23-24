# have to run this the first time nano after nano it turned on
#export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v

# imports
from inference import get_roboflow_model
import cv2
import time
import numpy as np
from . import thrusters



def cam_setup():
	#camera
	camera = cv2.VideoCapture(0)

	# load v2 model
	model = get_roboflow_model(model_id="bouy-bg2fz/4")
	
	return camera, model


def infer(frame, model):
	# Assume the frame contains the left and right images side by side
	height, width, _ = frame.shape
	half_width = width // 2

	# Split the image into left and right images
	left_image = frame[:, :half_width]
	right_image = frame[:, half_width:]

	# Create a combined image by overlaying (use blending or addWeighted)
	# Here we use addWeighted to overlay the images
	alpha = 1  # Transparency factor
	combined_image = cv2.addWeighted(left_image, alpha, right_image, 1 - alpha, 0)
	cv2.imwrite("frame.jpg", combined_image)
	
	# define the image url to use for inference
	image_file = "frame.jpg"
	image = cv2.imread(image_file)
	
	results = model.infer(image)

	# print detected label
	try:
		# print(results[0].predictions[0].class_name)
		# print(results[0].predictions[0].x)
		# print(results[0].predictions[0].confidence)
		# sv.plot_image(annotated_image)
		print(results)
	except IndexError:
		print("nothing")
	
	return results

def detect_buoy(results):
	for k in range(5):
		try:
			for j in range(5):
				try:
					if ((results[0].predictions[j].class_name == "buoy") and (results[0].predictions[j].confidence >= 0.75)):
						buoy = 1
						X = results[0].predictions[j].x
						
				except:
					continue
			
			else:
				buoy = 0

		except:
			continue

	return buoy, X


def detect_gate(results):
	for k in range(5):
		try:
			for j in range(5):
				try:
					if ((results[0].predictions[j].class_name == "gate") and (results[0].predictions[j].confidence >= 0.75)):
						gate = 1
						X = results[0].predictions[j].x
						
				except:
					continue
			
			else:
				gate = 0

		except:
			continue

	return gate, X
	


	
	
	
def move(X):
	if X < 550:
		thrusters.left()
	elif X > 580:
		thruster.right()
	else:
		thrusters.forward()
