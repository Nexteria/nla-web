# -*- coding: utf-8 -*-
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


def max_words(words=400):
    def validator(value):
        wslen = len(value.split())
        if wslen > words:
            raise ValidationError('Presiahnutý limit slov: %(current_words)s/%(max_words)s',
                                  params={'current_words': wslen, 'max_words': words},
                                  code='max_words')
    return validator


@python_2_unicode_compatible
class Registracia(models.Model):
    meno = models.CharField(max_length=100 )
    priezvisko = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefon = models.CharField(max_length=15)

    QUESTION_SOFT_LIMIT_WORDS = 200
    QUESTION_HARD_LIMIT_WORDS = 400

    uspech = models.TextField(validators=[max_words(QUESTION_HARD_LIMIT_WORDS)])
    smerovanie = models.TextField(validators=[max_words(QUESTION_HARD_LIMIT_WORDS)])
    okolie = models.TextField(validators=[max_words(QUESTION_HARD_LIMIT_WORDS)])
    ocakavanie = models.TextField(validators=[max_words(QUESTION_HARD_LIMIT_WORDS)])

    list = models.FileField(null=True, upload_to='uploads/list/')

    token = models.UUIDField(default=uuid.uuid4, editable=False)

    cv = models.FileField(upload_to='uploads/cv/', blank=True)

    ref = models.CharField(max_length=500)
    skola = models.CharField(max_length=500)

    STUPNE_STUDIA = (('1', 'Stredná škola',), ('2', 'Maturitný ročník',), ('3', 'Bakalárske štúdium',), ('4', 'Magisterské štúdium',), ('5', 'Absolvent (PhD.)',))
    stupen_studia = models.CharField(max_length=1, choices=STUPNE_STUDIA, null=True)

    udaje = models.BooleanField()
    novinky = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meno + ' ' + self.priezvisko
