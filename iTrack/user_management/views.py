from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print("Submitted Username:", username)
        print("Submitted Email:", email)
        print("Submitted Password1:", password1)
        print("Submitted Password2:", password2)

        # basic validation
        if password1 != password2:
            print("Passwords do not match")
            messages.error(request, "Passwords do not match")
            return redirect("user_management:register")

        if User.objects.filter(username=username).exists():
            print("Username already taken")
            messages.error(request, "Username already taken")
            return redirect("user_management:register")

        if User.objects.filter(email=email).exists():
            print("Email already registered")
            messages.error(request, "Email already registered")
            return redirect("user_management:register")

        # create user (password hashed automatically)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        print("User created successfully:", user)

        messages.success(request, "Account created successfully!")
        return redirect("dashboard:login")

    # GET request
    print("Rendering registration page (GET request)")
    return render(request, "user_management/register.html")
