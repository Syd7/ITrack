from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # basic validation
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("user_management:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("user_management:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("user_management:register")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Account created successfully!")
        return redirect("login")  
    # GET request
    return render(request, "user_management/register.html")
