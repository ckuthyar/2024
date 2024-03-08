
def diff1(list6,list7):
    len6=len(list6)
    list1=[]
    for i in range(0,len6,1):
        item1=list6[i]
        item2=list7[i]
        if(item1!=item2):
            list1.append(i+1)
    return list1



list3=[2,4,6]
list4=[2,4,8]
list2=diff1(list3,list4)
print(list2)
