import os

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.generic import View
from django.utils.encoding import smart_str

from infinario import Infinario

from reg.forms import RegistraciaForm, RegistraciaDruhyKrokForm
from reg.models import Registracia
# Create your views here.


def index(req):
    return render(req, "index.html")


class RegisterView(View):

    def get(self, req):
        form = RegistraciaForm()
        return render(req, "register_zaciatok.html", {'form': form})

    def post(self, req):
        form = RegistraciaForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            if settings.EXPONEA_TRACK_REGISTRATION:
                client = Infinario(settings.EXPONEA_TOKEN, target=settings.EXPONEA_TARGET)

                client.identify(req.POST['email'])
                client.update({
                    'first_name': req.POST['meno'],
                    'last_name': req.POST['priezvisko'],
                    'email': req.POST['email'],
                    'token': str(form.instance.token)
                })
                client.track('registration_first_part')
            return HttpResponseRedirect(reverse('registerFinal', kwargs={'uuid': form.instance.token}))

        return render(req, "register_zaciatok.html", {'form':form})


class RegisterFinalView(View):
    def get(self, req, uuid):
        try:
            registracia = Registracia.objects.get(token=uuid)
        except Registracia.DoesNotExist:
            return HttpResponseRedirect(reverse('index'))

        form = RegistraciaDruhyKrokForm(instance=registracia)
        return render(req, "register_final.html", {'form': form})


    def post(self, req, uuid):
        try:
            registracia = Registracia.objects.get(token=req.POST.get("token", "x"))
        except Registracia.DoesNotExist:
            return HttpResponseRedirect(reverse('index'))

        form = RegistraciaDruhyKrokForm(req.POST, req.FILES, instance=registracia)
        if form.is_valid():
            form.save()
            client = Infinario(settings.EXPONEA_TOKEN, target=settings.EXPONEA_TARGET)
            client.identify(registracia.email)
            client.track('registration_documets_uploaded')
            return HttpResponseRedirect(reverse('hotovo'))

        return render(req, "register_final.html", {'form':form})


def hotovo(req):
    return render(req, "hotovo.html")


def motivacny_example(req):
    return render(req, "motivacny_example.html")


def error_view(req):
    return render(req, "error.html")


def upload(req, file):
    if req.user.is_authenticated():

        response = HttpResponse(mimetype='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file)
        response['X-Sendfile'] = smart_str(os.path.join(settings.MEDIA_ROOT, file))
        # It's usually a good idea to set the 'Content-Length' header too.
        # You can also set any other required headers: Cache-Control, etc.
        return response
    else:
        return HttpResponseRedirect(reverse('index'))

