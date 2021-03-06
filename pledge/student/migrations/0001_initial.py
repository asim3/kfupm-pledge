# Generated by Django 3.1.4 on 2020-12-13 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pledge_type', models.CharField(choices=[('S', 'condition'), ('D1', 'final'), ('D', 'dismiss')], max_length=2)),
                ('next_tearm', models.IntegerField()),
                ('kfupm_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('phone', models.IntegerField()),
                ('phone_guardian', models.IntegerField(blank=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('approved_date', models.DateTimeField()),
                ('is_approved', models.BooleanField(null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
