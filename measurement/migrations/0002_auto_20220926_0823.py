# Generated by Django 3.1.2 on 2022-09-26 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='date',
            new_name='created_at',
        ),
    ]