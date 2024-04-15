def quiz1(fname):
    f1=open(fname)
    list2=[]
    list3=[]
    total=0
    for i in range(0,3,1):
        s1=f1.readline().replace('\n','')
        list1=s1.split(',')
        response1=input('what is the capital of '+list1[0]+': ')     
        if response1.lower()==list1[1]:
            total=total+10
        else:
            list2.append(list1[0])
            list3.append(list1[1])             
    print(total)
    len2=len(list2)
    for i in range(0,len2,1):
        print('The capital of '+list2[i]+' is '+list3[i])
quiz1('capitals.txt')
