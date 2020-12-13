from django.db import models

# Create your models here.


class AddStudents(models.Model):
    excel_file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    # MEDIA_ROOT/uploads
