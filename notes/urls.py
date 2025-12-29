from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.note_list, name="note_list"),
    path("notes/new/", views.note_create, name="note_create"),        # ✅ 추가
    path("notes/<int:pk>/", views.note_detail, name="note_detail"),
]
