from django.shortcuts import render,redirect
from .forms import UserForm


def showformdata(request):
    if request.method=="POST":
        fm=UserForm(request.POST)
        if fm.is_valid():
            try:
                return redirect('/')
            except :
                pass
    else:
        fm=UserForm()
    return render(request,'user/userreg.html',{'form':fm})
