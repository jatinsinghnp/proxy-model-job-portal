# Generated by Django 4.0.4 on 2022-05-10 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_job_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_slug',
            new_name='slug',
        ),
    ]
