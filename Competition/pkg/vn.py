from vnpy import *
from math import atan2, pi
from . import thrusters



def sign(num):
	if num < 0:
		pos = 360 + num
	else:
		pos = num
	return pos
	


def direction(head, x, c):
	if x > (head + 10):
		thrusters.left()
		state = "L"
	elif x < (head - 10):
		thrusters.right()
		state = "R"
	else:
		thrusters.forward(c)
		state = "F"

	return state
	


# reads the sensor		
def orient():
	orientation = s.read_yaw_pitch_roll()
	x = sign(orientation.x)
	
	return x
	


