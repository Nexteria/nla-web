# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registracia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meno', models.CharField(max_length=100)),
                ('priezvisko', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefon', models.CharField(max_length=15)),
                ('uspech', models.TextField()),
                ('cv', models.FileField(upload_to='uploads/cv/')),
                ('list', models.FileField(upload_to='uploads/list/')),
                ('ref', models.CharField(blank=True, max_length=500, null=True)),
                ('skola', models.CharField(blank=True, max_length=500, null=True)),
                ('udaje', models.BooleanField()),
                ('novinky', models.BooleanField()),
            ],
        ),
    ]
