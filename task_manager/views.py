from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.mixins import VerboseLoginRequiredMixin


class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('index')
    success_message = _("You are logged in")

    def form_invalid(self, form):
        messages.error(self.request, _(
            'Please enter the correct username and password. Both fields can '
            'be case sensitive.'
        ))
        return super().form_invalid(form)


class UserLogout(VerboseLoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)
