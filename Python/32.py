def palincheck5(str1):
    s1=str1
    c1=s1[0:1]
    c2=s1[1:2]
    c3=s1[2:3]
    c4=s1[3:4]
    c5=s1[4:5]
    if(c1==c5) and (c2==c4):
        print(s1+ " is a palindrome")



list1=["madam", "hello", "list", "programming", "malayalam"]
for i in range(0,5,1):
    
    str1=list1[i]
    len1=len(str1)
    if len1==5:
        palincheck5(str1)
