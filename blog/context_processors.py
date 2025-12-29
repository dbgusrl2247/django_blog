from .models import Post

def recent_posts(request):
    """
    모든 템플릿에서 recent_posts 변수로 최신 글 목록을 쓰기 위한 context processor
    """
    posts = Post.objects.all().order_by("-created_at")[:5]
    return {"recent_posts": posts}
