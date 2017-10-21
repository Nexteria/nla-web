from django.contrib import admin
from .models import Registracia
from django.shortcuts import HttpResponse


# Register your models here.

# Priezvisko; Meno; Email; Telefon; Skola; Sales kanal; Uspech; Datum registracie dd/mm/yyyy; Link na CV; Link na ML;


def export_student_list(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=nla_zoznam_studentov.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Priezvisko"),
        smart_str(u"Meno"),
        smart_str(u"Email"),
        smart_str(u"Telefon"),
        smart_str(u"Skola"),
        smart_str(u"Sales kanal"),
        smart_str(u"Uspech"),
        smart_str(u"Datum reg"),
        smart_str(u"CV"),
        smart_str(u"ML"),
    ])

    for obj in queryset:
        writer.writerow([
            smart_str(obj.priezvisko),
            smart_str(obj.meno),
            smart_str(obj.email),
            smart_str(obj.telefon),
            smart_str(obj.skola),
            smart_str(obj.ref),
            smart_str(obj.uspech),
            smart_str(obj.created_at),
            smart_str('http://nla.nexteria.sk/media/' + str(obj.cv)),
            smart_str('http://nla.nexteria.sk/media/' + str(obj.list)),
        ])
    return response


export_student_list.short_description = 'Exportuj vybratych studentov do zoznamu'


@admin.register(Registracia)
class RegAdmin(admin.ModelAdmin):
    list_display = ('meno', 'priezvisko', 'email', 'telefon', 'created_at', 'updated_at')

    actions = [export_student_list, ]
    list_per_page = 1000
