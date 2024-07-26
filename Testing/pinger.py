from brping import Ping1D


myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB0", 9600)
# For UDP
# myPing.connect_udp("192.168.2.2", 9090)

if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)
    
data = myPing.get_distance()
if data:
    print("Distance: %s\tConfidence: %s%%" % (data["distance"], data["confidence"]))
else:
    print("Failed to get distance data")




"""
import sys
import os


# Add the external package folder to the system path
external_packages_path = os.path.abspath("/home/AUV/ping-python")
if external_packages_path not in sys.path:
    sys.path.insert(0, external_packages_path)

import time
from brping import Ping1D

# Initialize Ping1D instance
myPing = Ping1D()

# Connect to the Ping sensor via the specified serial port at baud rate 115200
print("Attempting to connect to Ping sensor at /dev/ttyUSB0 with baud rate 115200...")
try:
    if myPing.connect_serial("/dev/ttyUSB0", 9600):
        print("Connected to Ping!")
    else:
        print("Failed to connect to Ping.")
        exit(1)
except Exception as e:
    print(f"Exception occurred: {e}")
    exit(1)

# Function to get temperature and depth
def get_sensor_data():
    try:
        # Get depth data
        depth_data = myPing.get_distance()
        if depth_data:
            depth = depth_data["distance"] / 1000.0  # Convert from mm to meters
        else:
            depth = None

        # Get temperature data
        temperature_data = myPing.get_temperature()
        if temperature_data:
            temperature = temperature_data["temperature"] / 100.0  # Convert from centi-degrees to degrees Celsius
        else:
            temperature = None

        return depth, temperature
    except Exception as e:
        print(f"Error getting sensor data: {e}")
        return None, None

# Loop to print temperature and depth
try:
    while True:
        depth, temperature = get_sensor_data()

        if depth is not None:
            print(f"Depth: {depth:.2f} meters")
        else:
            print("Failed to read depth data")

        if temperature is not None:
            print(f"Temperature: {temperature:.2f} °C")
        else:
            print("Failed to read temperature data")

        # Wait for a second before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    myPing.disconnect()
"""
