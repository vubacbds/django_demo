from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # nếu ko cso null=True thì các trường dữ liệu đã tồn tại sẽ lỗi
    image = models.ImageField(null=True)

    # thay vì trả object, nó trả ra title
    def __str__(self):
        return self.title


# tạo Model cho bình luận
class Comment(models.Model):
    # quan hệ 1 nhiều lấy khóa phụ, on_delete để khi Post xóa thì các bình luận xóa luôn, related_name để gọi lại ở tempalates
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    # lấy khóa ngoại model user qua settings
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # body, date nhập từ form
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


# Create your models here.
