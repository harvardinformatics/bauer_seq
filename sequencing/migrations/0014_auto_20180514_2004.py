# Generated by Django 2.0.2 on 2018-05-14 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequencing', '0013_auto_20180514_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='type',
            new_name='run_type',
        ),
    ]
