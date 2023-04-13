from django.shortcuts import render,redirect
from django.http import HttpResponse
from .EmailBackend import EmailBackend
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def base(request):
    return render(request,'index.html')
def log(request):
    return render(request, 'login.html')
def Dologin(request):
    if request.method== "POST" :
        user=EmailBackend.authenticate(request,username=request.POST.get('email'),
                                       password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            user_type= user.user_type
            if user_type == '1':
                return HttpResponse('This is HOD panel')
            elif user_type == '2':
                return HttpResponse('This is Staff panel')
            elif user_type == '3':
                return HttpResponse('This is Student panel')
            else:
                messages.error(request, 'Invalid User')
                return redirect ('log')
        else:
                messages.error(request, 'Invalid User')
                return redirect ('log')
    else:
      return redirect ('log')