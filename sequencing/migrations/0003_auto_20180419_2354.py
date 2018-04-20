# Generated by Django 2.0.2 on 2018-04-19 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequencing', '0002_auto_20180419_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='expiration',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='run',
            name='flowcell',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='run',
            name='lot',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
