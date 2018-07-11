# Generated by Django 2.0.2 on 2018-07-05 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sequencing', '0015_auto_20180515_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lane',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_lanes', to='sequencing.Run'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='run_samples', to='sequencing.Run'),
        ),
    ]