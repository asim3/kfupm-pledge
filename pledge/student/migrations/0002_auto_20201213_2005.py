# Generated by Django 3.1.4 on 2020-12-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='approved_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
