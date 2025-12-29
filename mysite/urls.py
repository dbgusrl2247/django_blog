from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # pages: /about, /contact
    path("", include("pages.urls")),

    # blog: / (목록), /posts/1/ (상세)
    path("", include("blog.urls")),
    path("", include("notes.urls")),

]

# 개발환경에서 media 파일 서빙(배포에서는 다르게 처리)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
