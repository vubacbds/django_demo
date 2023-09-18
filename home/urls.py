from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact, name="contact"),
    # URL pattern cho xử lý lỗi 404
    path("404/", views.error_404, name="error_404"),
    path("signup/", views.signup, name="signup"),
    path("signup2/", views.signup2, name="signup2"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
