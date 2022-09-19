
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')   



def setting(request):
    return  HttpResponse('hello setting page')

def add(request):
    n1=int(request.POST['n1'])
    n2=int(request.POST['n2'])
    res=n1+n2
    return render(request,'result.html',{'sum':res} )


       