#Built-in libs
import numpy as np
import cv2
import argparse
import math
from matplotlib import pyplot as plt

#Built-out libs
import myImage
import filter as flt
import harris
import mysift
import blob

def main():
    #Measure time
    e1 = cv2.getTickCount()

    # input gray image
    grayImg = myImage.readImage("empire.jpg")
    
    # Convert img in range[0,1]
    floatImg = grayImg / 255.0

    # # Call harris detector function
    # harris.detectByHarris(floatImg)
    
    # # Detect Blob used LoG
    # # Declare CBlob obj
    # myblob = blob.CBlob()
    # myblob.detectBlobByLoG(floatImg)
    # myblob.plotBlob(floatImg)

    # # Detect Blob used DoG
    # # Declare sift obj
    # mySift = sift.CSift(floatImg)
    # mySift.detectBlobByDoG()
    # mySift.plotBlob()
    
    # Sift detector
    # Declare sift obj
    mySift = mysift.CSift(floatImg)
    mySift.detectBySift()

    e2 = cv2.getTickCount()
    time = (e2 - e1)/cv2.getTickFrequency()
    print('Time: %.2f(s)' %(time))

    plt.show()


if __name__ == "__main__":
    main()