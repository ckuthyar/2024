import cv2 as cv   #computer vision
for i in range(1,14,1):
    

    img1=cv.imread(str(i)+".jpg")
    cv.imwrite("Image"+str(i)+".jpg",img1)

