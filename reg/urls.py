"""nla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from reg import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^register/(?P<uuid>[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12})/final',
        views.RegisterFinalView.as_view(),
        name='registerFinal'),
    url(r'^hotovo', views.hotovo, name='hotovo'),
    url(r'^motivacny_list', views.motivacny_example, name='motivacny_example'),
    url(r'media/(?P<file>.*)', views.upload, name='media'),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'reg.views.error_view'
