from django.urls import path
from . import views

urlpatterns = [
    # path("", views.list, name="blog"),
    # nếu dùng cách khác thì gọi như này
    path("", views.PostListView.as_view(), name="blog"),
    # vào trang chi tiết dựa vào id
    # path("<int:id>/", views.post, name="post"),
    # vào trang chi tiết dựa vào primary key, nếu như dùng view có sẵn thì phải dùng cái này
    path("<int:post_id>/", views.post, name="post"),
]
