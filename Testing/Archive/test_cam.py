import cv2
import numpy as np

def main():
    # Open a connection to the ZED Mini camera
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Could not open camera.")
        return

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

        # Display the combined image
        cv2.imshow("Combined Image", combined_image)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close OpenCV windows
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

