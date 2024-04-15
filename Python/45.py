list1=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
list2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list3=["ABCD",]
list4=[]

for word1 in list3:
    s2=""
    for letter1 in word1:
        pos1=list2.index(letter1)
        s2=s2+list1[pos1]
    list4.append(s2)
print(list4)

    
