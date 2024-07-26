# have to run this the first time nano after nano it turned on
# export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v


# import a utility function for loading Roboflow models
from inference import get_roboflow_model
# import supervision to visualize our results
import supervision as sv
# import cv2 to help load our image
import cv2
import time
import string
import numpy as np

def infer(image, model):
	results = model.infer(image)
	direction = "right"

	for k in range(5):
		try:
			for j in range(5):
				try:
					if results[0].predictions[j].class_name == "buoy_red" or results[0].predictions[j].class_name == "bola_merah" or results[0].predictions[j].class_name == "Orange":
						# move left
						if results[0].predictions[j].x < 1916:
							direction = "left"
						elif results[0].predictions[j].x > 2116:
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
