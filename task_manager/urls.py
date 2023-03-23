from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import LogInForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.tasks, name="tasks"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html", authentication_form = LogInForm), name="login"),
    path('task/', include('task.urls')),
    path('log_out/', views.log_out, name="log_out"),
]
