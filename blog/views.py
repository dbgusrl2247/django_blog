from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Post, Category
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts, "category": None})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

def post_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by("-created_at")
    return render(
        request,
        "blog/post_list.html",
        {
            "posts": posts,
            "category": category,
        },
    )

def post_search(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by("-created_at")
    else:
        posts = Post.objects.none()

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts, "category": None, "query": query},
    )
