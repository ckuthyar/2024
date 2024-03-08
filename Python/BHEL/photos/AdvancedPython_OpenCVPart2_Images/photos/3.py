import cv2 as cv   #computer vision

img1=cv.imread(str(6)+".jpg")
img1=cv.resize(img1,(200,300))

img2=cv.imread(str(7)+".jpg")
img2=cv.resize(img2,(200,300))

img3=cv.imread(str(8)+".jpg")
img3=cv.resize(img3,(200,300))

img4=cv.imread(str(9)+".jpg")
img4=cv.resize(img4,(200,300))

img5=cv.imread(str(10)+".jpg")
img5=cv.resize(img5,(200,300))

row2=cv.hconcat((img1,img2,img3,img4,img5))
cv.imwrite("row2.jpg",row2)
cv.imshow("temp",row2)


