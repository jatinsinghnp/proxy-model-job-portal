from django.db import models
from account.models import CompanyProfile
# Create your models here.


class Job(models.Model):

    STATUS_CHOICE = [
        ("Active", "Active"),
        ("Pending", "Pending"),
    ]

    TYPES_CHOICES = [
        ("FullTime", "FullTime"),
        ("PartTime", "PartTime"),
    ]
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=220)
    job_salary = models.FloatField()
    job_description = models.TextField()
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    job_type = models.CharField(max_length=220, choices=TYPES_CHOICES)
    job_working_hour = models.CharField(max_length=20)
    job_expreience = models.CharField(max_length=220, blank=False, null=False)
    job_company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    job_status = models.CharField(max_length=220, choices=STATUS_CHOICE)
    job_creations_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.job_title
