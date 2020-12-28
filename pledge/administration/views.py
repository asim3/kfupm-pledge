from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf import settings
from os.path import join


class DownloadExcelView(PermissionRequiredMixin, View):

    def has_permission(self):
        return self.request.user.is_staff

    def get_excel_template(self, **kwargs):
        path = join(settings.BASE_DIR, 'administration/static/excel-template.xlsx')
        return open(path, 'rb')

    def get(self, request, **kwargs):
        excel_bytes = self.get_excel_template()
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        filename = 'excel-template.xlsx'

        response = HttpResponse(excel_bytes, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
