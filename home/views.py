from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# các thử đăng ký
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms2 import SignUpForm2

# def index(request):
#     respone = HttpResponse()
#     respone.writelines('<h1>Xin chào</h1>')
#     respone.write('đây là app home')
#     return respone


def index(request):
    # reverse('logout') đã bằng với {% url 'logout' %}
    logout_url = reverse(
        "logout"
    )  # 'logout' là tên của URL pattern của trang đăng xuất
    signup2_url = reverse("signup2")
    login_url = reverse("login")
    return render(
        request,
        "pages/home.html",
        {"logout_url": logout_url, "signup2_url": signup2_url, "login_url": login_url},
    )


def contact(request):
    return render(request, "pages/contact.html")


def error_404(request, exception):
    return render(request, "pages/error_404.html", {"message": "Không tìm thấy trang"})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(
                "home"
            )  # Thay 'home' bằng đường dẫn đến trang chính của bạn
    else:
        form = SignUpForm()
    return render(request, "pages/signup.html", {"form": form})


def signup2(request):
    if request.method == "POST":
        form = SignUpForm2(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(
                "home"
            )  # Thay 'home' bằng đường dẫn đến trang chính của bạn
    else:
        form = SignUpForm2()
    return render(request, "pages/signup2.html", {"form": form})


# def error_500(request, exception=None):
#     return render(request, "pages/error_500.html", {})


# Create your views here.
