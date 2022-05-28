from django import forms

from account.models import Profiles
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Profiles
        fields = (
            "email",
            "date_of_birth",
            "first_name",
            "last_name",
        )
       

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profiles
        fields = ("email", "password", "date_of_birth", "is_active", "is_admin")


class LogInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.widgets.TextInput(
            attrs={"class": "outline-none p-2", "placeholder": "email"}
        )
        self.fields["password"].widget = forms.widgets.PasswordInput(
            attrs={"class": "outline-none p-2", "placeholder": "password"}
        )
