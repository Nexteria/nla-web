# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Registracia(models.Model):
    meno = models.CharField(max_length=100 )
    priezvisko = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefon = models.CharField(max_length=15 )
    uspech = models.TextField()
    token = models.UUIDField(default=uuid.uuid4, editable=False)

    cv = models.FileField(upload_to='uploads/cv/')
    list = models.FileField(upload_to='uploads/list/')

    ref = models.CharField(max_length=500, blank=True, null=True)
    skola = models.CharField(max_length=500, blank=True, null=True)

    STUPNE_STUDIA = (('1', 'Stredná škola',), ('2', 'Maturitný ročník',), ('3', 'Bakalárske štúdium',), ('4', 'Magisterské štúdium',), ('5', 'Absolvent (PhD.)',))
    stupen_studia = models.CharField(max_length=1, choices=STUPNE_STUDIA, null=True)

    udaje = models.BooleanField()
    novinky = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meno + ' ' + self.priezvisko
