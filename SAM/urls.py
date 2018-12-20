"""SAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from App.views import index, profile, plogin, mlogin, pregister, mregister, profileview, edit, alarm

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/logout', include('django.contrib.auth.urls'), name='logout'),
    url(r'^Profile/', profile, name='profile'),
    url(r'^PatientLogin/', plogin, name='plogin'),
    url(r'^MedicalLogin/', mlogin, name='mlogin'),
    url(r'^AddPatient/', pregister, name='pregister'),
    url(r'^MedicalRegister/', mregister, name='mregister'),
    url(r'^ProfileView/(?P<username>\w+)/$', profileview, name='profile_view'),
    url(r'^Edit/(?P<username>\w+)/$', edit, name='edit'),
    url(r'^Alarm/(?P<username>\w+)/$', alarm, name='alarm'),
]
