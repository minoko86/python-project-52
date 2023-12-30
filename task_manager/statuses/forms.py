from django import forms
from django.utils.translation import gettext as _
from task_manager.statuses.models import Status


class CreateStatusForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label=_("Name"))

    class Meta:
        model = Status
        fields = ['name']
