from django.db import models
from django.db.models import Q
class CompanyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        from account.models import Profiles
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(Q(user_type__contains=Profiles.ProfileType.Company))
        )


class ApplicantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        from account.models import Profiles
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(Q(user_type__contains=Profiles.ProfileType.Applicant))
        )

