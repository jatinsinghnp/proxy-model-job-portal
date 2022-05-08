# Generated by Django 4.0.4 on 2022-05-08 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_profiles_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAdditional',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=220)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_website', models.CharField(max_length=220)),
                ('company_address', models.CharField(max_length=220)),
                ('company_logo', models.FileField(blank=True, null=True, upload_to='')),
                ('company_description', models.TextField()),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantAdditional',
            fields=[
                ('applicant_id', models.AutoField(primary_key=True, serialize=False)),
                ('applicant_address', models.CharField(max_length=50)),
                ('applicant_qualification', models.TextField()),
                ('applicant_description', models.TextField()),
                ('applicant_profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]