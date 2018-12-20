from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    patient = models.BooleanField(default=False)
    medical = models.BooleanField(default=False)
    gender = models.CharField(max_length=6)
    age = models.IntegerField(default=0)
    h = models.IntegerField(default=0,null=True, blank=True)
    w = models.IntegerField(default=0,null=True, blank=True)
    idd = models.IntegerField(default=0,null=True, blank=True)
    station = models.BooleanField(default=False, blank=True)
    derma = models.BooleanField(default=False, blank=True)
    cpt = models.IntegerField(null=True, blank=True)
    rbp = models.IntegerField(null=True, blank=True)
    sc = models.IntegerField(null=True, blank=True)
    fbs = models.IntegerField(null=True, blank=True)
    rer = models.IntegerField(null=True, blank=True)
    mhra = models.IntegerField(null=True, blank=True)
    eia = models.IntegerField(null=True, blank=True)
    oldpeak = models.IntegerField(null=True, blank=True)
    sotp = models.IntegerField(null=True, blank=True)
    nomv = models.IntegerField(null=True, blank=True)
    thal = models.IntegerField(null=True, blank=True)
    alarm = models.IntegerField(default=0, null=True, blank=True)
    sex = models.BooleanField(default=False, blank=True)
    risk = models.BooleanField(default=False, blank=True)
    safe = models.BooleanField(default=False, blank=True)