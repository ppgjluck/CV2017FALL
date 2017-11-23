import cv2
import argparse
import matplotlib.pyplot as plt

# construct the argument parse
ap = argparse.ArgumentParser()
ap.add_argument("image", help="path to the input image")
args = ap.parse_args()

# load input image
img = cv2.imread(args.image,0)

(iH, iW) = img.shape[:2]

# create a list with all value 0
l = list()
l = [0]*256

for i in range(iH):
    for j in range(iW):
        l[img[i,j]] += 1

plt.plot(l)
plt.show()



