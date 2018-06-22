from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    is_admin = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

    phone_number = models.PositiveIntegerField(
        _('phone number'),
        unique=True,
        error_messages={
            'unique': _("A user with that phone number already exists."),
        })
    fullname = models.CharField(_('fullname'), max_length=200)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['fullname', 'business_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Return the fullname
        """
        return self.fullname


class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    business_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'admin'
        verbose_name_plural = 'admins'

    def __str__(self):
        return self.user.fullname


class Agent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='agents')

    class Meta:
        verbose_name = 'agent'
        verbose_name_plural = 'agents'

    def __str__(self):
        return self.user.fullname
