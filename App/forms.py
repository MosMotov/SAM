from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction, models
from App.models import User

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (  
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'gender',
            'age',
            'h',
            'w',
            'station',
            'derma',
            'idd',
            'cpt',
            'rbp',
            'sc',
            'fbs',
            'rer',
            'mhra',
            'eia',
            'oldpeak',
            'sotp',
            'nomv',
            'thal',
            'alarm',
        )

    @transaction.atomic
    def save(self, patient, medical, commit = True):
        user = super(RegistrationForm,self).save(commit=False)
        user.patient = patient
        user.medical = medical
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.gender = self.cleaned_data['gender']
        user.age = self.cleaned_data['age']
        user.h = self.cleaned_data['h']
        user.w = self.cleaned_data['w']
        user.station = self.cleaned_data['station']
        user.derma = self.cleaned_data['derma']
        user.idd = self.cleaned_data['idd']
        user.cpt = self.cleaned_data['cpt']
        user.rbp = self.cleaned_data['rbp']
        user.sc = self.cleaned_data['sc']
        user.fbs = self.cleaned_data['fbs']
        user.rer = self.cleaned_data['rer']
        user.mhra = self.cleaned_data['mhra']
        user.eia = self.cleaned_data['eia']
        user.oldpeak = self.cleaned_data['oldpeak']
        user.sotp = self.cleaned_data['sotp']
        user.nomv = self.cleaned_data['nomv']
        user.thal = self.cleaned_data['thal']
        user.alarm = self.cleaned_data['alarm']
        if commit:
            user.save()

        return user
