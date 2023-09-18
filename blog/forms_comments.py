from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

# gọi lại model Comment đã tạo
from .models import Comment


# tạo form từ các trường từ model (nó sẽ tự động thêm và xác thực các trường input luôn)
class CommentForm(forms.ModelForm):
    # # để thêm các trường mà khóa ngoại, ko tự thêm bằng tay đc
    # def __init__(self, *args, **kwargs):
    #     # trường author lấy giá trị trong list kwargs đã unpaking, còn *args đánh dấu các tham số kế tiếp phải truyền vào có key đằng trước
    #     # lúc đầu CommentForm chạy ko có thì author lấy là null
    #     self.author = kwargs.pop("author", None)
    #     self.post = kwargs.pop("post", None)

    #     # super là hàm khởi tạo hàm cha
    #     super().__init__(*args, **kwargs)

    # # hàm save() này đã viết sẵn nhưng vì muốn overwrite là muốn thêm author, post, date nên cần
    # # commit=True là lưu vào db

    # def save(self, commit=True):
    #     # commit=false để ko lưu vào db
    #     comment = super().save(commit=False)
    #     comment.author = self.author
    #     comment.post = self.post
    #     comment.save()

    class Meta:
        model = Comment
        # có mỗi trường body vì các trường kia tự thêm, ko thể nhập bằng tay
        fields = ["body"]
