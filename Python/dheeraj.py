names=[]
english=[]
f1=open("Marks.txt","r")
for i in range(0,26,1):
    
    info1=f1.readline()
    list1=info1.split(",")
    names.append(list1[0])
    temp=list1[3].split(":")
    english.append(temp[1])

print(names)
print(english)
