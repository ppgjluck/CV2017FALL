import numpy as np
import cv2
import argparse

# construct the argument parse
ap = argparse.ArgumentParser()
ap.add_argument("image", help="path to the input image")
args = ap.parse_args()

# load input image
img = cv2.imread(args.image)

(iH, iW) = img.shape[:2]

# rotate 45
M = cv2.getRotationMatrix2D((iW/2,iH/2),45,1)
output = cv2.warpAffine(img,M,(iW,iH))
cv2.imshow("rotation", output)
cv2.imwrite("rotation.png", output)
cv2.waitKey(0)

#shrink
output1 = cv2.resize(img,None,fx=0.5,fy=0.5, interpolation = cv2.INTER_AREA)
cv2.imshow("rotation", output1)
cv2.imwrite("rotation.png", output1)
cv2.waitKey(0)


#binarize
bimg = cv2.imread(args.image,0)
thresh = 128
maxValue = 255
th, output2 = cv2.threshold(bimg, thresh, maxValue, cv2.THRESH_BINARY);
cv2.imshow("binarize", output2)
cv2.imwrite("binarize.png", output2)
cv2.waitKey(0)
