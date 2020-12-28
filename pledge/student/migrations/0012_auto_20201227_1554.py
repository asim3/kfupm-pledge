# Generated by Django 3.1.4 on 2020-12-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20201221_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='export_date',
            field=models.DateTimeField(null=True, verbose_name='export Date'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='approved_date',
            field=models.DateTimeField(null=True, verbose_name='Approved Date'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Added'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='guardian_relation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Guardian Relation'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='is_approved',
            field=models.BooleanField(null=True, verbose_name='Is Approved'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='kfupm_gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='KFUPM GPA'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='low_performance_other_reasons',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Low Performance Other Reasons'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='low_performance_reasons',
            field=models.CharField(max_length=100, null=True, verbose_name='Low Performance Reasons'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='next_tearm',
            field=models.IntegerField(verbose_name='Next Tearm'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='phone_guardian',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone Guardian'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='pledge_type',
            field=models.CharField(choices=[('S', 'condition'), ('D1', 'final'), ('D', 'dismiss')], max_length=2, verbose_name='Pledge Type'),
        ),
    ]
