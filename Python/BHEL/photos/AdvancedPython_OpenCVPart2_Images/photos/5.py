import cv2 as cv   #computer vision

img1=cv.imread("row1.jpg")
img2=cv.imread("row2.jpg")
img3=cv.imread("row3.jpg")
final=cv.vconcat((img1,img2,img3))

cv.imwrite("final.jpg",final)
cv.imshow("temp",final)


