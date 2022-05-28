from django import forms
from job.models import Job


class JobForms(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ("slug", "job_company")
        widgets = {
            "job_title": forms.TextInput(
                attrs={"class": "p-1 outline-none", "placeholder": "Job Title"}
            ),
            "job_salary": forms.TextInput(
                attrs={"class": "p-1 outline-none", "placeholder": "Salary"}
            ),
            "job_description": forms.Textarea(
                attrs={
                    "class": " form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transitionease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none",
                    "placeholder": "Job Description",
                    "rows": 5,
                    "cols": 20,
                }
            ),
            "job_start_date": forms.DateInput(
                attrs={"class": "p-1 outline-none", "placeholder": "yyyy-dd-mm"}
            ),
            "job_end_date": forms.DateInput(
                attrs={"class": "p-1 outline-none", "placeholder": "yyyy-dd-mm"}
            ),
            "job_type": forms.Select(
                attrs={
                    "class": "p-1 outline-none ",
                },
            ),
            "job_working_hour": forms.TextInput(
                attrs={"class": "p-1 outline-none", "placeholder": "Working hours"}
            ),
            "job_expreience": forms.TextInput(
                attrs={"class": "p-1 outline-none", "placeholder": "Expreience"}
            ),
            "job_company": forms.Select(
                attrs={
                    "class": "p-1 outline-none",
                }
            ),
        }
