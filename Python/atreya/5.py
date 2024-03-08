prison=["C","C","C","C","C","C","C","C","C","C"]
print(prison)
for i in range(0,10,1):
    prison[i]="O"
print(prison)
for i in range(1,10,2):
    prison[i]="C"
print(prison)
for j in range(2,10,1):
    
    for i in range(j,10,j+1):
        if prison[i]=="C":
            prison[i]="O"
        else:
            prison[i]="C"
    print(prison)
for i in range(0,10,1):
    if prison[i]=="O":
        print("Prisoner "+str(i+1)+" is lucky")
