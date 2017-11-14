# -*- coding: utf-8 -*-

# imports
import cv2, helper;
import numpy as np;

# This filter does the average filtering on the image
# using the cv2.blur(frame, kernel_size = (5,5)).
def avgFilter(frame, kernel_size = (5,5)):
    return cv2.blur(frame, kernel_size);
#end

# This function does the Gaussian Blurring of the image using
# cv2.GaussianBlur(frame, kernel_size = (5,5), sigmaX = 0, sigmaY = 0).
def gaussianBlur(frame, kernel_size = (5,5), sigmaX = 0, sigmaY = 0):
    if sigmaX == 0:
        return cv2.GaussianBlur(frame, kernel_size, sigmaX);
    else:
        return cv2.GaussianBlur(frame, kernel_size, sigmaX, sigmaY);
#end


# This function does the median blurring via the 
# cv2.medianBlur(frame, kernel_size = 5);
# ------ Information ------
# Here, the function cv2.medianBlur() takes median of all the pixels under kernel area and central element is
# replaced with this median value. This is highly effective against SALT AND PEPPER NOISE in the images. 
# Interesting thing is that, in the above filters, central element is a newly calculated value which may be a pixel
# value in the image or a new value. But in median blurring, central element is always replaced by some pixel value in the image. 
# It reduces the noise effectively. Its kernel size should be a positive odd integer.
def medianBlur(frame, kernel_size = 5):
    if kernel_size == 1 or kernel_size % 2 == 0:
        helper.throwException("Error : Invalid kernel_size for median blur. Must be > 1 and odd number");
    else:
        return cv2.medianBlur(frame, kernel_size);
#end

def bilateralFilter