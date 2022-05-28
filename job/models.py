from django.db import models
from account.models import CompanyProfile
from django.utils.text import slugify
from random import randint

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
    job_title = models.CharField(max_length=220)
    job_salary = models.CharField(max_length=220)
    job_description = models.TextField()
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    job_type = models.CharField(max_length=220, choices=TYPES_CHOICES)
    job_working_hour = models.CharField(max_length=20)
    job_expreience = models.CharField(max_length=220, blank=False, null=False)
    job_company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    job_status = models.CharField(max_length=220, choices=STATUS_CHOICE)
    job_creations_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True,unique=True)

    def __str__(self) -> str:
        return self.job_title

    def save(self, *args, **kwargs):
        if Job.objects.filter(job_title=self.job_title).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.job_title) + "-" + extra
        else:
            self.slug = slugify(self.job_title)
        super(Job, self).save(*args, **kwargs)

