# Generated by Django 4.0.4 on 2022-05-07 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_applicant_delete_company_applicantprofile_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiles',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
    ]