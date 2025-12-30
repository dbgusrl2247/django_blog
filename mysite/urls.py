from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # ✅ 메인/소개/연락
    path("", include("pages.urls")),

    # ✅ 포스트는 /posts/ 아래로
    path("", include("blog.urls")),

    # ✅ 노트는 /notes/ 아래로
    path("", include("notes.urls")),
]
