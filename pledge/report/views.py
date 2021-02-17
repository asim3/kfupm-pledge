from django.views.generic import DetailView, TemplateView
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import save_virtual_workbook

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


class PrintReportsView(PermissionRequiredMixin, TemplateView):
    template_name = "reports/list_choices.html"

    def has_permission(self):
        return self.request.user.is_staff

    def get_object(self, queryset=None):
        tearm = self.kwargs.get('tearm')
        reasons = self.kwargs.get('reasons')
        return Pledge.objects.filter(
            next_tearm=tearm,
            low_performance_reasons__contains=reasons)

    def get(self, request, *args, **kwargs):
        return self.export_as_excel(self.get_object())

    def export_as_excel(self, queryset):
        excel_file = Workbook()
        sheet_name = self.kwargs.get('reasons')
        excel_file.active.title = sheet_name
        settings = (
            ('A', 5, _('No')),
            ('B', 15, _('KFUPM ID')),
            ('C', 30, _('Name')),
            ('D', 30, _('Approved Date')),
            ('E', 15, _('Phone')),
            ('F', 15, _('Phone Guardian')),
        )

        sheet = excel_file[sheet_name]
        for setting in settings:
            sheet.column_dimensions[setting[0]].width = setting[1]
            sheet['%s1' % setting[0]] = str(setting[2])

        for i, pledge in enumerate(queryset, start=2):
            sheet['A%d' % i] = i - 1
            sheet['B%d' % i] = pledge.student.username
            sheet['C%d' % i] = pledge.student.first_name
            sheet['D%d' % i] = pledge.approved_date
            sheet['E%d' % i] = pledge.phone
            sheet['F%d' % i] = pledge.phone_guardian

        excel_bytes = save_virtual_workbook(excel_file)
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        filename = 'pledge-%s.xlsx' % datetime.now().strftime('%s')
        response = HttpResponse(excel_bytes, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
