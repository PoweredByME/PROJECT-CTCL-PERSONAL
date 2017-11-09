# -*- coding: utf-8 -*-
import cv2;

# Throws Exceptions in the best practice manner.
def throwException(*args):
    raise ValueError(args);

# Converts the raw image to JPEG formate.
def convertToJPEG(raw_image):
    ret, buf = cv2.imencode(".jpg", raw_image);
    if ret == True:
        return buf;
    else:
        throwException("visual_input.py -> def getFrame -> ERROR : Frame did not convert to jpeg.");