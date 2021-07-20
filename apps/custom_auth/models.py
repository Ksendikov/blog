from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True,
        max_length=30,
    )
    email = models.EmailField(blank=True, null=True)

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_superuser = models.BooleanField(
        default=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'username'
        verbose_name_plural = 'usernames'
        abstract = False

