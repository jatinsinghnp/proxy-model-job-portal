# Generated by Django 4.0.4 on 2022-05-08 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0008_remove_companyadditional_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=220)),
                ('job_salary', models.FloatField()),
                ('job_description', models.TextField()),
                ('job_start_date', models.DateField()),
                ('job_end_date', models.DateField()),
                ('job_type', models.CharField(choices=[('FullTime', 'FullTime'), ('PartTime', 'PartTime')], max_length=220)),
                ('job_working_hour', models.CharField(max_length=20)),
                ('job_expreience', models.CharField(max_length=220)),
                ('job_status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending')], max_length=220)),
                ('job_creations_date', models.DateTimeField(auto_now_add=True)),
                ('job_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.companyprofile')),
            ],
        ),
    ]
