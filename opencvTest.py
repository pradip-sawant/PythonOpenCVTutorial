import cv2 #computer vision
import numpy

img= cv2.imread("resources/DSC_0163.jpg")

cv2.imshow("Lena",img)

cv2.waitKey(0)