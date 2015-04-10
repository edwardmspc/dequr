from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/single_page.html')

class PostView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/post_page.html')
