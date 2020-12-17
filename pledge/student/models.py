from django.db.models import (
    Model, CASCADE, BooleanField,
    IntegerField, CharField, DecimalField, ForeignKey, DateTimeField,)
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Pledge(Model):

    class Meta:
        ordering = ["date_update"]
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
                                        max_length=10,
                                        null=True,
                                        choices=LowPerformanceReasons.choices())
    # date
    date_update = DateTimeField(_('date_update'), auto_now=True)
    approved_date = DateTimeField(_('approved_date'), null=True)
    is_approved = BooleanField(_('is_approved'), null=True)
