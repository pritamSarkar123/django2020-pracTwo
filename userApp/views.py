from django.shortcuts import render, redirect
from . forms import UserProfileInfoForm, UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'userApp/index.html')


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'userApp/index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'userApp/home.html')
            else:
                return render(request, 'userApp/login.html', {'active_status': 'Account Not Active'})
        else:
            return render(request, 'userApp/login.html', {'login_status': 'Username or Password is wrong retype'})
    else:
        return render(request, 'userApp/login.html', {})


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # manipulating password
            user = user_form.save()
            # apply encrypting algo
            # or hashing the password
            user.set_password(user.password)
            user.save()
            # manipulating other profile
            profile = profile_form.save(commit=False)
            profile.user = user  # the one to one relation ship
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'userApp/registration.html', {'registered': registered,
                                                         'user_form': user_form,
                                                         'profile_form': profile_form})
