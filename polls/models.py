# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserProfileManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    # user_group = models.ManyToManyField(UserGroup,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_group = models.ForeignKey('UserGroup',blank=True,null=True)
    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class UserGroup(models.Model):
    group_name =  models.CharField(max_length=30,unique=True)
    description = models.TextField()
    def __unicode__(self):
        return self.group_name



class Server(models.Model):
    server_name = models.CharField(max_length=64 , verbose_name=u'服务器名')
    ip = models.GenericIPAddressField(verbose_name=u'地址')

    def __unicode__(self):
        return self.server_name
    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"