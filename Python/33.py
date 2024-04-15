
list1=["madam", "hello", "list", "programming", "malayalam","rabbit","mam","noon","deified", "wow"]
len1=len(list1)
for i in range(0,len1,1):
    
    s1=list1[i]
    s2=s1[::-1]
    if(s1==s2):
        print(s1+" is a palindrome")
