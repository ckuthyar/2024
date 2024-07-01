from django.shortcuts import render 
def home(request):
   n=6
   fact1=1
   for  i in range(1,n,1):
        fact1=i*fact1
        return render(request,'app1/index.html',{'param1':fact1})
