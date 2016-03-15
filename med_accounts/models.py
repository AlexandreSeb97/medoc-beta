from __future__ import unicode_literals
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

from django.db import models

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, name=None, owner_first_name=None, owner_last_name=None, email=None, password=None, country=None, specialite=None):
        """
        Creates and saves a User with a name, email, country, password and specialite
        """
        if not name:
            raise ValueError('Must have an username')
        if not owner_first_name:
            raise ValueError('Must include a first name')
        if not owner_last_name:
            raise ValueError('Must include a last name')
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            name=name,
            owner_first_name=owner_first_name,
            owner_last_name=owner_last_name,
            email=self.normalize_email(email),
            country=country,
            specialite=specialite,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, owner_first_name, owner_last_name, email, password, country, specialite):
        """
Create and save a superuser
        """
        user = self.create_user(
            name=name,
            owner_first_name=owner_first_name,
            owner_last_name=owner_last_name,
            email=email,
            password=password,
            country=country,
            specialite=specialite,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyDoctor(AbstractBaseUser):
    name = models.CharField(max_length=255, unique=True,)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    country = models.CharField(max_length=255,)
    specialite = models.CharField(max_length=255,)
    owner_first_name = models.CharField(max_length=120,)
    owner_last_name = models.CharField(max_length=120,)
    is_member = models.BooleanField(default=False, verbose_name='Is Paid Member')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email', 'country', 'specialite']

    def get_full_name(self):
        # The user is identified by their email address
        return "%s %s" %(self.owner_first_name, self.owner_last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.owner_first_name

    def __str__(self):
        return self.name

    def get_country(self):
        return self.country

    def get_specialite(self):
        return self.specialite

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


class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    patient_first_name = models.CharField(max_length=100)
    patient_last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=255, unique=True,)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    created_by = models.CharField(max_length=255, default='Not Created')
    requested_doc = models.CharField(max_length=255, default='No Doctor Yet')

    def __str__(self):
        return self.patient_last_name

