import time
from adafruit_servokit import ServoKit

# Initialize PCA9685 (16 channels)
kit = ServoKit(channels=16)

# ESC is on channel 7
ESC_CHANNEL = 7

# Set correct PWM range for ESCs (BlueRobotics: 1100–1900 µs)
kit.servo[ESC_CHANNEL].set_pulse_width_range(1100, 1900)

class Motor:
    def __init__(self, channel):
        self.channel = channel
        self.speed = 90  # Default = neutral (1500 µs)
        self.prev_speed = None  # Force first update

    def set_speed(self, angle):
        self.speed = angle

    def run(self):
        if self.prev_speed != self.speed:
            print(f"Motor[{self.channel}]: angle = {self.speed}")
            kit.servo[self.channel].angle = self.speed
            self.prev_speed = self.speed

    def stop(self):
        self.set_speed(90)
        self.run()

# Initialize motor on CH7
A1 = Motor(ESC_CHANNEL)

# Step 1: ESC Initialization
print("Initializing ESC...")
A1.set_speed(90)  # 1500 µs = neutral
A1.run()
time.sleep(5)  # Wait 5 seconds for ESC to beep twice

# Step 2: Control loop
print("Entering control loop. Ctrl+C to stop.")
try:
    while True:
        A1.set_speed(80)  # ~1400 µs → reverse thrust
        A1.run()
        print(f"A1 running at {A1.speed}°")
        time.sleep(2)

        A1.set_speed(100)  # ~1600 µs → forward thrust
        A1.run()
        print(f"A1 running at {A1.speed}°")
        time.sleep(2)

#        A1.stop()
#        print("A1 stopped")
#        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopping...")
    A1.stop()

