start=int(input("enter the first number"))
end=int(input("enter the second number"))
for j in range(start,end+1,1):
    for i in range(1,11,1):
        print(j,i,j*i)
    print()
