# -*- coding: utf-8 -*-

# imports
import cv2, helper, filters;
import visual_input as vi;
import visual_output as vo;


def main():
    vi.getCamera();
    while True:
        # getting image
        helper.printDebugMsg(" > Getting Frame.");
        frame = vi.getFrame();

        #processing image
        helper.printDebugMsg(" > Processing Frame.");
        greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
        frame = filters.avgFilter(greyframe);
        guassianframe = filters.medianBlur(greyframe, 5);
        
        #showing image
        helper.printDebugMsg(" > Showing Frame.");
        processedframe = helper.convertToJPEG(frame);
        greyframe = helper.convertToJPEG(greyframe)
        processedframe1 = helper.convertToJPEG(guassianframe);
        vo.showFrame(greyframe, "imageText_orignal.txt");
        vo.showFrame(processedframe, "imageText_processed.txt");
        vo.showFrame(processedframe1, "imageText_processed1.txt");
#end


try:
    main();
except ValueError as err:
    print(err.args)