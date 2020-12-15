from django.views.generic import CreateView
from .forms import AddStudentsForm


class StudentsView(CreateView):
    """
    Adding students using an excel file.

    - List all student registered in the database, 
    - download the template excel file.
    """
    template_name = "administration/student.html"
    form_class = AddStudentsForm
    success_url = "/admin/student/pledge/"
