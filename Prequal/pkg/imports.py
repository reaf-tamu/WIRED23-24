import sys
import os

def pings():
	# Add the external package folder to the system path
	external_packages_path = os.path.abspath("/Home/AUV/ping-python")
	if external_packages_path not in sys.path:
	    sys.path.insert(0, external_packages_path)

# Now you can import the module
from my_package import my_module

# Use the module
my_module.some_function()

