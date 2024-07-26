# import functions
# from pkg import cam_around, thrusters, vn
from pkg import pinger
import time

myPing = pinger.ping_setup()

while True:
	data = pinger.depth(myPing)
	print(data)
	
	time.sleep(1)
