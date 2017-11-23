import numpy as np
import cv2
import argparse

# construct the argument parse
ap = argparse.ArgumentParser()
ap.add_argument("image", help="path to the input image")
args = ap.parse_args()

# load input image
img = cv2.imread(args.image,0)

(iH, iW) = img.shape[:2]

# set threshold
threshold = 128


b = np.zeros(img.shape, np.uint8)
for i in range(iW):
    for j in range(iH):
        if img[i,j] >= 128:
            b[i,j] = 255
        else:
            b[i,j] = 0

cv2.imshow("binarize", b)
cv2.imwrite("binarize.png", b)
cv2.waitKey(0)

