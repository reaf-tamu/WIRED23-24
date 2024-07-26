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

# Initialize camera
cam = cv2.VideoCapture(0)

# Load a pre-trained YOLOv8n model
model = get_roboflow_model(model_id="bouy-bg2fz/1")

while True:
    # Capture the image from the camera
    result, frame = cam.read(0)

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
    # Adjust alpha values to see both images
    alpha = 0.5  # Transparency factor
    combined_image = cv2.addWeighted(left_image, alpha, right_image, 1 - alpha, 0)

    # Run inference on the combined image
    results = model.infer(combined_image)

    # Load the results into the supervision Detections API
    detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))

    # Create supervision annotators
    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    # Annotate the image with inference results
    annotated_image = bounding_box_annotator.annotate(scene=combined_image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    # Print detected labels
    try:
        for prediction in results[0].predictions:
            print(prediction.class_name)
            print(prediction.x)
        sv.plot_image(annotated_image)
    except IndexError:
        continue

    # Display the annotated image
    cv2.imshow("Annotated Image", annotated_image)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(3)

# Release the camera and close OpenCV windows
cam.release()
cv2.destroyAllWindows()
