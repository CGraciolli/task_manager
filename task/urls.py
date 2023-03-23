from django.urls import path
from . import views

app_name = "task"

urlpatterns = [
    path("new/", views.new, name="new"),
    path("<int:pk>/", views.item, name="item"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),
]