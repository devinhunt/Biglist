from django import forms

class AddTaskForm(forms.Form):
    task = forms.CharField(max_length = 500)