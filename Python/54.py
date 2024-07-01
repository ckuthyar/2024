def genOutFile(fname1):
    list1=fname1.split(".")
    fname2=list1[0]+ "_out." + list1[1]
    return fname2

print(genOutFile("hello.csv"))
