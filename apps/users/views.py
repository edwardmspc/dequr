from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View


class LoginIndex(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'users/login-register-social.html')

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