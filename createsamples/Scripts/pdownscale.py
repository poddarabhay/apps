import cv2
import os

for filename in os.listdir('pos'):
        image = cv2.imread('pos/'+filename)
        image=cv2.resize(image,(50,50))
        cv2.imwrite('pos/'+filename,image)
        cv2.waitKey(0)
