from django.db.models import (
    Model, CASCADE, BooleanField,
    IntegerField, CharField, DecimalField, ForeignKey, DateTimeField,)
from django.contrib.auth.models import User


class Pledge(Model):

    class PledgeType:
        CONDITION = 'S'
        FINAL = 'D1'
        DISMISS = 'D'

        @classmethod
        def choices(cls):
            return (
                (cls.CONDITION, 'condition'),
                (cls.FINAL, 'final'),
                (cls.DISMISS, 'dismiss'),
            )

    student = ForeignKey(User, on_delete=CASCADE)
    pledge_type = CharField(max_length=2, choices=PledgeType.choices())
    next_tearm = IntegerField()
    kfupm_gpa = DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True)
    phone = IntegerField()
    phone_guardian = IntegerField(blank=True, null=True)
    # date
    date_update = DateTimeField(auto_now=True)
    approved_date = DateTimeField()
    is_approved = BooleanField(null=True)
