import smbus2
import time

# Define constants
I2C_BUS = 1          # I²C bus number
SENSOR_ADDRESS = 0x76  # Bar30 sensor I²C address

# Create an smbus object
bus = smbus2.SMBus(I2C_BUS)

try:
    # Initialize the sensor (adjust based on sensor requirements)
    # Example: bus.write_byte_data(SENSOR_ADDRESS, 0, 1)
    
    # Read temperature data (example)
    temp_data = bus.read_i2c_block_data(SENSOR_ADDRESS, 0x1E, 2)  # Read 2 bytes starting from register 0x1E

    # Convert temperature data
    temperature_raw = temp_data[0] << 8 | temp_data[1]  # Combine MSB and LSB
    temperature_degC = temperature_raw / 100.0  # Convert to degrees Celsius

    # Print temperature
    print(f"Temperature: {temperature_degC:.2f} °C")

except OSError as e:
    print(f"Error: {e}")
finally:
    # Close the I²C bus
    bus.close()





"""
import ms5837
import time


# connect to sensor
# sensor = ms5837.MS5837_02BA()
sensor = ms5837.MS5837_30BA()

# We must initialize the sensor before reading it
if not sensor.init():
        print("Sensor could not be initialized")
        exit(1)

# We have to read values from sensor to update pressure and temperature
if not sensor.read():
    print("Sensor read failed!")
    exit(1)


# variables for measurement
pressure = sensor.pressure(ms5837.UNITS_psi)
temp = sensor.temperature(ms5837.UNITS_Centigrade)

freshwaterDepth = sensor.depth() # default is freshwater
sensor.setFluidDensity(ms5837.DENSITY_SALTWATER)
saltwaterDepth = sensor.depth() # No nead to read() again
sensor.setFluidDensity(1000) # kg/m^3

print(freshwaterDepth)
print(temp)
"""


