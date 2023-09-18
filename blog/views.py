from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import Http404
from django.views.generic import ListView, DetailView

# thêm mấy cái này để làm commenr
from django.http import HttpResponseRedirect
from .forms_comments import CommentForm
from .models import Comment


# Create your views here.
def list(request):
    Data = {"Post": Post.objects.all().order_by("-date")}
    return render(request, "blog/blog.html", Data)


# thay vì list như ở trên có cách khác nhanh hơn
class PostListView(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = "blog/blog.html"
    context_object_name = "Post"
    paginate_by = 1


# trang details bài viết gốc
# def post(request, id):
#     post = Post.objects.get(id=id)

#     return render(request, "blog/post.html", {"post": post})


# trang details bài viết có comment
# def post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = CommentForm()
#     if request.method == "POST":
#         form = CommentForm(request.POST, author=request.user, post=post)
#         # khi có hàm này mới gọi save được
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect(request.path)
#     return render(request, "blog/post.html", {"post": post, "form": form})


def post(request, post_id):
    # pk là primary key, get_object_or_404 vì lỗi 500
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        # CommentForm tạo từ model form là dựa vào các trường của model
        form = CommentForm(request.POST)
        # is_valid() mơi gọi dc save
        if form.is_valid():
            # commit=False để ko lưu vào db ngay mà muốn overwrite viết đè lên
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # để lưu thành công thì quay lại chính trang đó
            return redirect("post", post_id=post_id)
            # hoặc dùng lệnh này
            # return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
    # comments = Comment.objects.filter(post=post)
    return render(request, "blog/post.html", {"form": form, "post": post})
