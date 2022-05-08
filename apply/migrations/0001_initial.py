# Generated by Django 4.0.4 on 2022-05-06 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Applicant', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('apply_id', models.AutoField(primary_key=True, serialize=False)),
                ('apply_date', models.DateTimeField(auto_now_add=True)),
                ('apply_applicant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Applicant.applicant')),
                ('apply_job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
    ]