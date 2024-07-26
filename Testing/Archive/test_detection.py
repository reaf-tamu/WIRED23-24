# import a utility function for loading Roboflow models
from inference import get_roboflow_model
# import supervision to visualize our results
import supervision as sv
# import cv2 to help load our image
import cv2
import time

#camera
cam = cv2.VideoCapture(0)
result, image = cam.read(0)
# count = 0
# cv2.imwrite("frame0.jpg", image)


# load a pre-trained yolov8n model
model = get_roboflow_model(model_id="bouy-bg2fz/1")

while True:

	result, image = cam.read(0)

	# run inference on our chosen image, image can be a url, a numpy array, a PIL image, etc.
	results = model.infer(image)

	# load the results into the supervision Detections api
	detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))

	# create supervision annotators
	bounding_box_annotator = sv.BoundingBoxAnnotator()
	label_annotator = sv.LabelAnnotator()

	# annotate the image with our inference results
	annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
	annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

	# display the image
	sv.plot_image(annotated_image)
	

	time.sleep(1)
