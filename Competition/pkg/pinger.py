from brping import Ping1D
from . import thrusters


# connect to sensor
def ping_setup():
	myPing = Ping1D()
	myPing.connect_serial("/dev/ttyUSB0", 9600)

	if myPing.initialize() is False:
	    print("Failed to initialize Ping!")
	    exit(1)
		
	# suggestions to improve accuracy
	myPing.set_ping_interval(29)
	myPing.set_speed_of_sound(1500)
	
	return myPing

# get depth
def depth(myPing):
	data = myPing.get_distance_simple()
	ping = data["distance"] * (10 ** -3) # convert to meters
	
	return ping

# adjust depth
def move(depth, goal):
	if depth < (goal - 0.5):
		thrusters.up()
	elif depth > (goal + 0.5):
		thrusters.down()
	else:
		thrusters.hover()
