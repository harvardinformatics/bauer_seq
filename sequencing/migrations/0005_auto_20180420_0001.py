# Generated by Django 2.0.2 on 2018-04-20 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequencing', '0004_auto_20180419_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='log',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='pid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='stop',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='read',
            name='indexed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='read',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='requestor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='index1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='index2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
