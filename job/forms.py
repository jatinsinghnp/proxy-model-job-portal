from django import forms
from job.models import Job


class JobForms(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ("slug", "job_company")
