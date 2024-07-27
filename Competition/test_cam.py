from pkg import cam, era

import cv2
import time
import numpy as np
from vnpy import *

camera, model = cam.cam_setup()

result, frame = camera.read()
results = cam.infer(frame, model)

camera.release()


camera, model = era.cam_setup()

result, frame = camera.read()
results = era.infer(frame, model)

camera.release()
