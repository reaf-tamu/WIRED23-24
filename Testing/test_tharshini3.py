import time
import Jetson.GPIO as GPIO
from adafruit_servokit import ServoKit

# -------------------------
# GPIO Setup
# -------------------------
BUTTON_PIN = 12  # Pin 32 = BCM 12

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# -------------------------
# ESC and Motor Setup
# -------------------------
kit = ServoKit(channels=16)
kit.servo[7].set_pulse_width_range(1100, 1900)

class Motor:
    def __init__(self, channel):
        self.channel = channel
        self.speed = 90
        self.prev_speed = None

    def set_speed(self, angle):
        self.speed = angle

    def run(self):
        if self.prev_speed != self.speed:
            print(f"Sending PWM: {self.speed}°")
            kit.servo[self.channel].angle = self.speed
            self.prev_speed = self.speed

    def stop(self):
        self.set_speed(90)
        self.run()

A1 = Motor(7)

# -------------------------
# Wait for Button Press
# -------------------------
print("Waiting for button press to start...")
try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            print("Button pressed. Starting motor sequence...")
            break
        time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

# -------------------------
# ESC Initialization
# -------------------------
print("Initializing ESC with 1500 µs (90°) signal...")
A1.set_speed(90)
A1.run()
time.sleep(5)

print("Setting speed to 80° (reverse thrust)...")
A1.set_speed(80)
A1.run()
time.sleep(3)

print("Setting speed to 100° (forward thrust)...")
A1.set_speed(100)
A1.run()
time.sleep(3)

print("Stopping motor...")
A1.stop()

# -------------------------
# Cleanup GPIO
# -------------------------
GPIO.cleanup()

