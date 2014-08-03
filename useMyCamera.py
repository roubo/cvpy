#!/usr/bin/env python
# encoding: utf-8
"""
Just use my camera, do anything.
"""
import numpy as np
import cv2 as cv
import cv2.cv as cvold
import os
def openCameraWith(camindex, opfun):
    """
    open the camera with somethings
    something is opfun
    """
    cap = cv.VideoCapture(camindex)
    # get the loop out file
    out = []
    outfile = []
    for i in range(0,6):
        outName = "out"+str(i)+".avi"
        outfile.append(outName)
        outHandle = cv.VideoWriter(outName, cvold.CV_FOURCC(*'XVID'), 20.0, (640,480))
        out.append(outHandle)
    loopcount = 0
    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == True :
            if opfun == None:
                out[loopcount].write(frame)
                if os.path.getsize(outfile[loopcount]) >= 200000000 :
                    loopcount += 1
                # just show it
                cv.imshow('frame', frame)
                if cv.waitKey(1) & 0xff == ord('q'):
                    cap.release()
                    cv.destroyAllWindows()
                    break
            else:
                out[loopcount].write(frame)
                if os.path.getsize(outfile[loopcount]) >= 200000000 :
                    loopcount += 1
                # show it after opfun
                frame = opfun(frame)
                cv.imshow('frame', frame)
                if cv.waitKey(1) & 0xff == ord('q'):
                    cap.release()
                    cv.destroyAllWindows()
                    break
        else:
            cap.release()
            cv.destroyAllWindows()
            break
def detectMove():
    cap = cv.VideoCapture(1)
    fgbg = cv.BackgroundSubtractorMOG()
    while 1:
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        cv.imshow("frame",fgmask)
        if cv.waitKey(1) & 0xff == ord('q'):
            cap.release()
            cv.destroyAllWindows()
            break

if __name__ == '__main__':
#    openCameraWith(1, None)
    detectMove()
