def show1():
    print("Please book your slot")
    for i in range(0,6,1):
        if(status[i]==1):
            status1=" Booked"
        else:
            status1=" Free"
        slot1=slots[i]
        pos1=int(slot1[0:2])
        day1=days[pos1-1]
        time1=slot1[2:6]
        s1=str(i+1)+"."+day1+"-"+time1+"-"+status1
        print(s1)

slots=["050900","050930","051000","051030","051100","051130",]
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
status=[0,1,0,0,0,0]

show1()

bkg=False
inslot1=int(input())
if status[inslot1-1]==1:
    bkg=True

while(bkg==True):
    print("wrong input, enter again")
    inslot1=int(input())
    if status[inslot1-1]==1:
        bkg=True
    else:
        bkg=False

pos2=inslot1-1
status[pos2]=1
show1()
