from vnpy import *
from math import atan2, pi


def sign(num):
	if num < 0:
		pos = 360 + num
	else:
		pos = num
	return pos
	

def direction(head, x):
	if x > (head + 10):
		thrusters.left()
	elif x < (head - 10):
		thrusters.right()
	

# reads the sensors		
def orient():
	orientation = s.read_yaw_pitch_roll()
	x = sign(orientation.x)
	
	return x
	
