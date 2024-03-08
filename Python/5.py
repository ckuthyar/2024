def calc1(n1,n2):
    num1=n1
    num2=n2
    sum1=num1+num2
    dif1=num1-num2
    prd1=num1*num2
    print(sum1,dif1,prd1)
 
f1=open("input2.txt", "r")
info1=f1.readline().replace("\n","")
list1=info1.split(",")
print(info1)
print(list1)
