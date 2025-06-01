import Jetson.GPIO as GPIO
import time

BUTTON_PIN = 12

GPIO.setmode(GPIO.BCM)
# Setup
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Wait for button press (LOW when pressed)
print("Waiting for button press to start...")
try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button is pressed
            print("Button pressed. Starting motor sequence...")
            break
        time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
