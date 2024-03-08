import cv2 as cv
import numpy as np
img1=cv.imread("6.jpg")
img1=cv.resize(img1,(200,300))

img2=cv.imread("7.jpg")
img2=cv.resize(img2,(200,300))

img3=cv.imread("8.jpg")
img3=cv.resize(img3,(200,300))


img4=cv.imread("9.jpg")
img4=cv.resize(img4,(200,300))

img5=cv.imread("10.jpg")
img5=cv.resize(img5,(200,300))

hstack1=np.hstack([img1,img2,img3,img4,img5])
cv.imwrite("row2.jpg",hstack1)
cv.imshow("temp",hstack1)

