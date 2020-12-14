from django.contrib.admin import register, ModelAdmin
from .models import AddStudents
from .forms import AddStudentsForm


@register(AddStudents)
class AddStudentsAdmin(ModelAdmin):
    form = AddStudentsForm
    add_form = AddStudentsForm
