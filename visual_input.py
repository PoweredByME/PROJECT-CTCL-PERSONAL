# -*- coding: utf-8 -*-

#   imports
import helper;
import cv2;

#   global variables
cam = 0;

#   Function gets access of the camera.
def getCamera():
    global cam;
    cam = cv2.VideoCapture("experimentalVideos/vid2.mp4");
    #cam = cv2.VideoCapture("experimentalVideos/vid2.mp4");
    #cam = cv2.VideoCapture(0);
#end
   
#   Function gets the video frames from the already 
#   accessed camera.
#   -------------------------------------------------
#   OUTPUT : Raw Image Matrix
def getFrame():
    global cam;
    ret_val, img = cam.read();
    if ret_val == True:
        return img
    else:
        helper.throwException("visual_input.py -> def getFrame -> ERROR : Frame is not accessed.");
#end

def getTemplateImage():
    return cv2.imread("web_test_visual_output/sel_image.png", cv2.IMREAD_COLOR);
#end
