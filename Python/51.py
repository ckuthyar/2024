def diamond3(s1):
    len1=len(s1)
    len2=len1//2
    str1=""
    for i in range(0,len2,1):
        spaces=" "*(len2-i)
        str1=str1+spaces
        str1=str1+s1[0:(2*i)+1]+"\n"
    return str1

f1=open("names4.txt","r")
f2=open("names4_out.txt","w")
for i in range(0,6,1):
    name1=f1.readline()
    result=diamond3(name1)
    print(result)
    f2.write(result)
    f2.write("\n")
f2.close()

