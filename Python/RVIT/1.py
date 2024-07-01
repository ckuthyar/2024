def getFact(limit):
    factorial=[]
    numbers=[]
    for j in range(1,limit+1,1):
        n1=j
        fact1=1
        for i in range(1,n1+1,1):
            fact1=fact1*i
        factorial.append(fact1)
        numbers.append(n1)
    return(factorial, numbers)
limit=8
result=getFact(limit)
for i in range(0,limit,1):
    print("Factorial of "+str(result[1][i])+" - "+str(result[0][i]))
    


