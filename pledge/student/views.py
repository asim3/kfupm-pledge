from django.views.generic import UpdateView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView

from .forms import PledgeForm, AuthenticationForm


class HomeView(LoginRequiredMixin, DetailView):
    template_name = "student/home.html"

    def get_object(self):
        return self.request.user.pledge_set.order_by('-id').first()


class PledgeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "student/pledge.html"
    form_class = PledgeForm
    success_url = reverse_lazy("home")
    # TODO: add translation
    success_message = "شكراً لك لقد قمت بالانتهاء من تعبئة نموذج الإقرار "

    def get_object(self, queryset=None):
        return self.request.user.pledge_set.order_by('-id').first()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object:
            messages.warning(self.request, _(
                'Please contact Admission Department to add your pledge form'))
            return HttpResponseRedirect(reverse_lazy("home"))
        elif self.object.approved_date is not None:
            return HttpResponseRedirect(reverse_lazy("home"))
        return super().get(request, *args, **kwargs)


class LoginForAllView(LoginView):
    form_class = AuthenticationForm

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy("admin:index")
        return reverse_lazy("pledge")


class ReportsView(PermissionRequiredMixin, DetailView):
    template_name = "reports/list.html"

    def has_permission(self):
        return self.request.user.is_staff

    def get_object(self):
        return self.request.user.get_full_name()
