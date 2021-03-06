from django.db import models
from django.conf import settings


class Profile(models.Model):
    _genders = (
        ('M', 'Male',),
        ('F', 'Female',),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=_genders)


    def __str__(self):
        return '{}'.format(self.pk)

