# USAGE
# python deep_learning_with_opencv.py --image images/jemma.png --prototxt bvlc_googlenet.prototxt --model bvlc_googlenet.caffemodel --labels synset_words.txt

# import the necessary packages
import cv2
import os

for filename in os.listdir('neg'):
        image = cv2.imread('neg/'+filename)
        image=cv2.resize(image,(100,100))
        cv2.imwrite('neg/'+filename,image)
        cv2.waitKey(0)
