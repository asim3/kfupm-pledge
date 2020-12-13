from django.forms import ModelForm
from .models import AddStudents


class AddStudentsForm(ModelForm):
    class Meta:
        model = AddStudents
        fields = ['excel_file']

    def form_valid(self, form):
        print('\n'*3, form.object)
        return HttpResponseRedirect(self.get_success_url())
