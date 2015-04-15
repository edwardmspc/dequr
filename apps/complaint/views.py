from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/single_page.html')

class PostView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/post_page.html')

class StepOneView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/step_one.html')

class StepTwoView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/step_two.html')

class CategoryView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/category.html')

class ProfileView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/profile.html')
