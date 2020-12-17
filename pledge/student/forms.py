from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.forms import (
    ModelForm, MultipleChoiceField, CheckboxSelectMultiple, CheckboxInput, BooleanField)
from .models import Pledge


class LowPerformanceReasons:
    HEALTHY = 'HEALTHY'
    PHYSICAL = 'PHYSICAL'
    FAMILY = 'FAMILY'
    STUDY = 'STUDY'
    OTHER = 'OTHER'

    @classmethod
    def choices(cls):
        return (
            (cls.HEALTHY, _('Healthy')),
            (cls.PHYSICAL, _('Psychological')),
            (cls.FAMILY, _('Family circumstances')),
            (cls.STUDY, _(
                'Study difficulties related to (major / academic courses)')),
            (cls.OTHER, _('other')),
        )


class PledgeForm(ModelForm):
    low_performance_reasons = MultipleChoiceField(
        widget=CheckboxSelectMultiple,
        choices=LowPerformanceReasons.choices(),)
    is_approved = BooleanField(widget=CheckboxInput)

    class Meta:
        model = Pledge
        fields = ['low_performance_reasons',
                  'phone',
                  'phone_guardian',
                  'is_approved', ]
