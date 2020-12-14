from django.db.models import Model, FileField
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class AddStudents(Model):

    class Meta:
        ordering = ["excel_file"]
        verbose_name = _('Add Student')
        verbose_name_plural = _("Add Students")

    excel_file = FileField(upload_to='uploads/%Y/%m/%d/')

    def get_absolute_url(self):
        return reverse_lazy('admin-student')
