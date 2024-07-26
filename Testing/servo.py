import time
import board
import busio
from adafruit_servokit import ServoKit

# Initialize I2C bus and ServoKit instance for 16 channels
i2c_bus = busio.I2C(board.SCL, board.SDA)
kit = ServoKit(channels=16, i2c=i2c_bus)

# Function to set the servo angle
def set_servo_angle(channel, angle):
    if 0 <= angle <= 180:
        kit.servo[channel].angle = angle
    else:
        print(f"Invalid angle: {angle}. Angle must be between 0 and 180 degrees.")

# Test the servo on channel 8
servo_channel = 8

# Move servo to 0 degrees
print("Moving servo to 0 degrees")
set_servo_angle(servo_channel, 0)
time.sleep(1)

# Move servo to 90 degrees
print("Moving servo to 90 degrees")
set_servo_angle(servo_channel, 90)
time.sleep(1)

# Move servo to 180 degrees
print("Moving servo to 180 degrees")
set_servo_angle(servo_channel, 180)
time.sleep(1)

# Move servo back to 90 degrees
print("Moving servo back to 90 degrees")
set_servo_angle(servo_channel, 90)
time.sleep(1)

# Move servo back to 0 degrees
print("Moving servo back to 0 degrees")
set_servo_angle(servo_channel, 0)
time.sleep(1)

