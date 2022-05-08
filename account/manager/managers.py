from django.contrib.auth.models import BaseUserManager


class ProfilesManager(BaseUserManager):
    def create_user(self, email, date_of_birth, last_name, first_name, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, date_of_birth, last_name, first_name, password=None
    ):

        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True   
        user.save(using=self._db)
        return user
