from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse
from App.models import User
from App.forms import RegistrationForm

import sys
from time import sleep
import urllib.request
import json
import ast

from firebase import firebase

from google.cloud import storage
from google.cloud.storage import client

#Pokpong Code
from App.thingspeak import Thingspeak
from App.sam_ml import predict, predict_melanomas

sam_station = Thingspeak("VEMUS670D5ZP2OLN", "5LT3QPFMB8XPVWEF")
"""sam_station1 = Thingspeak("4PQLXV7E0I6DB2GR", "NZCY0LG564J9TI9I")
sam_station2 = Thingspeak("CM68O9L3LWGYLNKJ", "UWKSVUO6AGI3J0WX")
sam_station3 = Thingspeak("7V3BALK6C1AI6J5I", "O3WIU241F54J1BR2")"""

print(sam_station.get_data())

client = storage.Client()
bucket = client.get_bucket('samtech-fibo.appspot.com')
blob = bucket.blob('my-test-file.png')
blob.upload_from_filename('App/static/img/SAM.png')

firebase2 = firebase.FirebaseApplication('https://samtech-fibo.firebaseio.com/')
led1 = firebase2.get('/led1', None)
tempp = firebase2.get('/temp', None)
"""print(led1)
print(tempp['ch01'])"""
ran=predict_melanomas()
#sam = [sam_station.get_data(),sam_station1.get_data(),sam_station2.get_data(),sam_station3.get_data()]
def index(request):
    return render(request, 'index.html')

def profile(request):
        context = {
                'sam_station': sam_station.get_data(),
                'create': sam_station.get_data()['created_at'],
                'f1': sam_station.get_data()['field1'],
                'f2': sam_station.get_data()['field2'],
                'f3': sam_station.get_data()['field3'],
                'f4': sam_station.get_data()['field4'],
                'f5': sam_station.get_data()['field5'],
                'patient': User.objects.filter(patient=1),
                'pamount': len(User.objects.filter(patient=1)),
                'ran': ran,
        }
        return render(request, 'profile.html', context)

def pregister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
                user = form.save(True, False)
                if form.data['gender'] == 'Male':
                        user.sex = 0
                else:
                        user.sex = 1
                user.save()
                context = {
                'sam_station': sam_station.get_data(),
                'create': sam_station.get_data()['created_at'],
                'f1': sam_station.get_data()['field1'],
                'f2': sam_station.get_data()['field2'],
                'f3': sam_station.get_data()['field3'],
                'f4': sam_station.get_data()['field4'],
                'f5': sam_station.get_data()['field5'],
                'h': sam_station.get_data()['field1'],
                'w': sam_station.get_data()['field2'],
                'risk': user.risk,
                'safe': user.safe,
                'patient': User.objects.filter(patient=1),
                'pamount': len(User.objects.filter(patient=1)),
                'ran': ran,
                }
                return render(request,'profile.html',context)
        else:
                form = RegistrationForm()
                return render(request,'pregister.html',{'form':form}) 
    else:
        form = RegistrationForm()
        return render(request,'pregister.html',{'form':form})

def mregister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
                user = form.save(False, True)
                if form.data['gender'] == 'Male':
                        user.sex = 0
                else:
                        user.sex = 1
                user.save()
                login(request, user)
                return render(request,'profile.html')
        else:
                form = RegistrationForm()
                return render(request,'mregister.html',{'form':form}) 
    else:
        form = RegistrationForm()
        return render(request,'mregister.html',{'form':form})


