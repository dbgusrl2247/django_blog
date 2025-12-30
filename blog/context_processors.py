from .models import Category, Post

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def recent_posts(request):
    return {
        'recent_posts': Post.objects.order_by('-created_at')[:5]
    }