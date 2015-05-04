# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginTraditionalForm, UserCreateForm
from django.core.urlresolvers import reverse

class SettingView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'users/setting.html')

class SettingBissView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'users/setting_biss.html')

class MyCommentsView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'users/my_comments.html')    

class MyComplaintView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'users/my_complaints.html')                

class LoginIndex(View):
    def get(self, request,  *args, **kwargs):
        login_form = LoginTraditionalForm()
        register_form = UserCreateForm()
        return render(request, 'users/login-register-social.html', {'login_form':login_form,'register_form':register_form,})

    def post(self, request,  *args, **kwargs):
        login_error = None
        login_form = LoginTraditionalForm()
        register_form = UserCreateForm()

        if 'register' in request.POST["form"]:
            register_form = UserCreateForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                user = authenticate(username=request.POST['username'],
                    password=request.POST['password1'])
                login(request, user)
                return redirect(reverse("general:index"))

        elif 'login' in request.POST["form"]:
            login_form = LoginTraditionalForm(request.POST)
            if login_form.is_valid():
                user = authenticate(username=request.POST['username'],
                    password=request.POST['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(reverse("general:index"))
                    else:
                        login_error = "* El usuario se encuentra inactivo"
                else:
                    login_error = "* El usuario o contraseña son incorrectos"
        return render(request, 'users/login-register-social.html', {'login_form':login_form,
            'register_form':register_form, 'login_error':login_error,})
        
class RequiredEmailView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'users/required_email.html')

    def post(self, request,  *args, **kwargs):
        request.session['saved_email'] = request.POST['email']
        backend = request.session['partial_pipeline']['backend']
        url = "/complete/%s/" % backend
        return redirect(url)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')