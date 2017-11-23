import cv2
import argparse
import numpy as np
import sys

# construct the argument parse
ap = argparse.ArgumentParser()
ap.add_argument("image", help="path to the input image")
args = ap.parse_args()

def h(b,c,d,e):
    if b == c and (d != b or e != b):
        return 'q'
    elif b == c and (d == b and e == b):
        return 'r'
    else:
        return 's'

def f(a1,a2,a3,a4):
    nr = 0;
    nq = 0;
    for a in [a1,a2,a3,a4]:
        if a == 'r':
            nr += 1
        elif a == 'q':
            nq += 1
    if nr == 4:
        return 5
    return nq


def yokoi(img):
    img_pad = np.zeros((img.shape[0]+2,img.shape[1]+2), np.int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_pad[i+1,j+1] = img[i,j]
    yokoi_num = np.zeros(img.shape, np.int)
    for i in range(1,img_pad.shape[0]-1):
        for j in range(1,img_pad.shape[1]-1):
            if img_pad[i,j] > 0:
                a1 = h(img_pad[i,j], img_pad[i,j+1], img_pad[i-1,j+1], img_pad[i-1,j])
                a2 = h(img_pad[i,j], img_pad[i-1,j], img_pad[i-1,j-1], img_pad[i,j-1])
                a3 = h(img_pad[i,j], img_pad[i,j-1], img_pad[i+1,j-1], img_pad[i+1,j])
                a4 = h(img_pad[i,j], img_pad[i+1,j], img_pad[i+1,j+1], img_pad[i,j+1])
                yokoi_num[i-1,j-1] = f(a1,a2,a3,a4)
    return yokoi_num

def main():
    img = cv2.imread(args.image,0)
    i_ds = np.zeros((64,64), np.int)
    for i in range(64):
        for j in range(64):
            i_ds[i,j] = img[8*i,8*j]
    cv2.imwrite("lena_bin_128_64*64.png", i_ds)

    yokoi_num = yokoi(i_ds)
    np.savetxt('lena_yokoi.txt', yokoi_num, '%d')

    s = open('lena_yokoi.txt').read().replace('0', ' ')
    open('lena_yokoi_final.txt','w+').write(s)


if __name__ == '__main__':
    main()



