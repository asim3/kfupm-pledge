from django.forms import ModelForm
from .models import Pledge


class PledgeForm(ModelForm):

    class Meta:
        model = Pledge
        fields = ['pledge_type',
                  'next_tearm',
                  'kfupm_gpa',
                  'phone',
                  'phone_guardian',
                  'approved_date',
                  'is_approved', ]
