from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task   # ✅ THIS LINE IS REQUIRED
        fields = ['task', 'is_completed']