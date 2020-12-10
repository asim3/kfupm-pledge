from django.forms import Form, FileField


class AddStudentForm(Form):
    excel_file = FileField(upload_to='uploads/%Y/%m/%d/', max_length=100)

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        return HttpResponseRedirect(self.get_success_url())
