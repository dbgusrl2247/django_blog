from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),           # ✅ /posts/
    path("posts/new/", views.post_create, name="post_create"),   # ✅ /posts/new/
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("category/<str:slug>/", views.post_category, name="post_category"),
    path("search/", views.post_search, name="post_search"),
]
