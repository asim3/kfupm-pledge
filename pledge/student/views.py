from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .forms import PledgeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "student/home.html"


class PledgeView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "student/pledge.html"
    form_class = PledgeForm
    success_url = reverse_lazy("home")
    success_message = _("Your pledge was updated successfully")


class LoginForAllView(LoginView):
    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy("admin:index")
        return reverse_lazy("pledge")
