import datetime as dt
today=dt.datetime.now()
date1=str(today.year)+str(today.month).zfill(2)+str(today.day)
time1=str(today.hour)+str(today.minute)
votetime=(date1+"_"+time1)
f1=open("elections1.txt","r")
f2=open("results.txt","w")
list1=[]
list2=[]
list3=[]
for i in range(0,3,1):    
    s1=f1.readline()
    temp1=s1.split(":")
    list1.append(temp1[0])
    list2.append(temp1[1])
print("Elections will be held in")
for i in range(0,3,1):
    print(list1[i])
for i in range(0,3,1):
    loc1=input("Choose your constituency")
    pos1=list1.index(loc1)
    print("The candidates are ")
    print(list2[pos1])
    can1=input("Choose your candidate")
    f2.write(loc1+":"+can1+","+str(1)+","+votetime)
    f2.write("\n")
f2.close()




