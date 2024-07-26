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
from adafruit_servokit import ServoKit

# initiate thrusters
kit = ServoKit(channels = 16)

"""
# Turn OFF all thrusters
A1 = kit.servo[0].angle = 90   
A2 = kit.servo[1].angle = 90   
A3 = kit.servo[2].angle = 90   
A4 = kit.servo[3].angle = 90   
M1 = kit.servo[7].angle = 90    
M2 = kit.servo[9].angle = 90    
M3 = kit.servo[10].angle = 90   
M4 = kit.servo[13].angle = 90    
"""

def set_speed(speed, motor):
	kit.servo[motor].angle = speed
	return

class Motor:
	def __init__(self, name):
		self.name = name
		self.speed = 90
		self.prev_speed = self.speed
	def setSpeed(self, speed):
		self.speed = speed

	def run(self):
		if self.prev_speed != self.speed:
			# print("boop")
			kit.servo[self.name].angle = self.speed
			self.prev_speed = self.speed
		else:
			return
	def stop(self):
		kit.servo[name] = 90

# set thrusters as global variables
global A1, A2, A3, A4, M1, M2, M3, M4	
global A2

# set thruster pins
A1 = Motor(0)
A2 = Motor(1)
A3 = Motor(2)
A4 = Motor(3)
M1 = Motor(4)
M2 = Motor(5)
M3 = Motor(6)
M4 = Motor(7)

#camera
cam = cv2.VideoCapture(0)

# load a pre-trained yolov8n model
model = get_roboflow_model(model_id="bouy-bg2fz/3")

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
		# print(results[0].predictions[0].confidence)
		# print(results)
		# sv.plot_image(annotated_image)
	except IndexError:
		print("nothing detected")
		print("turn right")
		M1.setSpeed(93)
		M3.setSpeed(93)
		A1.setSpeed(87)
		A3.setSpeed(87)
		A1.run()
		A3.run()
		M1.run()
		M3.run()
		continue
			
			
	#only go into this if statement if buoy is detected
	if results[0].predictions[0].class_name == "buoy":
		# move left
		if results[0].predictions[0].x < 550:
			print("turn left")
			A1.setSpeed(93)
			A3.setSpeed(93)
			M1.setSpeed(87)
			M3.setSpeed(87)
			A1.run()
			A3.run()
			M1.run()
			M3.run()
	
		elif results[0].predictions[0].x > 580:
			print("turn right")
			M1.setSpeed(93)
			M3.setSpeed(93)
			A1.setSpeed(87)
			A3.setSpeed(87)
			A1.run()
			A3.run()
			M1.run()
			M3.run()
		else:
			# display the image
			# sv.plot_image(annotated_image)
			print("centered")
			A1.setSpeed(85)
			A3.setSpeed(85)
			M1.setSpeed(85)
			M3.setSpeed(85)
			A1.run()
			A3.run()
			M1.run()
			M3.run()
	else:
		print("turn right")
		M1.setSpeed(93)
		M3.setSpeed(93)
		A1.setSpeed(87)
		A3.setSpeed(87)
		A1.run()
		A3.run()
		M1.run()
		M3.run()
	


	print()
	time.sleep(0.5)
