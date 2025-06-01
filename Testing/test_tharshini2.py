import time
from adafruit_servokit import ServoKit

# Initialize PCA9685 with 16 channels
kit = ServoKit(channels=16)

# Set correct PWM range for ESCs: 1100–1900 µs
kit.servo[7].set_pulse_width_range(1100, 1900)

class Motor:
    def __init__(self, channel):
        self.channel = channel
        self.speed = 90  # Default to neutral (1500 µs)
        self.prev_speed = None  # Force update on first run

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

# Initialize A1 on channel 7 (ESC signal wire is connected here)
A1 = Motor(7)

# -------------------------
# STEP 1: ESC Initialization
# -------------------------

print("Initializing ESC with 1500 µs (90°) signal...")
A1.set_speed(90)
A1.run()
time.sleep(5)  # Wait 5 seconds for ESC to arm (listen for 2 beeps)

# -------------------------
# STEP 2: Set desired speed
# -------------------------

print("Setting speed to 80° (reverse thrust)...")
A1.set_speed(80)  # ~1400 µs (reverse)
A1.run()
time.sleep(3)

print("Setting speed to 100° (forward thrust)...")
A1.set_speed(100)  # ~1600 µs (forward)
A1.run()
time.sleep(3)

print("Stopping motor...")
A1.stop()

