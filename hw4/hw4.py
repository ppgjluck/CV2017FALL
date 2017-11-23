import cv2
import argparse
import numpy as np

# construct the argument parse
ap = argparse.ArgumentParser()
ap.add_argument("image", help="path to the input image")
args = ap.parse_args()


def dilation(img, kernel):
    i_dia = np.zeros(img.shape, np.int)
    (iH, iW) = img.shape[:2]
    (kH, kW) = kernel.shape[:2]
    for i in range(kW/2, iW-kW/2):
        for j in range(kH/2, iH-kH/2):
            if img[j,i] > 0:
                for ki in range(kW):
                    for kj in range(kH):
                        if kernel[kj,ki] != 0:
                            i_dia[j-kH/2+kj, i-kW/2+ki] = kernel[kj,ki]
    return i_dia


def erosion(img, kernel):
    i_ero = np.zeros(img.shape, np.int)
    (iH, iW) = img.shape[:2]
    (kH, kW) = kernel.shape[:2]
    for i in range(kW/2, iW-kW/2):
        for j in range(kH/2, iH-kH/2):
            flag = False
            if img[j,i] == kernel[kH/2,kW/2]:
                flag = True
                for ki in range(kW):
                    for kj in range(kH):
                        if img[j-kH/2+kj, i-kW/2+ki] != kernel[kj,ki] and \
                           kernel[kj,ki] > 0:
                            flag = False
                            break
            if flag:
                i_ero[j,i] = 255
    return i_ero

def opening(img, kernel):
    return dilation(erosion(img, kernel),kernel)

def closing(img, kernel):
    return erosion(dilation(img, kernel),kernel)

def hnm(img,j,k):
    i_c = -img + 255
    ij = erosion(img, j)
    ik = erosion(i_c, k)
    i_hnm = ((ij + ik)/2 == 255) * 255
    return i_hnm


def main():
    img = cv2.imread(args.image,0)
    kernel = np.array((
                       [0,255,255,255,0],
                       [255,255,255,255,255],
                       [255,255,255,255,255],
                       [255,255,255,255,255],
                       [0,255,255,255,0]), dtype="int")
    i_dia = dilation(img, kernel)
    cv2.imwrite("lena_dia.png", i_dia)
    i_ero = erosion(img, kernel)
    cv2.imwrite("lena_ero.png", i_ero)
    i_ope = opening(img, kernel)
    cv2.imwrite("lena_ope.png", i_ope)
    i_clo = closing(img, kernel)
    cv2.imwrite("lena_clo.png", i_clo)

    j = np.array((
                  [0,0,0],
                  [255,255,0],
                  [0,255,0]), dtype="int")
    k = np.array((
                  [0,255,255],
                  [0,0,255],
                  [0,0,0]), dtype="int")
        
    i_hnm = hnm(img, j, k)
    cv2.imwrite("lena_hnm.png", i_hnm)

if __name__ == '__main__':
    main()



