# Generated by Django 3.2.5 on 2022-06-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_warning_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warning',
            name='status',
            field=models.CharField(blank=True, default=None, max_length=120, null=True, verbose_name='Warning status'),
        ),
    ]
