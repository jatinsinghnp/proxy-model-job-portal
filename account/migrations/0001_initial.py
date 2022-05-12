# Generated by Django 4.0.4 on 2022-05-09 01:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import django.db.models.functions.text
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,10}$')])),
                ('first_name', models.CharField(max_length=50, verbose_name='fname')),
                ('last_name', models.CharField(max_length=50, verbose_name='lname')),
                ('profile_image', models.ImageField(upload_to=None, verbose_name='imagfields')),
                ('user_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Company', 'Company'), ('Applicant', 'Applicant')], default=[], max_length=17, null=True)),
                ('date_of_birth', models.DateField(verbose_name='DOB')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is_admin')),
                ('is_staff', models.BooleanField(default=False)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='CompanyAdditional',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=220)),
                ('company_website', models.CharField(max_length=220)),
                ('company_address', models.CharField(max_length=220)),
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
        migrations.AddConstraint(
            model_name='profiles',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('first_name'), django.db.models.expressions.OrderBy(django.db.models.functions.text.Lower('last_name'), descending=True), name='first_last_name_unique'),
        ),
        migrations.CreateModel(
            name='ApplicantProfile',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.profiles',),
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.profiles',),
        ),
    ]
