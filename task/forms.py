from .models import Task
from django import forms

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["user"]
        widgets = {
            'due_date' : forms.DateInput(attrs={'type':'date'}, format='d/m/Y'),
        }

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["user"]
        widgets = {
            'due_date' : forms.DateInput(attrs={'type':'date'}, format='d/m/Y'),
        }