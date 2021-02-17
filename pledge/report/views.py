from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import PermissionRequiredMixin

from student.forms import LowPerformanceReasons
from student.models import Pledge


class ReportsView(PermissionRequiredMixin, DetailView):
    template_name = "reports/list_semester.html"

    def has_permission(self):
        return self.request.user.is_staff

    def get_object(self):
        return Pledge.objects.values('next_tearm').order_by('next_tearm').distinct()


class ReasonsReportsView(PermissionRequiredMixin, DetailView):
    template_name = "reports/list_choices.html"

    def has_permission(self):
        return self.request.user.is_staff

    def get_object(self):
        return LowPerformanceReasons.choices


class PrintReportsView(PermissionRequiredMixin, DetailView):
    template_name = "reports/list_choices.html"

    def has_permission(self):
        return self.request.user.is_staff

    def get_object(self):
        return LowPerformanceReasons.choices

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        tearm = kwargs.get('tearm')
        reasons = kwargs.get('reasons')
        if not self.object:
            return HttpResponseRedirect(reverse_lazy("home"))
        return super().get(request, *args, **kwargs)
