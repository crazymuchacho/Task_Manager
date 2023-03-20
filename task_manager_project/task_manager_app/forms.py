from django import forms


class TaskViewForm(forms.Form):
    task = forms.CharField()
    task_is_Done = forms.BooleanField()
    task_create = forms.DateTimeField()
    task_completed = forms.DateTimeField()
    task_plan = forms.DateTimeField()
    task_author = forms.CharField()
    task_implementer = forms.CharField()
    task_attach = forms.FileField()
    task_project = forms.CharField()
    task_sprint = forms.CharField()
