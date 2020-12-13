from django.forms import ModelForm
from .models import AddStudents


class AddStudentsForm(ModelForm):
    class Meta:
        model = AddStudents
        fields = ['excel_file']
