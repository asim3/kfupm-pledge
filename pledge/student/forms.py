from django.forms import ModelForm, MultipleChoiceField
from .models import Pledge


class PledgeForm(ModelForm):
    low_performance_reasons = MultipleChoiceField

    class Meta:
        model = Pledge
        fields = ['low_performance_reasons',
                  'phone',
                  'phone_guardian',
                  'is_approved', ]
