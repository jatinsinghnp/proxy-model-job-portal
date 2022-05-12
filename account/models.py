from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from account.manager.managers import ProfilesManager
from account.manager.proxyusermanager import CompanyManager, ApplicantManager
from multiselectfield import MultiSelectField

# Create your models here.


class Profiles(AbstractBaseUser):
    class ProfileType(models.TextChoices):
        Company = "Company", _("Company")
        Applicant = "Applicant", _("Applicant")
    
    email = models.EmailField(_("email"), max_length=254, unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,10}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # Validators should be a list

    first_name = models.CharField(_("fname"), max_length=50)
    last_name = models.CharField(_("lname"), max_length=50)
    profile_image = models.ImageField(
        _("imagfields"),
        upload_to=None,
        height_field=None,
        width_field=None,
        max_length=None,
    )

    # default type
    default_user_type = ProfileType.Applicant
    # user type

    """
      
        # the draw back is it's can allows the user to make only one account one at  a its type 
    """

    # user_type = models.CharField(
    #     _("user_type"),
    #     max_length=50,
    #     choices=ProfileType.choices,
    #     default=default_user_type,
    # )

    """ to generate the conflict that user cannot sing in with  same id at multiple type i addd the multiselect field so the it can resolve the issue"""

    user_type = MultiSelectField(
        choices=ProfileType.choices, default=[], null=True, blank=True
    )

    date_of_birth = models.DateField(_("DOB"), auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(_("is_active"), default=True)
    is_admin = models.BooleanField(_("is_admin"), default=False)
    is_staff = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_superadmin = models.BooleanField(default=False)
    objects = ProfilesManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth", "first_name", "last_name"]

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("first_name"),
                Lower("last_name").desc(),
                name="first_last_name_unique",
            ),
        ]
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    def save(self, *args, **kwargs):
        if not self.id:
            self.user_type.append(self.default_user_type)
        return super().save(*args, **kwargs)


class ApplicantAdditional(models.Model):
    applicant_id = models.AutoField(primary_key=True)
    applicant_profile = models.OneToOneField(
        Profiles, on_delete=models.CASCADE, null=True, blank=True
    )

    applicant_address = models.CharField(max_length=50, blank=False, null=False)
    applicant_qualification = models.TextField()
    applicant_description = models.TextField()

    def __str__(self) -> str:
        return self.applicant_profile.first_name


class CompanyAdditional(models.Model):
    profile = models.OneToOneField(
        Profiles, on_delete=models.CASCADE, blank=True, null=True
    )
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=220)
    company_website = models.CharField(max_length=220, blank=False, null=False)
    company_address = models.CharField(max_length=220, blank=False, null=False)
    company_description = models.TextField()

    def __str__(self) -> str:
        return self.company_name


# user models for company
class CompanyProfile(Profiles):
    default_user_type = Profiles.ProfileType.Company
    objects = CompanyManager()

    class Meta:
        proxy = True

    def postjob(self):
        print("I post ")

    @property
    def showAdditional(self):
        return self.CompanyAdditional


# user models for Applicant
class ApplicantProfile(Profiles):
    default_user_type = Profiles.ProfileType.Applicant
    objects = ApplicantManager()

    class Meta:
        proxy = True

    def applyjob(self):
        print("I can apply")

    @property
    def showAdditional(self):
        return self.ApplicantAdditional
