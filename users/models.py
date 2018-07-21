from django.db import models, transaction, DatabaseError
from django.utils import timezone as date
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Saves new user with email and password"""
        if not email:
            raise ValueError('The given email must be set')

        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)

                return user

        except DatabaseError:
            user.active = False

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Model for users with full features including admin permissions"""

    email = models.EmailField(max_length=40, unique=True)

    first_name = models.CharField(max_length=30, blank=True)
    second_name = models.CharField(max_length=30, blank=True)

    active = models.BooleanField(default=True)
    date_when_joined = models.DateTimeField(default=date.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name']
