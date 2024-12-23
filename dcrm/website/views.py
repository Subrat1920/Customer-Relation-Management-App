from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    ## checking to see if loggin in
    if request.method == 'POST':
        user_name = request.POST['first_name']
        user_password = request.POST['password']

        ## authenticating
        user = authenticate(request, username = user_name, password = user_password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged-in")
            return redirect('home', {})
        else:
            messages.success(request, 'Error in loggin, Please try again....')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass