from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTaskForm, EditTaskForm
from django.contrib.auth.decorators import login_required
from .models import Task

def item(request, pk):
    item = get_object_or_404(Task, pk=pk)

    return render(request, "item.html", {"item": item})

@login_required
def new(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST, request.FILES)
        if form.is_valid:
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task:item", pk=task.pk)
    else:
        form = NewTaskForm()
    return render(request, "new.html", {"form": form})

@login_required
def edit(request, pk):
    item = get_object_or_404(Task, pk=pk, user = request.user)
    if request.method == "POST":
        form = EditTaskForm(request.POST, request.FILES, instance=item)
        if form.is_valid:
            form.save()
            return redirect("task:item", pk=item.pk)
    else:
        form = EditTaskForm(instance=item)
    return render(request, "new.html", {"form": form})

@login_required
def delete(request, pk):
    item = get_object_or_404(Task, pk=pk, user = request.user)
    item.delete()

    return redirect("tasks")