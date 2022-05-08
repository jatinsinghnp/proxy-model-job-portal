from django import forms
from django.contrib.auth.forms import UserCreationForm
# from account.models import CompanyProfile
from account.models import Profiles, CompanyAdditional


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Profiles
        fields = [
            "email",
            "date_of_birth",
            "first_name",
            "phone_number",
            "last_name",
            "password1",
            "password2",
        ]




        """
        if user wats to make a seprate register than this forms works well else goto from 2
        """
# class CompanyRegrastrationForm(UserCreationForm):
#     class Meta:
#         model = CompanyProfile
#         fields = [
#             "email",
#             "date_of_birth",
#             "first_name",
#             "last_name",
#             "password1",
#             "password2",
#         ]


class CompanyForm2(forms.ModelForm):
    class Meta:
        model = CompanyAdditional
        fields = [
            "company_name",
            "company_website",
            "company_address",
            "company_description",
        ]
