import cv2

def test_camera(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"Camera {index} cannot be opened.")
        return
    ret, frame = cap.read()
    if not ret:
        print(f"Failed to read from camera {index}.")
    else:
        print(f"Camera {index} is working.")
    cap.release()

# Test all video devices
for i in range(4):
    print(f"Testing /dev/video{i}")
    test_camera(i)

