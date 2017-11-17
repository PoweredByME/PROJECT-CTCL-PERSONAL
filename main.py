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


def main():
    
    #variables
    resizedFrameWidth = 300;
    cannyEdgeDetector_minVal = 90;
    cannyEdgeDetector_maxVal = 200;
    orignal = frame = processedframe1 = processedframe = None;

    vi.getCamera();
    while True:
        # getting image
        helper.printDebugMsg(" > Getting Frame.");
        frame = vi.getFrame();

        #processing image
        helper.printDebugMsg(" > Processing Frame.");
        orignal = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
        orignal = filters.gaussianBlur(orignal);
        orignal = cv2.adaptiveThreshold(orignal,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        processedframe = cv2.Canny(filters.gaussianBlur(orignal),180,200);
        orignal = processedframe1 = filters.avgFilter(processedframe, (29,29));
        ret,processedframe1 = cv2.threshold(processedframe1,68,255,cv2.THRESH_BINARY)
        cnts = cv2.findContours(processedframe1.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE);
        cnts = cnts[0] if imutils.is_cv2() else cnts[1];
        sd = ShapeDetector.ShapeDetector();
        for c in cnts:
    	    shape = sd.detect(c);
            #cv2.drawContours(frame, [c], -1, (255, 255, 255), 2);
            M = cv2.moments(c);
            cY = cX = 0
            try:
                cX = int((M["m10"] / M["m00"]));
                cY = int((M["m01"] / M["m00"]));
            except:
                pass;
            if len(c) > 20:
                cv2.circle(frame, (cX,cY), 6,(0,255,0),-1);
                cv2.circle(frame, (cX,cY), int(np.linalg.norm((cX,cY)-max(c[0]))),(255,255,0),2);
                print max(c[0]);

        processedframe1 = frame;
        
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







'''
        orignal = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
        im = resizedFrame = imutils.resize(orignal, width=resizedFrameWidth);
        resize_ratio = frame.shape[0]/float(resizedFrame.shape[0]); print("resize_ratio = " + str(resize_ratio));
        kernel = np.array([[-1,-1,-1], [-1,18,-1], [-1,-1,-1]])
        im = cv2.filter2D(im, -1, kernel)
        blurredFrame = filters.medianBlur(resizedFrame);
        
        processedframe = thresholdedFrame = cv2.Canny(blurredFrame,cannyEdgeDetector_minVal,cannyEdgeDetector_maxVal);
        #circles = cv2.HoughCircles(thresholdedFrame,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
        

        cnts = cv2.findContours(thresholdedFrame.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE);
        cnts = cnts[0] if imutils.is_cv2() else cnts[1];
        sd = ShapeDetector.ShapeDetector();
        for c in cnts:
    	    shape = sd.detect(c);
            c = c.astype("float");
            c *= resize_ratio;
            c = c.astype("int");
            cv2.drawContours(frame, [c], -1, (255, 255, 255), 2);


        
        processedframe1 = frame;
        
        circles = cv2.HoughCircles(orignal,cv2.HOUGH_GRADIENT,20,300,param1=50,param2=30,minRadius=0,maxRadius=300);
        
        try:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                resize_ratio = 1;
                cv2.circle(frame,(i[0] * resize_ratio,i[1] * resize_ratio),i[2] * resize_ratio,(0,255,0),2)
                cv2.circle(frame,(i[0] * resize_ratio,i[1] * resize_ratio),2,(0,0,255),3)
                frame = processedframe1;
        except:
            pass;




        
'''