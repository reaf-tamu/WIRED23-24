# have to run this the first time nano after nano it turned on
# export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v

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

	# load v2 model
	model = get_roboflow_model(model_id="bouy-bg2fz/3")
	
	return camera, model
	

def infer(frame, model):
	# direction = "left"

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
		# print(results[0].predictions[0].class_name)
		# print(results[0].predictions[0].x)
		# print(results[0].predictions[0].confidence)
		# sv.plot_image(annotated_image)
		print(results)
	except IndexError:
		print("nothing")
		

	for k in range(5):
		try:
			for j in range(5):
				try:
					if ((results[0].predictions[j].class_name == "buoy" or results[0].predictions[j].class_name == "Orange") and (results[0].predictions[0].confidence >= 0.75)):
						if results[0].predictions[j].x < 50:
							direction = "left"
						elif results[0].predictions[j].x > 150:
							direction = "right"
						else:
							# display the image
							# sv.plot_image(annotated_image)
							direction = "centered"
						buoy = 1
						
				except:
					continue
			
			if buoy == 0:		
				direction = "right"
			else:
				buoy = 0
				
		except:
			continue
	return direction
	

"""
	try:
		#only go into this if statement if buoy is detected
		if results[0].predictions[0].class_name == "buoy" or results[0].predictions[0].class_name == "Orange":
				# move left
			if results[0].predictions[0].x < 50:
				direction = "left"
			elif results[0].predictions[0].x > 150:
				direction = "right"
			else:
				# display the image
				# sv.plot_image(annotated_image)
				direction = "centered"
		else:
			direction = "left"		
	except IndexError:
		print("detected")
		direction = "none"
	
	return	direction
	"""
