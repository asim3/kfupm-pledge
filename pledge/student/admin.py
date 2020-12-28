from django.contrib.admin import register, ModelAdmin
from django.http import HttpResponse
from django.utils.timezone import datetime
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from .models import Pledge


@register(Pledge)
class AdminPledge(ModelAdmin):
    search_fields = ('student__username', 'student__first_name', 'phone', 'phone_guardian')
    list_filter = ("is_approved", 'export_date',)
    ordering = ('date_added',)
    list_display = (
        'student',
        'pledge_type',
        'next_tearm',
        'kfupm_gpa',
        'date_added',
        'phone',
        'phone_guardian',
        'approved_date',
        'export_date',
        'is_approved',)

    def export_as_excel(self, request, queryset):
        excel_file = Workbook()
        excel_file.active.title = Pledge.PledgeType.CONDITION
        excel_file.create_sheet(title=Pledge.PledgeType.FINAL)
        excel_file.create_sheet(title=Pledge.PledgeType.DISMISS)
        settings = (
            ('A', 5, 'No'),
            ('B', 15, 'KFUPM ID'),
            ('C', 30, 'Approved Date'),
            ('D', 15, 'Phone'),
            ('E', 15, 'Phone Guardian'),)

        for sheet_name in excel_file.sheetnames:
            sheet = excel_file[sheet_name]
            for setting in settings:
                sheet.column_dimensions[setting[0]].width = setting[1]
                sheet['%s1' % setting[0]] = setting[2]

            data = queryset.filter(pledge_type=sheet_name)
            for i, pledge in enumerate(data, start=2):
                sheet['A%d' % i] = i - 1
                sheet['B%d' % i] = pledge.student.username
                sheet['C%d' % i] = pledge.approved_date
                sheet['D%d' % i] = pledge.phone
                sheet['E%d' % i] = pledge.phone_guardian

        data.update(export_date=datetime.now())

        excel_bytes = save_virtual_workbook(excel_file)
        content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        filename = 'pledge-%s.xlsx' % datetime.now().strftime('%s')
        response = HttpResponse(excel_bytes, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response

    actions = ['export_as_excel']
    export_as_excel.short_description = "تصدير إلى ملف إكسل"
