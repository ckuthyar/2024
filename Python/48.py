def diamond3(s1):
    len1=len(s1)
    len2=(len1//2)
    for i in range(0,len2+1,1):
        spaces=" "*(len2-i)
        print(spaces,end="")
        print(s1[0:(2*i)+1])
    print()
diamond3("Kishan")
diamond3("Rahul")
diamond3("Rohit")
diamond3("Sudheera")
diamond3("ChandrashekarRaoKuthyar")
