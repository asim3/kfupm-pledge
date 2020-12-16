from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Pledge
from .forms import PledgeForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "student/home.html"


class PledgeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "student/pledge.html"
    form_class = PledgeForm
    success_url = reverse_lazy("home")
    success_message = _("Your pledge was updated successfully")

    def get_object(self, queryset=None):
        try:
            # Get the single item from the filtered queryset
            obj = Pledge.objects.filter(
                student=self.request.user).order_by('-id')[1]
        except Pledge.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': Pledge.model._meta.verbose_name})
        return obj


class LoginForAllView(LoginView):
    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy("admin:index")
        return reverse_lazy("pledge")
