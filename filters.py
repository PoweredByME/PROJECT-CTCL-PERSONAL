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

# This function does the bilateral Filtering on the image via the
# cv2.bilateralFilter(frame, kernel_size = 9, sigmaColor = 75, signalSpace = 75)
# ------ Information ------
# cv2.bilateralFilter() is highly effective in noise removal while keeping edges sharp. 
# But the operation is slower compared to other filters. We already saw that gaussian filter takes 
# the a neighbourhood around the pixel and find its gaussian weighted average. This gaussian filter 
# is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't 
# consider whether pixels have almost same intensity. It doesn't consider whether pixel is an edge 
# pixel or not. So it blurs the edges also, which we don't want to do.
#Bilateral filter also takes a gaussian filter in space, but one more gaussian filter which is a function of pixel difference. Gaussian function of space make sure only nearby pixels are considered for blurring while gaussian function of intensity difference make sure only those pixels with similar intensity to central pixel is considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.
def bilateralFilter(frame, kernel_size = 9, sigmaColor = 75, signalSpace = 75):
    return cv2.bilateralFilter(frame, kernel_size, sigmaColor, signalSpace);
#end

# Apply sobel operator (derivative wrt y-axis) on image.
def sobelY(frame, kernel_size = 5):
    return cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=kernel_size);

# Apply sobel operator (derivative wrt x-axis) on image.
def sobelX(frame, kernel_size = 5):
    return cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=kernel_size);


#Laplacian can be used directly by:
#guassianframe = cv2.Laplacian(filters.gaussianBlur(greyframe), cv2.CV_32F, 5,5);
def laplacian(frame):
    return cv2.Laplacian(frame, cv2.CV_32F, 5,5);
#end

