from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.forms import (
    ModelForm, CharField, TextInput, PasswordInput, BooleanField,
    MultipleChoiceField, CheckboxSelectMultiple, CheckboxInput,)
from django.contrib.auth.forms import UsernameField, AuthenticationForm as AuthenticationFormBase
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
            (cls.HEALTHY, "صحية"),
            (cls.PHYSICAL, "نفسية"),
            (cls.FAMILY, "ظروف أسرية"),
            (cls.STUDY, "صعوبات دراسية متعلقة (بالتخصص / مقررات دراسية)"),
            (cls.OTHER, "اخرى"),
        )
        # return (
        #     (cls.HEALTHY, _('Healthy')),
        #     (cls.PHYSICAL, _('Psychological')),
        #     (cls.FAMILY, _('Family circumstances')),
        #     (cls.STUDY, _(
        #         'Study difficulties related to (major / academic courses)')),
        #     (cls.OTHER, _('other')),
        # )


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

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.approved_date = datetime.now()
        instance.save()
        return instance


class AuthenticationForm(AuthenticationFormBase):
    username = UsernameField(
        label="الرقم الجامعي",
        widget=TextInput(attrs={'autofocus': True})
    )
    password = CharField(
        label="رقم بطاقة الأحوال",
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
