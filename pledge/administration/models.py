from django.db.models import Model, FileField
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from openpyxl import load_workbook
from student.models import Pledge




class AddStudents(Model):

    class Meta:
        ordering = ["excel_file"]
        verbose_name = _('Add Student')
        verbose_name_plural = _("Add Students")

    excel_file = FileField(upload_to='uploads/%Y/%m/%d/')

    def get_absolute_url(self):
        return reverse_lazy('admin-student')

        
    def add_new_student(self, excel_row, pledge_type):
        kfupmid = str(excel_row[1].value)
        try:
            user = User.objects.get(username=kfupmid)
        except User.DoesNotExist:
            user = User.objects.create_user(
                kfupmid, 
                email=f's{kfupmid}@kfupm.edu.sa',
                password=str(excel_row[2].value), 
                first_name=excel_row[3].value)
            
        next_tearm = excel_row[4].value
        kfupm_gpa = excel_row[5].value if len(excel_row) > 5 else 0.0
        try:
            Pledge.objects.get(
                student=user,
                pledge_type=pledge_type,
                next_tearm=next_tearm)
            print('get')
        except Pledge.DoesNotExist:
            Pledge.objects.create(
                student=user,
                pledge_type=pledge_type,
                kfupm_gpa=kfupm_gpa,
                next_tearm=next_tearm)
            print('add')

    def save(self, *args, **kwargs):
        response = super().save(*args, **kwargs)
        excel_file = load_workbook(self.excel_file.path)
        for sheet in excel_file.sheetnames:
            for (i, row) in enumerate(excel_file[sheet].rows):
                if i < 1:
                    continue
                self.add_new_student(row, sheet.capitalize())
