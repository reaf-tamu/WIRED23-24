from adafruit_blinka.microcontroller.generic_linux.i2c import I2C as I2CBus

def get_i2c0():
    return I2CBus(0)  
