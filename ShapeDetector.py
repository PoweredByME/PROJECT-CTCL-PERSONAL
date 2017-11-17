# -*- coding: utf-8 -*-
import cv2;

class ShapeDetector:

    def __init__(self):
        pass;
    #end

    def detect(self, c):
        shape = "undefined";
        peri = cv2.arcLength(c, True);
        approx = cv2.approxPolyDP(c, 0.04 * peri, True);
    #end

#end_class 