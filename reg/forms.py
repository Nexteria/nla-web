# coding=utf-8

from django.forms import ModelForm
from django import forms
from .models import Registracia
from django.core.exceptions import ValidationError

class RegistraciaForm(ModelForm):

    class Meta:
        model = Registracia

        STUPNE_STUDIA = (('1', 'Stredná škola',), ('2', 'Maturitný ročník',), ('3', 'Bakalárske štúdium',), ('4', 'Magisterské štúdium',), ('5', 'Absolvent (PhD.)',))
        stupen_studia = forms.ChoiceField(widget=forms.Select(attrs={'id':'mf-degree'}), choices=STUPNE_STUDIA)

        fields = ['meno','priezvisko','email','telefon','uspech','stupen_studia','ref','skola','udaje','novinky']

        widgets = {
            'meno':forms.TextInput(attrs={'placeholder': 'Meno'}),
            'priezvisko':forms.TextInput(attrs={'placeholder': 'Priezvisko'}),
            'email':forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'telefon':forms.TextInput(attrs={'placeholder': 'Telefónne číslo'}),
            'uspech':forms.Textarea(attrs={'placeholder':'Čo je tvoj doterajší najväčší úspech, na ktorý si hrdý, a ktorý ťa odlišuje od ostatných? Aký je tvoj najväčší životný úspech?'}),
            'ref':forms.TextInput(attrs={'placeholder': 'Ako si sa o nás dozvedel'}),
            'skola':forms.TextInput(attrs={'placeholder': 'Názov aktuálnej školy'}),
            'udaje':forms.CheckboxInput(attrs={'required':True}),
            'novinky':forms.CheckboxInput(),
        }
        error_messages = {
            'meno': {
                'required': ('Položka meno je povinná.')
            },
            'priezvisko': {
                'required': ('Položka prievisko je povinná.')
            },
            'email': {
                'required': ('Položka email je povinná.')
            },
            'telefon': {
                'required': ('Položka telefónne číslo je povinná.')
            },
            'uspech': {
                'required': ('Položka s najväčším úspechom je povinná.')
            },
            'stupen_studia': {
                'required': ('Položka stupeň štúdia je povinná.')
            },
        }

class RegistraciaDruhyKrokForm(ModelForm):

    def clean_cv(self):
        cv = self.cleaned_data.get('cv', False)
        if cv:
            if cv._size > 2.5*1024*1024:
                raise ValidationError("CV súbor je príliš veľký ( > 2.5 MB )")
        return cv

    def clean_list(self):
        list = self.cleaned_data.get('list', False)
        if list:
            if list._size > 2.5*1024*1024:
                raise ValidationError("Súbor s listom je príliš veľký ( > 2.5 MB )")
        return list

    class Meta:
        model = Registracia

        cv = forms.FileField(label='CV')
        fields = ['cv', 'list']

        widgets = {
            'list': forms.FileInput(),
        }
        error_messages = {
            'cv': {
                'required': ('Položka CV je povinná.')
            },
            'list': {
                'required': ('Položka s motivačným listom je povinná.')
            },
        }


# class RegistrationForm(forms.Form):
#     meno = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Meno'}))
#     priezvisko = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Priezvisko'}))
#     email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
#     telefon = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Telefón'}))
#     uspech = forms.CharField(widget=forms.Textarea(attrs={'placeholder':
#               'Čo je tvoj doterajší najväčší úspech, na ktorý si hrdý, a ktorý ťa odlišuje od ostatných? Aký je tvoj najväčší životný úspech?'}))
#
#     cv = forms.FileInput(widget = forms.File)
#     list = forms.FileInput()
#
#     ref = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Ako si sa o nás dozvedel'}))
#     skola = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Názov školy'}))
#
#     udaje = forms.BooleanField(required= True)
#     novinky = forms.BooleanField(required=False)

