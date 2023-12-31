"""
URL configuration for PythonWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

# ghép đường dẫn ảnh, nếu deploy sever thì ko cần làm
from django.conf.urls.static import static
from django.conf import settings

# để tạo API
from rest_framework.routers import DefaultRouter
from blog.views import TaskViewSet

router = DefaultRouter()
router.register(r"posts", TaskViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("blog/", include("blog.urls")),
    path("api/", include(router.urls)),
]

# ghép đường dẫn ảnh, nếu deploy sever thì ko cần làm
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "home.views.error_404"
