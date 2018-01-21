
import numpy as np
import argparse
import cv2
from skimage.color import rgb2gray
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"],0)
image=cv2.resize(image,(0,0), fx=0.25, fy=0.25)
img_gray = rgb2gray(image)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img_gray)
cl2 = np.hstack((img_gray,cl1))
cv2.imwrite(str(time.time())+".png",cl2)
cv2.imshow('image', img_gray)
cv2.waitKey(0)
