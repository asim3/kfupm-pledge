from django.db.models import (
    Model, CASCADE, BooleanField,
    IntegerField, CharField, DecimalField, ForeignKey, DateTimeField,)
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Pledge(Model):

    class Meta:
        ordering = ["date_added"]
        verbose_name = _('Pledge')
        verbose_name_plural = _("Pledges")

    class PledgeType:
        CONDITION = 'S'
        FINAL = 'D1'
        DISMISS = 'D'

        @classmethod
        def choices(cls):
            return (
                (cls.CONDITION, _('condition')),
                (cls.FINAL, _('final')),
                (cls.DISMISS, _('dismiss')),
            )

    student = ForeignKey(User, on_delete=CASCADE, verbose_name=_('student'))
    pledge_type = CharField(_('pledge_type'),
                            max_length=2,
                            choices=PledgeType.choices())
    next_tearm = IntegerField(_('next_tearm'), )
    kfupm_gpa = DecimalField(_('kfupm_gpa'),
                             max_digits=3, decimal_places=2, blank=True, null=True)
    phone = IntegerField(_('phone'), null=True)
    phone_guardian = IntegerField(_('phone_guardian'), blank=True, null=True)
    low_performance_reasons = CharField(_('low_performance_reasons'),
                                        max_length=100, null=True,)
    # date
    date_added = DateTimeField(_('date_added'), auto_now_add=True)
    approved_date = DateTimeField(_('approved_date'), auto_now=True)
    is_approved = BooleanField(_('is_approved'), null=True)
