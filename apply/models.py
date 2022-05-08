from django.db import models
from job.models import Job
from Applicant.models import Applicant

# Create your models here.
class Apply(models.Model):
    apply_id = models.AutoField(primary_key=True)
    apply_job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    apply_applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, null=True, blank=True
    )
    apply_date = models.DateTimeField(auto_now_add=True)
    apply_cv = models.FileField(blank=True, null=True)

    def __str__(self) -> str:
        return self.apply_applicant.applicant_profile.first_name
