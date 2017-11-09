# -*- coding: utf-8 -*-
import cv2, helper;
import visual_input as vi;
import visual_output as vo;


def main():
    vi.getCamera();
    while True:
        frame = vi.getFrame();
        frame = cv2.GaussianBlur(frame,(5,5),0);
        jpeg_frame = helper.convertToJPEG(frame);
        vo.showFrame(jpeg_frame);


try:
    main();
except ValueError as err:
    print(err.args)