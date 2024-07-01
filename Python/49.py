def diamond3(s1):
    len1=len(s1)
    len2=len1//2
    str1=""
    for i in range(0,len2+1,1):
        spaces=" "*(len2-i)
        str1=str1+spaces
        str1=str1+s1[0:(2*i)+1]+"\n"
    return str1
result=diamond3("Pranatharthiharan")
print(result)
