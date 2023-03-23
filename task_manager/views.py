from django.shortcuts import render, redirect
from .forms import SignUpForm
from task.models import Task
from django.contrib.auth import logout

def tasks(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user = request.user)
    else:
        tasks = []
    return render(request, "tasks.html", {"tasks": tasks})

def item(request):
    return render(request, "item.html", {})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/login/")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})

def log_out(request):
    logout(request)
    
    return redirect("tasks")
