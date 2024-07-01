from django.shortcuts import render
def home(request):
    num=6
    fact=1
    for i in range (1,num,1):
        fact=fact*i

    return render(request,'factorial1/index.html',{'param1':fact})
# Create your views here.
