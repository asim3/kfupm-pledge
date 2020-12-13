from django.views.generic import CreateView
from .forms import AddStudentsForm


class StudentsView(CreateView):
    """
    List all student registered in the database, 
    add new students using an excel file,
    download the template excel file.
    """
    template_name = "administration/student.html"
    form_class = AddStudentsForm
