# -*- coding: utf-8 -*-
from django import forms
from apps.users.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginTraditionalForm(forms.Form):
    username = forms.CharField(max_length=140, required=True)
    password = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={'type':'password'}))
    form = forms.CharField(required=False,widget=forms.TextInput(attrs={'type':'hidden','value':'login'}))
    
class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['email'].widget.attrs['placeholder'] = "Correo electrónico"
        self.fields['password1'].widget.attrs['placeholder'] = "Contraseña"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirmación"

    email = forms.EmailField(required=True)
    form = forms.CharField(required=False,widget=forms.TextInput(attrs={'type':'hidden','value':'register'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        exclude = ['first_name', 'last_name']

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("El Correo electrónico ya se encuentra registrado")
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user