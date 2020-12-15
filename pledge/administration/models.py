from django.db.models import Model, FileField
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from openpyxl import load_workbook
from student.models import Pledge


def add_new_student(row, pledge_type):
    kfupmid = row[1].value
    passwd = str(row[2].value)
    name = row[3].value
    tearm = row[4].value
    gpa = row[5].value if len(row) > 5 else 0.0
    user = User.objects.create_user(kfupmid, f's{kfupmid}@kfupm.edu.sa',
                                    passwd, first_name=name)
    Pledge.objects.create(
        student=user,
        pledge_type=pledge_type,
        kfupm_gpa=gpa,
        next_tearm=tearm)


def add_new_students_from_excel(e_path):
    e_file = load_workbook(e_path)
    for sheet in e_file.sheetnames:
        for (i, row) in enumerate(e_file[sheet].rows):
            if i < 1:
                continue
            add_new_student(row, sheet.capitalize())


class AddStudents(Model):

    class Meta:
        ordering = ["excel_file"]
        verbose_name = _('Add Student')
        verbose_name_plural = _("Add Students")

    excel_file = FileField(upload_to='uploads/%Y/%m/%d/')

    def get_absolute_url(self):
        return reverse_lazy('admin-student')

    def save(self, *args, **kwargs):
        response = super().save(*args, **kwargs)
        add_new_students_from_excel(self.excel_file.path)
