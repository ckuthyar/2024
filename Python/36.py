count=10
lucky=[]
prison=["C"]*count
#print(prison)

for i in range(0,count,1):
    prison[i]="O"
#print(prison)

for i in range(1,count,2):
    prison[i]="C"
#print(prison)

for j in range(2,10,1):
    
    for i in range(j,count,j+1):
        if prison[i]=="C":
            prison[i]="O"
        else:
            prison[i]="C"
    #print(prison)






print(prison)

for i in range(0,count,1):
    if(prison[i]=="O"):
        lucky.append(i+1)
print(lucky, "are the lucky prisoners")
