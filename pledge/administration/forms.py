from django.forms import ModelForm, ValidationError
from django.contrib.auth.models import User
from openpyxl import load_workbook
from .models import AddStudents


class AddStudentsForm(ModelForm):
    class Meta:
        model = AddStudents
        fields = ['excel_file']

    def clean_excel_file(self):
        excel_file = self.cleaned_data.get('excel_file')
        e_file = load_workbook(excel_file.file)
        for sheet in e_file.sheetnames:
            for (i, row) in enumerate(e_file[sheet].rows):
                if i < 1:
                    continue
                kfupmid = row[1].value
                if isinstance(kfupmid, int):
                    if User.objects.filter(username=kfupmid):
                        raise ValidationError(
                            f"Student {kfupmid} is already listed")
                else:
                    raise ValidationError(
                        f"Student {kfupmid} is not valid!")
                if not isinstance(row[2].value, int):
                    raise ValidationError(
                        f"Student {kfupmid} national ID is not valid!")
                if not isinstance(row[4].value, int):
                    raise ValidationError(
                        f"Student {kfupmid} next tearm is not valid!")
                if len(row) > 5 and not isinstance(row[5].value, float):
                    if not isinstance(row[5].value, int):
                        raise ValidationError(
                            f"Student {kfupmid} GPA is not valid!")
        return excel_file
