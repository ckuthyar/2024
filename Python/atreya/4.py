prison=["C","C","C","C","C","C","C","C","C","C"]
print(prison)
for i in range(0,10,1):
    prison[i]="O"
print(prison)
for i in range(1,10,2):
    prison[i]="C"
print(prison)

for i in range(2,10,3):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print(prison)
for i in range(3,10,4):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print(prison)
for i in range(4,10,5):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print(prison)
