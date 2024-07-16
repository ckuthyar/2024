import random
f1=open("dictionary.txt","r")
list1=[]
total1=[]
total2=[]
for i in range(0,58110,1):
    s1=f1.readline().replace("\n","")
    list1.append(s1)
len1=len(list1)

for i in range(0,3,1):
    list2=[]
    player_choice=input("Enter a word ") 
    last_letter=player_choice[-1]
    for i in range(0,len1,1):
        if list1[i][0]==last_letter:
            list2.append(list1[i])
    computer_choice=list2[0]
    marks1=len(player_choice)
    marks2=len(computer_choice)
    total1.append(marks1)
    total2.append(marks2)
    last_letter=computer_choice[-1]
    print(player_choice, computer_choice,marks1,marks2)

sum1=sum(total1)
sum2=sum(total2)
if total1>total2:
    print("Player has won with marks ",sum1)
elif total1<total2:
    print("Computer has won with marks ",sum2)
else:
    print("Player and Computer have got same marks ", sum1)




        
