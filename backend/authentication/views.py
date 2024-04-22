from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages


# Create your views here.
def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in!")
                return redirect("index")
            else:
                messages.error(request, "Please check your username or password.")
        return render(request, "authentication/userLogin.html")
    return redirect("index")


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect("signin")
        return redirect("signin")
    return redirect("index")


@login_required(redirect_field_name="signin")
def signout(request):
    logout(request)
    messages.success(request, "You are now logged out!")
    return redirect("signin")


