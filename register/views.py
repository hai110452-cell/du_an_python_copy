from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Đăng ký thành công! Bạn có thể đăng nhập ngay.")
            return redirect("login")  # 'login' là tên URL đăng nhập
        else: print(form.errors)
        
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})


