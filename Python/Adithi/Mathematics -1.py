# Tables from 3 to 20
a = 3
b = 20
for i in range ( a, b+1):
     print(i , "Table")
     for j in range (1, 11):
         print(i , "*" ,  j , "=" , i*j)
#We should nest the second for loop for an appropriate output
