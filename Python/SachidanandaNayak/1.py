num1=3
num2=10
diff=num2-num1

for j in range(0,diff,1):
    output=""
    for i in range(1,11,1):
        info1=str(num1+j)+"*"+str(i)+"="+str((num1+j)*i)
        print(info1)
        output=output+info1+"\n"

    s1=".txt"
    fname=str(num1+j)+s1
    f1=open(fname,"w")
    f1.write(output)
    f1.close()
    print()
    

