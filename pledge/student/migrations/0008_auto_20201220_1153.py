# Generated by Django 3.1.4 on 2020-12-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20201219_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='approved_date',
            field=models.DateTimeField(null=True, verbose_name='approved_date'),
        ),
    ]
