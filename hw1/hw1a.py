import numpy as np
import cv2
import argparse

# construct the argument parse
ap = argparse.ArgumentParser()
ap.add_argument("image", help="path to the input image")
args = ap.parse_args()

# load input image
img = cv2.imread(args.image)

# upside down
(iH, iW) = img.shape[:2]
udo = np.zeros(img.shape, np.uint8)
for i in range(iW):
    for j in range(iH):
        udo[j,i,0] = img[iH-j-1,i,0]
        udo[j,i,1] = img[iH-j-1,i,1]
        udo[j,i,2] = img[iH-j-1,i,2]


cv2.imshow("upside down", udo)
cv2.imwrite("upside down.png", udo)
cv2.waitKey(0)


#left side right
lro = np.zeros(img.shape, np.uint8)
for i in range(iW):
    for j in range(iH):
        lro[j,i,0] = img[j,iW-i-1,0]
        lro[j,i,1] = img[j,iW-i-1,1]
        lro[j,i,2] = img[j,iW-i-1,2]

cv2.imshow("left side right", lro)
cv2.imwrite("left side right.png", lro)
cv2.waitKey(0)


#diagonally mirrored
dmo = np.zeros(img.shape, np.uint8)
for i in range(iW):
    for j in range(iH):
        dmo[i,j,0] = img[j,i,0]
        dmo[i,j,1] = img[j,i,1]
        dmo[i,j,2] = img[j,i,2]

cv2.imshow("diagonally mirrored", dmo)
cv2.imwrite("diagonally mirrored.png", dmo)
cv2.waitKey(0)
