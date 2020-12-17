from django.contrib.admin import register, ModelAdmin
from .models import Pledge


@register(Pledge)
class AdminPledge(ModelAdmin):
    search_fields = ('student', 'phone', 'phone_guardian')
    ordering = ('date_added',)
    list_display = (
        'student',
        'pledge_type',
        'next_tearm',
        'kfupm_gpa',
        'date_added',
        'phone',
        'phone_guardian',
        'approved_date',
        'is_approved',)
