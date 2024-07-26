# tests if the keyboard and camera model can be used in the same code
# DOES NOT WORK

# have to run this the first time nano after nano it turned on
# export ROBOFLOW_API_KEY=Lw0LcAJ8WMWM4TKlD71v

# import a utility function for loading Roboflow models
from inference import get_roboflow_model
# import supervision to visualize our results
import supervision as sv
# import cv2 to help load our image
import cv2
import time
import numpy as np
from pynput import keyboard

# camera
cam = cv2.VideoCapture(0)

# load a pre-trained yolov8n model
model = get_roboflow_model(model_id="bouy-bg2fz/1")


def on_key_release(key):
	if key == keyboard.Key.esc:
		return False  # Stop the listener
	try:
		# forward
		if key.char == "w":
			print("forward")

		# backward
		if key.char == "s":
			print("backward")

		# up
		if key.char == "p":
				print("up")

		# down
		if key.char == "l":
				print("down")

		# left
		if key.char == "a":
				print("left")

		# right
		if key.char == 'd':
				print("right")

		# stop
		if key.char == "x":
				print("stopping")

	except AttributeError:
		pass

while True:
	# Capture the image from the camera
	result, frame = cam.read()

	if not result:
		print("Error: Could not read frame.")
		break

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
		print(results[0].predictions[0].x)
		# sv.plot_image(annotated_image)
		# print(results)
	except IndexError:
		continue
			

	#only go into this if statement if buoy is detected
	if results[0].predictions[0].class_name == "buoy_red" or results[0].predictions[0].class_name == "bola_merah" or results[0].predictions[0].class_name == "Orange":
		# move left
		if results[0].predictions[0].x < 300:
			print("move left")
		elif results[0].predictions[0].x > 400:
			print("move right")
		else:
			# display the image
			# sv.plot_image(annotated_image)
			print("centered")
	else:
		print("turn right")

	print()
	time.sleep(0.5)
	
	
	with keyboard.Listener(on_release=on_key_release) as listener:
		listener.join()
