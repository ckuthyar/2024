def diff2(fname1,fname2):
    def diff1(list6,list7):
        len6=len(list6)
        list1=[]
        for i in range(0,len6,1):
            item1=list6[i].replace("\n","")
            item2=list7[i].replace("\n","")
            if(item1!=item2):
                list1.append(i+1)
        return list1

    f1=open(fname1,"r")
    f2=open(fname2,"r")
    info6=f1.readlines()
    info7=f2.readlines()
    list1=diff1(info6,info7)
    len1=len(list1)

    for i in range(0,len1,1):
        item3=(info6[list1[i]-1])
        item4=(info7[list1[i]-1])
        list3=item3.replace("\n","").split(" ")
        list4=item4.replace("\n","").split(" ")
        list5=diff1(list3,list4)
        pos2=list5[0]-1
        print("Difference is in line",list1[i],"word",list5[0],list3[pos2],list4[pos2])

diff2("in6.txt","in7.txt")
