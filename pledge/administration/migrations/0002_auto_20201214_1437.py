# Generated by Django 3.1.4 on 2020-12-14 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addstudents',
            options={'ordering': ['excel_file'], 'verbose_name': 'Add Student', 'verbose_name_plural': 'Add Students'},
        ),
    ]
