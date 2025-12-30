from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.note_list, name="note_list"),
    path("notes/new/", views.note_create, name="note_create"),
    path("notes/<int:pk>/", views.note_detail, name="note_detail"),
    path("notes/<int:pk>/edit/", views.note_update, name="note_update"),      # ✅ 추가
    path("notes/<int:pk>/delete/", views.note_delete, name="note_delete"),    # ✅ 추가
]
