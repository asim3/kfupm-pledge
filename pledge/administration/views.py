from django.views.generic import TemplateView


class StudentView(TemplateView):
    """
    List all student registered in the database, 
    add new students using an excel file,
    download the template excel file.
    """
    template_name = "administration/student.html"
