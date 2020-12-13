from django.views.generic import CreateView
from django.contrib.auth.models import User
from openpyxl import load_workbook
from .forms import AddStudentsForm
from student.models import Pledge

class StudentsView(CreateView):
    """
    Adding students using an excel file.

    - List all student registered in the database, 
    - download the template excel file.
    """
    template_name = "administration/student.html"
    form_class = AddStudentsForm

    def form_valid(self, form):
        response = super().form_valid(form)
        e_file = load_workbook(self.object.excel_file.path) 
        for sheet in e_file.sheetnames:
            for row in e_file[sheet].rows:
                kfupmid = row[1].value
                if isinstance(kfupmid, int):
                    passwd = str(row[2].value)
                    name = row[3].value
                    tearm = row[4].value
                    gpa = row[5].value if len(row) > 5 else 0.0
                    if not User.objects.filter(username=kfupmid):
                        user = User.objects.create_user(
                            kfupmid, 
                            f's{kfupmid}@kfupm.edu.sa', 
                            passwd,
                            first_name=name)
                        Pledge.objects.create(
                            student=user,
                            pledge_type=sheet.lower(), 
                            kfupm_gpa=gpa, 
                            next_tearm=tearm)
                    else:
                        # TODO: student already exist.
                        pass
        return response
