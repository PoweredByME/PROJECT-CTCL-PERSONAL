###################################################################
# IN THE NAME OF ALLAH. I SWEAR HE REALLY IS THE ONE TRUE GOD AND #
# ONLY HE CAN CREATE THIS ENTIRE WORLD. WE CAN NEVER MIMIC HIS    #
# CREATIONS.                                                      #
# - Saad Ahmad -                                                  #
###################################################################

# -*- coding: utf-8 -*-

# imports
import cv2, helper, filters, imutils, ShapeDetector;
import visual_input as vi;
import visual_output as vo;
import numpy as np;
import cell_detect_via_contours as cdvc;
import cell_detect_via_blob as cdvb;

def main():
    
    #variables
    orignal = frame = processedframe1 = processedframe = None;

    vi.getCamera();
    while True:
        # getting image
        helper.printDebugMsg(" > Getting Frame.");
        orignal = frame = processedframe1 = processedframe = vi.getFrame();
        template = vi.getTemplateImage();


        #proxessing frame
        helper.printDebugMsg(" > Processing Frame.");
        dim, w,h = template.shape[::-1]

        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY);
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
        res = cv2.matchTemplate(frame,template,cv2.TM_SQDIFF);
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc;
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(processedframe,top_left, bottom_right, 255, 2)


        #showing image
        helper.printDebugMsg(" > Showing Frame.");
        orignal = helper.convertToJPEG(orignal)
        processedframe = helper.convertToJPEG(processedframe);
        processedframe1 = helper.convertToJPEG(processedframe1);
        vo.showFrame(orignal, "imageText_orignal.txt");
        vo.showFrame(processedframe, "imageText_processed.txt");
        vo.showFrame(processedframe1, "imageText_processed1.txt");

#end_main


try:
    main();
except ValueError as err:
    print(err.args)







''' (x,y),radius = cv2.minEnclosingCircle(c)
            center = (int(x * resize_ratio), int(y * resize_ratio));
            radius = int(radius * resize_ratio);
            if(radius > 70):
                cv2.circle(frame, center, 6,(0,255,0),-1);
                cv2.circle(frame, center, radius,(255,255,0),2);                

        orignal = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
        orignal = filters.gaussianBlur(orignal);
        orignal = cv2.adaptiveThreshold(orignal,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        processedframe = cv2.Canny(filters.gaussianBlur(orignal),180,200);
        orignal = processedframe1 = filters.avgFilter(processedframe, (29,29));
        ret,processedframe1 = cv2.threshold(processedframe1,68,255,cv2.THRESH_BINARY)
        

        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()
 
        # Filter by Area.
        params.filterByArea = True
        params.minArea = 100
 
        # Filter by Circularity
        params.filterByCircularity = True
        params.minCircularity = 0.1
 
 
        # Create a detector with the parameters
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3 :
            detector = cv2.SimpleBlobDetector(params)
        else : 
            detector = cv2.SimpleBlobDetector_create(params)

        keypoints = detector.detect(frame);
        print keypoints;
        processedframe = cv2.drawKeypoints(orignal, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


        
        
'''