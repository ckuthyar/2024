import cv2 as cv
import numpy as np


row=int(input("rows"))
col=int(input("colmnes"))
def func(b,c):
    list1=[]
    list2=[]
    for i in range(b,c-1,1):
        a=str(i)+".jpg"
        img1 = cv.imread(a)
        im1=cv.resize(img1,(400,400))
        list1.append(im1)
    img=np.hstack(list1)
    list2.append(img)
    return list2[0]

def read1():
    list3=[]
    list4=[]
    list5=[]
    d=1
    for i in range(0,row,1):
        list4.append(d)
        list5.append(list4[i]+col+1)
        d=d+col
    print(list4,list5)

    for i in range(0,row,1):
        lis=func(list4[i],list5[i])
        list3.append(lis)

    img2=np.vstack(list3)
    list3.append(img2)
    cv.imwrite("read.jpg",img2)
    cv.imshow("temp",img2)
read1()
cv.waitKey(0)
