# Generated by Django 2.0.2 on 2018-05-07 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequencing', '0007_auto_20180504_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='read',
            name='lane_id',
        ),
    ]
