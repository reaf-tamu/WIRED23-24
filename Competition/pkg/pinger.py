from brping import Ping1D
# from . import thrusters


# connect to sensor
def ping_setup():
	myPing = Ping1D()
	myPing.connect_serial("/dev/ttyUSB1", 9600)

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
	if (depth < (goal - 25)):
		print("going up")
	elif (depth > (goal + 25)):
		print("going down")
		A2.setSpeed(70)
		A4.setSpeed(110)
		M2.setSpeed(110)
		M4.setSpeed(70)
		A2.run()
		A4.run()
		M2.run()
		M4.run()

	else:
		print("hovering")
		A2.setSpeed(71)
		A4.setSpeed(109)
		M2.setSpeed(109)
		M4.setSpeed(71)
		A2.run()
		A4.run()
		M2.run()
		M4.run()
