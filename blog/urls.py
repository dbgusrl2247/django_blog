from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("posts/new/", views.post_create, name="post_create"),     # ✅ 추가
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
]
