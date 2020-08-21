from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def signup(request):
    return render(request, 'accounts/signup.html')


def createuser(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['repeat_pass']

        # verify the password
        if len(username) > 20:
            messages.error(request, 'Username should not exceed 20 caharacters')
            return redirect(signup)
        if pass1 != pass2:
            messages.error(request, 'Password doesn\'t match')
            return redirect(signup)
        if not username.isalnum():
            messages.error(request, 'Username should contain only letters and numbers')
            return redirect(signup)

        # create the user
        my_user = User.objects.create_user(username, email, pass1)
        fname = name.split()[:1]
        lname = name.split()[1:]
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()

        return redirect(loginview)

    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


def loginview(request):
    return render(request, 'accounts/login.html')


def request_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        # authentication
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfuly Logged In")
            return redirect('/tasks')

        else:
            messages.error(request, "Invalid Username or Password. Try Again...")
            return redirect(login)
    else:
        return render(request, 'accounts/login.html')


def handlelogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Successfuly Logged Out")
    return redirect(signup)
