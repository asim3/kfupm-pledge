from django.contrib.admin import register, ModelAdmin
from .models import Pledge


@register(Pledge)
class AdminPledge(ModelAdmin):
    list_display = (
        'student',
        'pledge_type',
        'next_tearm',
        'kfupm_gpa',
        'phone',
        'phone_guardian',
        'date_update',
        'approved_date',
        'is_approved',)
