from django.shortcuts import render, redirect
from .forms import SignUpForm

def tasks(request):
    return render(request, "tasks.html", {})

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