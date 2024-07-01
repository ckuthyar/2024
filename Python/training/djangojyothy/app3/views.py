from django.shortcuts import render
def home(request):
    temp=evenodd()
    list1=temp[0]
    list2=temp[1]
    return render(request,"app4/index.html",{'param1':list1,'param2':list2})
# Create your views here.de
def evenodd():
    list1=[]
    list2=[]
    for i in range(0,10,2):
        list1.append(i)
        list2.append(i+1)
    return (list1,list2)