def plogin(request):
     if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
                user = form.get_user()
                if user.is_active and user.patient:
                        context = {
                                'u':user,
                                'username':user.username,
                                'sam_station': sam_station.get_data(),
                                'create': sam_station.get_data()['created_at'],
                                'f1': sam_station.get_data()['field1'],
                                'f2': sam_station.get_data()['field2'],
                                'f3': sam_station.get_data()['field3'],
                                'f4': sam_station.get_data()['field4'],
                                'f5': sam_station.get_data()['field5'],
                                'risk': user.risk,
                                'safe': user.safe,
                                'patient': User.objects.filter(patient=1),
                                'pamount': len(User.objects.filter(patient=1)),
                                'ran': ran,
                        }
                        login(request,user)
                        return render(request,'profile.html', context)
                elif user.is_active and not user.patient:
                        form = AuthenticationForm()
                        message = 'This User is not a Patient!'
                        context = {
                                'message': message,
                                'form': form,
                        }
                        return render(request,'plogin.html', context)
                else :
                        form = AuthenticationForm()
                        message = 'Invalid Username or Password!'
                        context = {
                                'message': message,
                                'form': form,
                        }
                        return render(request,'plogin.html', context)
        else :
                form = AuthenticationForm()
                message = 'Invalid Username or Password!'
                context = {
                                'message': message,
                                'form': form,
                        }
                return render(request,'plogin.html', context)
     else :
        form = AuthenticationForm()
        message = ''
        context = {
                                'message': message,
                                'form': form,
                        }
        return render(request,'plogin.html', context)

def mlogin(request):
     if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
                user = form.get_user()
                if user.is_active and user.medical:
                        context = {
                                'patient': User.objects.filter(patient=1,idd=user.id),
                                'pamount': len(User.objects.filter(patient=1,idd=user.id)),
                                'ran': ran,
                        }
                        login(request,user)
                        return render(request, "profile.html", context)
                elif user.is_active and not user.medical:
                        form = AuthenticationForm()
                        message = 'This User is not a Medical Personnel!'
                        context = {
                                'message': message,
                                'form': form,
                        }
                        return render(request,'mlogin.html', context)
                else :
                        form = AuthenticationForm()
                        message = 'Invalid Username or Password!'
                        context = {
                                'message': message,
                                'form': form,
                        }
                        return render(request,'mlogin.html', context)
        else :
                form = AuthenticationForm()
                message = 'Invalid Username or Password!'
                context = {
                                'message': message,
                                'form': form,
                        }
                return render(request,'mlogin.html', context)
     else :
        form = AuthenticationForm()
        message = ''
        context = {
                                'message': message,
                                'form': form,
                        }
        return render(request,'mlogin.html', context)

def profileview(request, username):
    u = User.objects.get(username=username)
    context = {
                'u': u,
                'username':u.username,
                'sam_station': sam_station.get_data(),
                'create': sam_station.get_data()['created_at'],
                'f1': sam_station.get_data()['field1'],
                'f2': sam_station.get_data()['field2'],
                'f3': sam_station.get_data()['field3'],
                'f4': sam_station.get_data()['field4'],
                'f5': sam_station.get_data()['field5'],
                'risk': u.risk,
                'safe': u.safe,
                'patient': User.objects.filter(patient=1),
                'pamount': len(User.objects.filter(patient=1)),
                'ran': ran,
        }
    return render(request, 'select.html', context)

