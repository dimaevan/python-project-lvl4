# Generated by Django 3.2.11 on 2022-01-16 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='workers',
            new_name='executor',
        ),
    ]