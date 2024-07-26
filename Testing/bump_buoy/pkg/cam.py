# imports
# import a utility function for loading Roboflow models
from inference import get_roboflow_model
# import cv2 to help load our image
import cv2
import time
import numpy as np

def cam_setup():
	#camera
	camera = cv2.VideoCapture(0)

	# load a pre-trained yolov8n model
	model = get_roboflow_model(model_id="bouy-bg2fz/1")
	
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
	#cv2.imshow("Combined Image", image)
	
	results = model.infer(image)

	# print detected label
	try:
		print(results[0].predictions[0].class_name)
		print(results[0].predictions[0].x)
		# sv.plot_image(annotated_image)
		# print(results)
	except IndexError:
		print("nothing")
			

	try:
		#only go into this if statement if buoy is detected
		if results[0].predictions[0].class_name == "buoy_red" or results[0].predictions[0].class_name == "bola_merah" or results[0].predictions[0].class_name == "Orange":
			# move left
			if results[0].predictions[0].x < 300:
				direction = "left"
			elif results[0].predictions[0].x > 400:
				direction = "right"
			else:
				# display the image
				# sv.plot_image(annotated_image)
				direction = "centered"
		else:
			direction = "turn right"
	except IndexError:
		print("detected")
		direction = "none"
		
	return	direction
