from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import Profiles, CompanyProfile, ApplicantProfile
from account.form.forms import UserChangeForm, UserCreationForm

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("email", "date_of_birth", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("date_of_birth", "user_type")}),
        ("Permissions", {"fields": ("is_admin", "is_active", "is_staff")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "date_of_birth",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(Profiles, UserAdmin)
admin.site.register(CompanyProfile)
admin.site.register(ApplicantProfile)

admin.site.unregister(Group)
