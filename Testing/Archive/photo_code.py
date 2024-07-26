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

# load a pre-trained yolov8n model
model = get_roboflow_model(model_id="bouy-bg2fz/1")

i = 1

for i in range(20):
	# define the image url to use for inference
	image_file = "frame (" + str(i+1) + ").jpg"
	image = cv2.imread(image_file)
	print(image_file)
	# height, width, channels = image.shape
	# print(f"Width of the image: {width} pixels")
	#cv2.imshow("Combined Image", image)
	
	results = model.infer(image)

	# load the results into the supervision Detections api
	detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))

	# create supervision annotators
	bounding_box_annotator = sv.BoundingBoxAnnotator()
	label_annotator = sv.LabelAnnotator()

	# annotate the image with our inference results
	annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
	annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

	# print detected label
	try:
		print(results[0].predictions[0].class_name)
		# print(results[0].predictions[0].x)
		# sv.plot_image(annotated_image)
		# print(results)
	except IndexError:
		continue
			
	buoy = 0
	
	#only go into this if statement if buoy is detected
	for k in range(5):
		try:
			for j in range(5):
				try:
					if results[0].predictions[j].class_name == "buoy_red" or results[0].predictions[j].class_name == "bola_merah" or results[0].predictions[j].class_name == "Orange":
						print(f"buoy =",results[0].predictions[j].class_name)
						print("location =", results[0].predictions[j].x)
						# move left
						if results[0].predictions[j].x < 1916:
							print("move left")
						elif results[0].predictions[j].x > 2116:
							print("move right")
						else:
							# display the image
							# sv.plot_image(annotated_image)
							print("centered")
						buoy = 1
						
				except:
					continue
			
			if buoy == 0:		
				print("nothing, turn right")
			else:
				buoy = 0
			# else:
				# print("turn right")
		except:
			continue

	print()
	
	# num += 1
	time.sleep(2)
