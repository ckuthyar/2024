f1=open("family1.csv","r")
s2=""
for i in range(0,40,1):
    s1=f1.readline().replace("\n","")
    s2=s2+s1+","
print(s2)
