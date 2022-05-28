from django import forms
from django.contrib.auth.forms import UserCreationForm

# from account.models import CompanyProfile
from account.models import Profiles, CompanyAdditional
from django.contrib.auth import password_validation

from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=(
            forms.PasswordInput(
                attrs={"class": "p-1 outline-none", "placeholder": "Enter Password"}
            )
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password Confirmation"),
        widget=forms.PasswordInput(
            attrs={"class": "p-1 outline-none", "placeholder": "Enter Confrim Password"}
        ),
        help_text=_("Just Enter the same password, for confirmation"),
    )

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
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "p-1 outline-none", "placeholder": "Your@gmail.com"}
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "p-1 outline-none",
                    "placeholder": "Fist name",
                }
            ),
            "date_of_birth": forms.TextInput(
                attrs={
                    "class": "p-1 outline-none",
                    "placeholder": "yyyy-dd-mm",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "p-1 outline-none",
                    "placeholder": "last name ",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "p-1 outline-none",
                    "placeholder": "+977 00-0000-0000 ",
                }
            ),
            # "password1": forms.PasswordInput(
            #     attrs={
            #         "class": "p-1 outline-none",
            #         "placeholder": "password",
            #     }
            # ),
            # "password2": forms.PasswordInput(
            #     attrs={
            #         "class": "p-1 outline-none",
            #         "placeholder": "confrim password",
            #     }
            # ),
        }

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
