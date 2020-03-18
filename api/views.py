from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,authenticate,logout
from .forms import UserAuthenticationForm,RegistrationForm
from .models import Users
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email,password=raw_password)
            login(request,user)
            return redirect('home')
        else:
            context['registration_form']=form
    return render(request, 'api/register.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    context ={}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)

            if user:
                login(request,user)
                return redirect("home")
    else:
        form = UserAuthenticationForm
    context['login_form'] = form

    return render(request,'api/login.html',context)

def change_password(request):
    if request.POST:
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect(reverse('api:profile'))
        else:
            return redirect(reverse('api:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form':form}
        return render(request,'api/change_password.html',args)


def view_profile(request,pk=None):
    if pk:
        user = Users.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user':user}
    return render(request,'api/profile.html',args)

