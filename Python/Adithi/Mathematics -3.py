# Input  a number from txt file
# Python file and the txt file should be put into a single directory
with open("in.txt" , "r") as file:
    a = int(file.readline())
    b = int(file.readline())
for i in range ( a, b+1):
     print(i , "Table")
     for j in range (1, 11):
         print(i , "*" ,  j , "=" , i*j)
