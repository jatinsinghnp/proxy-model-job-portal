from .models import Apply
from django import forms


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = "__all__"
        exclude = ("apply_applicant", "apply_job")
