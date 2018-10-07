"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from boards import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^thank', views.thank, name='thank'),
    url(r'^admin/', admin.site.urls),
    url(r'^Rotract', views.Rotract, name='Rotract'),
    url(r'^d42', views.d42, name='d42'),
    url(r'^CSI', views.CSI, name='CSI'),
    url(r'^NSS', views.NSS, name='NSS'),
    url(r'^Ecell', views.Ecell, name='Ecell'),
    url(r'^IEEE', views.IEEE, name='IEEE'),
    url(r'^Parchhayi', views.Parchhayi, name='Parchhayi'),
    url(r'^Aahvaan', views.Aahvaan, name='Aahvaan'),
    url(r'^contact', views.contact, name='contact'),
]