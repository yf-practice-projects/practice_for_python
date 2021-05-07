from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone


class UserManager(UserManager):
    def create_user(self, username, email, password=None,is_superuser=False, is_staff=False, is_admin=False):
        if not username:
            raise ValueError('Users must have an username')
        elif not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, is_superuser=False, is_staff=False, is_admin=False):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            is_superuser=True,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        """ユーザーモデル"""
        db_table = 'accounts'
        verbose_name = _('username')
    
    username = models.CharField(_('username'),max_length=255, unique=True)

    email = models.EmailField(_('email address'), unique=True)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

