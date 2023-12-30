import django_filters
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.utils.translation import gettext as _


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(), label=_("Status")
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(), label=_("Executor")
    )
    labels = django_filters.ModelMultipleChoiceFilter(
        queryset=Label.objects.all(), label=_("Labels")
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_tasks(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