def edit(request, username):
        u = User.objects.get(username=username)
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.data['cpt'] != '':
                        u.cpt = form.data['cpt']
                if form.data['rbp'] != '':
                        u.rbp = form.data['rbp']
                if form.data['sc'] != '':
                        u.sc = form.data['sc']
                if form.data['fbs'] != '':
                        u.fbs = form.data['fbs']
                if form.data['rer'] != '':
                        u.rer = form.data['rer']
                if form.data['mhra'] != '':
                        u.mhra = form.data['mhra']
                if form.data['eia'] != '':
                        u.eia = form.data['eia']
                if form.data['oldpeak'] != '':
                        u.oldpeak = form.data['oldpeak']
                if form.data['sotp'] != '':
                        u.sotp = form.data['sotp']
                if form.data['nomv'] != '':
                        u.nomv = form.data['nomv']
                if form.data['thal'] != '':
                        u.thal = form.data['thal']
                u.risk = predict([u.age,u.sex,form.data['cpt'],sam_station.get_data()['field3'],form.data['sc'],form.data['fbs'],form.data['rer'],sam_station.get_data()['field4'],form.data['eia'],form.data['oldpeak'],form.data['sotp'],form.data['nomv'],form.data['thal']])
                if u.risk == 0:
                        u.safe = 1
                else:
                        u.safe = 0
                u.save()
                context = {
                        'form':form,
                        'u': u,
                        'username':u.username,
                        'sam_station': sam_station.get_data(),
                        'create': sam_station.get_data()['created_at'],
                        'f1': sam_station.get_data()['field1'],
                        'f2': sam_station.get_data()['field2'],
                        'f3': sam_station.get_data()['field3'],
                        'f4': sam_station.get_data()['field4'],
                        'f5': sam_station.get_data()['field5'],
                        'risk': u.risk,
                        'safe': u.safe,
                        'patient': User.objects.filter(patient=1),
                        'pamount': len(User.objects.filter(patient=1)),
                        'ran': ran,
                        }
                return render(request, 'select.html', context)
        else:
                form = RegistrationForm()
                context = {
                        'form':form,
                        'u': u,
                        'username':u.username,
                        'sam_station': sam_station.get_data(),
                        'create': sam_station.get_data()['created_at'],
                        'f1': sam_station.get_data()['field1'],
                        'f2': sam_station.get_data()['field2'],
                        'f3': sam_station.get_data()['field3'],
                        'f4': sam_station.get_data()['field4'],
                        'f5': sam_station.get_data()['field5'],
                        'risk': u.risk,
                        'safe': u.safe,
                        'patient': User.objects.filter(patient=1),
                        'pamount': len(User.objects.filter(patient=1)),
                        'ran': ran,
                        }
                return render(request, 'edit.html', context)

def alarm(request, username):
        user = User.objects.get(username=username)
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.data['alarm'] != '' and len(form.data['alarm']) == 4:
                        user.alarm = form.data['alarm']
                        sam_station.write(6, form.data['alarm'])
                        user.save()
                        context = {
                        'form':form,
                        'user': user,
                        'username':user.username,
                        'sam_station': sam_station.get_data(),
                        'create': sam_station.get_data()['created_at'],
                        'f1': sam_station.get_data()['field1'],
                        'f2': sam_station.get_data()['field2'],
                        'f3': sam_station.get_data()['field3'],
                        'f4': sam_station.get_data()['field4'],
                        'f5': sam_station.get_data()['field5'],
                        'risk': user.risk,
                        'safe': user.safe,
                        'patient': User.objects.filter(patient=1),
                        'pamount': len(User.objects.filter(patient=1)),
                        'ran': ran,
                        }
                        return render(request, 'profile.html', context)
                else :
                        context = {
                        'form':form,
                        'user': user,
                        'username':user.username,
                        'sam_station': sam_station.get_data(),
                        'create': sam_station.get_data()['created_at'],
                        'f1': sam_station.get_data()['field1'],
                        'f2': sam_station.get_data()['field2'],
                        'f3': sam_station.get_data()['field3'],
                        'f4': sam_station.get_data()['field4'],
                        'f5': sam_station.get_data()['field5'],
                        'risk': user.risk,
                        'safe': user.safe,
                        'patient': User.objects.filter(patient=1),
                        'pamount': len(User.objects.filter(patient=1)),
                        'ran': ran,
                        }
                        return render(request, 'alarm.html', context)
        else:
                form = RegistrationForm()
                context = {
                        'form':form,
                        'user': user,
                        'username':user.username,
                        'sam_station': sam_station.get_data(),
                        'create': sam_station.get_data()['created_at'],
                        'f1': sam_station.get_data()['field1'],
                        'f2': sam_station.get_data()['field2'],
                        'f3': sam_station.get_data()['field3'],
                        'f4': sam_station.get_data()['field4'],
                        'f5': sam_station.get_data()['field5'],
                        'risk': user.risk,
                        'safe': user.safe,
                        'patient': User.objects.filter(patient=1),
                        'pamount': len(User.objects.filter(patient=1)),
                        'ran': ran,
                        }
                return render(request, 'alarm.html', context)