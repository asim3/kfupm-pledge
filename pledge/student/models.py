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
        FINAL = 'S1'
        DISMISS = 'D'

        @classmethod
        def choices(cls):
            return (
                (cls.CONDITION, _('condition')),
                (cls.FINAL, _('final')),
                (cls.DISMISS, _('dismiss')),
            )

    student = ForeignKey(User, on_delete=CASCADE, verbose_name=_('student'))
    pledge_type = CharField(_('Pledge Type'),
                            max_length=2,
                            choices=PledgeType.choices())
    next_tearm = IntegerField(_('Next Tearm'), )
    kfupm_gpa = DecimalField(_('KFUPM GPA'),
                             max_digits=3, decimal_places=2, blank=True, null=True)
    # info
    phone = IntegerField(_('Phone'), null=True)
    phone_guardian = IntegerField(_('Phone Guardian'), blank=True, null=True)
    guardian_relation = CharField(
        _('Guardian Relation'), max_length=100, blank=True, null=True)
    # performance
    low_performance_reasons = CharField(_('Low Performance Reasons'),
                                        max_length=100, null=True)
    low_performance_other_reasons = CharField(
        _('Low Performance Other Reasons'), max_length=300, blank=True, null=True)
    # date
    date_added = DateTimeField(_('Date Added'), auto_now_add=True)
    approved_date = DateTimeField(_('Approved Date'), null=True)
    export_date = DateTimeField(_('export Date'), null=True)
    is_approved = BooleanField(_('Is Approved'), null=True)
