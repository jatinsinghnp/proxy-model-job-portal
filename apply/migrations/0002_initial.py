# Generated by Django 4.0.4 on 2022-05-08 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0001_initial'),
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='apply_job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.job'),
        ),
    ]
