from django.db import models
from django.urls import reverse_lazy


class AddStudents(models.Model):
    excel_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def get_absolute_url(self):
        return reverse_lazy('admin-student')