#Find Mean,Standard Deviation of numbers input from user
list1=[]
variance1=0
qty=int(input("Enter quantity of numbers to be entered Eg. 5 "))
for i in range(0,qty,1):
    n1=int(input("Enter a number "))
    list1.append(n1)
print(list1)
sum1=sum(list1)
len1=len(list1)
avg1=sum1/len1

for i in range(0,qty,1):
    diff1= list1[i]-avg1
    variance1=variance1+diff1**2
stdev1=variance1**0.5
print(sum1,len1,avg1,stdev1)
#https://en.wikipedia.org/wiki/Standard_deviation
