import cv2 as cv
import numpy as np
img1=cv.imread("row1.jpg")
img2=cv.imread("row2.jpg")
img3=cv.imread("row3.jpg")
vstack1=np.vstack([img1,img2,img3])
cv.imwrite("leaders.jpg",vstack1)
cv.imshow("temp",vstack1)

