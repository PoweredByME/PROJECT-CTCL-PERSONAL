# -*- coding: utf-8 -*-

# imports
import cv2, helper, filters, imutils, ShapeDetector;
import visual_input as vi;
import visual_output as vo;
import numpy as np;

def cell_detect_via_blob(frame):
    resize_ratio, orignal = filters.applyPrimaryFilteringOnImage(frame,last_thresh_min = 40);
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1
    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector()
    else : 
        detector = cv2.SimpleBlobDetector_create()

    keypoints = detector.detect(orignal);
    print keypoints;
    processedframe = cv2.drawKeypoints(orignal, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return processedframe;
