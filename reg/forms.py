# coding=utf-8

from django.forms import ModelForm
from django import forms
from .models import Registracia
from django.core.exceptions import ValidationError


class RegistraciaForm(ModelForm):
    class Meta:
        model = Registracia

        STUPNE_STUDIA = (('1', 'Stredná škola',), ('2', 'Maturitný ročník',), ('3', 'Bakalárske štúdium',),
                         ('4', 'Magisterské štúdium',), ('5', 'Absolvent (PhD.)',))
        stupen_studia = forms.ChoiceField(widget=forms.Select(attrs={'id': 'mf-degree'}), choices=STUPNE_STUDIA)

        fields = ['meno', 'priezvisko', 'email', 'telefon', 'stupen_studia', 'ref', 'skola', 'udaje', 'novinky']

        widgets = {
            'meno': forms.TextInput(attrs={'placeholder': 'Meno'}),
            'priezvisko': forms.TextInput(attrs={'placeholder': 'Priezvisko'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'telefon': forms.TextInput(attrs={'placeholder': 'Telefónne číslo'}),
            'ref': forms.TextInput(attrs={'placeholder': 'Ako si sa o nás dozvedel/a'}),
            'skola': forms.TextInput(attrs={'placeholder': 'Názov aktuálnej školy'}),
            'udaje': forms.CheckboxInput(attrs={'required': True}),
            'novinky': forms.CheckboxInput(),
        }
        error_messages = {
            'meno': {
                'required': 'Položka meno je povinná.'
            },
            'priezvisko': {
                'required': 'Položka prievisko je povinná.'
            },
            'email': {
                'required': 'Položka email je povinná.'
            },
            'telefon': {
                'required': 'Položka telefónne číslo je povinná.'
            },
            'stupen_studia': {
                'required': 'Položka stupeň štúdia je povinná.'
            },
            'ref': {
                'required': 'Táto položka je povinná.',
            },
            'skola': {
                'required': 'Položka škola je povinná.',
            },
        }


class RegistraciaDruhyKrokForm(ModelForm):
    def clean_cv(self):
        cv = self.cleaned_data.get('cv', False)
        if cv:
            if cv._size > 2.5 * 1024 * 1024:
                raise ValidationError("CV súbor je príliš veľký ( > 2.5 MB )")
        return cv

    class Meta:
        model = Registracia

        cv = forms.FileField(label='CV')
        fields = ['cv', 'uspech', 'smerovanie', 'okolie', 'ocakavanie']

        widgets = {
            'uspech': forms.Textarea(attrs={
                'soft_limit': Registracia.QUESTION_SOFT_LIMIT_WORDS,
                'placeholder':
                    'Buď prosím konkrétny/a a pomenuj pokojne 2-3 situácie.'}),
            'smerovanie': forms.Textarea(attrs={
                'soft_limit': Registracia.QUESTION_SOFT_LIMIT_WORDS,
                'placeholder':
                    'Napíš nám, v akej oblasti alebo oblastiach sa chceš po/popri škole uplatniť. '
                    'Vlastné podnikanie, zamestnanie, neziskovka, verejný sektor? Alebo čokoľvek iné.'}),
            'okolie': forms.Textarea(attrs={
                'soft_limit': Registracia.QUESTION_SOFT_LIMIT_WORDS,
                'placeholder':
                    'Zaujíma nás, na ktorej téme/témach Ti záleží a ako konkrétne chceš prispieť '
                    '(alebo už prispievaš) k pozitívnej zmene svojho okolia.'}),
            'ocakavanie': forms.Textarea(attrs={
                'soft_limit': Registracia.QUESTION_SOFT_LIMIT_WORDS,
                'placeholder':
                    'Ako Ti vieme pomôcť, v čom sa chceš rozvíjať a ako by si to, čo u nás získaš, '
                    'vedel/a využiť vo svojom živote a v prospech svojho okolia.'}),
        }
        error_messages = {
            'uspech': {
                'max_words': 'Pokús sa prosím svoju myšlienku vyjadriť trochu stručnejšie.'
            },
            'smerovanie': {
                'max_words': 'Pokús sa prosím svoju myšlienku vyjadriť trochu stručnejšie.'
            },
            'okolie': {
                'max_words': 'Pokús sa prosím svoju myšlienku vyjadriť trochu stručnejšie.'
            },
            'ocakavanie': {
                'max_words': 'Pokús sa prosím svoju myšlienku vyjadriť trochu stručnejšie.'
            },
        }
