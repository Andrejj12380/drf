# Generated by Django 3.1.2 on 2022-09-26 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0017_auto_20220926_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_id', to='measurement.sensor'),
        ),
    ]
