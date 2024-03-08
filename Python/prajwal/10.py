f1=open("in2.txt","r")
f2=open("out1.txt","w")
info1=f1.readline().replace("\n","")
list1=info1.split(",")
print(info1)
print(list1)
start=int(list1[0])
end=int(list1[1])
for j in range(start,end+1,1):
    for i in range(1,11,1):
        
        info2=str(j)+" "+str(i)+" "+str(j*i)
        print(info2)
        f2.write(info2)
        f2.write("\n")
    print()
    f2.write("\n")
f2.close()
