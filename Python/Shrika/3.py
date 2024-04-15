def lenstring2(file1):
    def lenstring1(word1):
        s1=word1
        len1=len(s1)
        print(len1,word1)
    f1=open(file1,'r')
    list1=[]
    for i in range(0,9,1):
        s2=f1.readline().replace('\n','')
        list1.append(s2)
        lenstring1(s2)
lenstring2('family1.txt')
print()
lenstring2('family2.txt')
print()
