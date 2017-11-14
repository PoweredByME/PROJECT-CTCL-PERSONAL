# -*- coding: utf-8 -*-

#imports
import cv2, base64;

#   This function shows the Frames of the video feed.
#   NOTE : For the local development on my MAC I have made a 
#   web interface which creates a huge overhead but I had no 
#   choice.
#   ----------------------------------------------------------
#   INPUT : 
#       - Image in JPEG format
def showFrame(frame_jpeg, dst_file):
    b64String = base64.b64encode(frame_jpeg);
    file = open("web_test_visual_output/"+dst_file,"w");
    file.write(b64String);
    file.close();
#end