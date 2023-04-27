from django.shortcuts import render,HttpResponseRedirect
from app1.forms import SignupForm,UpdateuserprofileForm,UpdateadminprofileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request,'app1/index.html',{'msg':'This is Index Page'})

def signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'REGISTERED SUCCESSFULLY')
    else:
        form = SignupForm()
    return render(request,'app1/signup.html',{'form':form})

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'LOGGED IN SUCCESSFULLY')
                    return HttpResponseRedirect('/app1/profile')
        else:
            form = AuthenticationForm()
        return render(request,'app1/login.html',{'form':form})    
    else:
        return HttpResponseRedirect('/app1/profile')
    

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/app1/login')

def Profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            users=None
            form = UpdateuserprofileForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'PROFILE UPDATED SUCCESSFULLY')
        else:
            if request.user.is_superuser == True:
                form = UpdateadminprofileForm(instance=request.POST)
                users = User.objects.all()
            else:
                form = UpdateuserprofileForm(instance=request.user)
                users =None
        context = {'msg':'WELCOME TO YOUR PROFILE','user':request.user,'form':form,'users':users} 
        return render(request,'app1/profile.html',context) 
    else:
        return HttpResponseRedirect('/app1/login')    

def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'YOUR PASSWORD HASS BEEN CHANGED')
                return HttpResponseRedirect('/app1/login')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'app1/cp.html',{'form':form})
    else:
        return HttpResponseRedirect('/app1/login')

            
def changepassword2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'YOUR PASSWORD HASS BEEN CHANGED')
                return HttpResponseRedirect('/app1/profile')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'app1/cp.html',{'form':form})
    else:
        return HttpResponseRedirect('/app1/login')

            
