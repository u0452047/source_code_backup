import os
import numpy as np
from numpy import random
import cv2


def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def posprocess(img):
    kernel = np.ones((2,2),np.uint8)
    (T, img) = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, kernel, iterations=2)
    img = cv2.dilate(img, kernel, iterations=8)
    return img

def filter_c(img):  
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
    for i in range(0, num_labels):
        if stats[i][4]<400:
            xi,yi,wi,hi=stats[i][0],stats[i][1],stats[i][2],stats[i][3]
            img2 =img [yi:yi+hi, xi:xi+wi]
            img[yi:yi+hi, xi:xi+wi]=img2*np.zeros(img2.shape)
    
    return img


def cut_image(x,img):
    bbox_x = int(x[0])
    bbox_y = int(x[1])
    bbox_w = abs( int(x[0]) - int(x[2]) )
    bbox_h = abs( int(x[1]) - int(x[3]) )
    img2 = img[ bbox_y:bbox_y+bbox_h , bbox_x:bbox_x+bbox_w ]
    img[ bbox_y:bbox_y+bbox_h , bbox_x:bbox_x+bbox_w ] = img2*np.zeros(img2.shape)