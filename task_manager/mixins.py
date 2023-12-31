from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _


class VerboseLoginRequiredMixin(LoginRequiredMixin):

    login_url = 'login'
    permission_denied_message = _(
        'You are not logged in! Please log in.'
    )

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()
