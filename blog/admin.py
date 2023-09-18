from django.contrib import admin
from .models import Post, Comment


# để khi vào trang admin thêm phần comment ở phía dưới
# StackedInline hiển thị phần comment theo hàng ngang
# TabularInline theo hàng dọc nhìn ngắn hơn
class CommentInline(admin.StackedInline):
    model = Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "image"]
    list_filter = ["date"]
    search_fields = ["title"]
    # thêm cái phần comment để hiển thị vào
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
