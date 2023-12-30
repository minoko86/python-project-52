from django import forms
from django.db.models import DateTimeField
from django.utils.translation import gettext as _
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.users.models import User


class CreateTaskForm(forms.ModelForm):
    name = forms.CharField(max_length=255, label=_("Name"))
    description = forms.CharField(
        label=_("Description"), required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 'placeholder': _("Description")
        })
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(), label=_("Status")
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(), label=_("Executor"),
        required=False
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(), label=_("Labels"), required=False
    )
    creation_date = DateTimeField(auto_now_add=True)

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
