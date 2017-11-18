# -*- coding: utf-8 -*-

# imports
import cv2, helper, filters, imutils, ShapeDetector;
import visual_input as vi;
import visual_output as vo;
import numpy as np;


def cell_detect_via_contours(frame):
    
    resize_ratio, processedframe1 = filters.applyPrimaryFilteringOnImage(frame);
    cnts = cv2.findContours(processedframe1.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE);
    cnts = cnts[0] if imutils.is_cv2() else cnts[1];
    sd = ShapeDetector.ShapeDetector();
    for c in cnts:
    	shape = sd.detect(c);
        #cv2.drawContours(frame, [c], -1, (255, 255, 255), 2);
        M = cv2.moments(c);
        cY = cX = 0
        try:
            cX = int(((M["m10"] / M["m00"]))* resize_ratio);
            cY = int(((M["m01"] / M["m00"]))* resize_ratio);
        except:
            pass;
        if len(c) > 20:
            cv2.circle(frame, (cX,cY), 6,(0,255,0),-1);
            cv2.circle(frame, (cX,cY), int(np.linalg.norm((cX,cY)-max(c[0]))),(255,255,0),2);
            print max(c[0]);

    return frame
        

#end
