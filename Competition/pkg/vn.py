from vnpy import *
from math import atan2, pi
from . import thrusters


"""
def sign(num):
	if num < 0:
		pos = 360 + num
	else:
		pos = num
	return pos
"""	


def direction(head, x, c):
	if head > 0:
		if x > (head + 5):
			state = "R"
		elif x < (head - 5):
			state = "L"
		else:
			state = "F"
	else:
		if x > (head + 5):
			state = "L"
		elif x < (head - 5):
			state = "R"
		else:
			state = "F"

	return state
	


# reads the sensor		
def orient(s):
	orientation = s.read_yaw_pitch_roll()
	x = orientation.x
	
	return x
	


