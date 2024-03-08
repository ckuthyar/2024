import cv2 as cv   #computer vision

img1=cv.imread(str(11)+".jpg")
img1=cv.resize(img1,(200,300))

img2=cv.imread(str(12)+".jpg")
img2=cv.resize(img2,(200,300))

img3=cv.imread(str(13)+".jpg")
img3=cv.resize(img3,(200,300))

img4=cv.imread(str(14)+".jpg")
img4=cv.resize(img4,(200,300))

img5=cv.imread(str(1)+".jpg")
img5=cv.resize(img5,(200,300))

row3=cv.hconcat((img1,img2,img3,img4,img5))
cv.imwrite("row3.jpg",row3)
cv.imshow("temp",row3)


