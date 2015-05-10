# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from .models import Category, SubCategory


class CategorysView(View):
    def get(self, request,  *args, **kwargs):
        data = {}
        ul = []
        for cat in Category.objects.all():
            if SubCategory.objects.filter(category=cat).count() > 0:
                for item in SubCategory.objects.filter(category=cat).order_by('name'):
                    li = {
                        'id': item.id,
                        'subcategory': item.name,
                        'category': cat.name,
                    }
                    ul.append(li)
            else:
                li = {
                    'id': "",
                    'subcategory': "",
                    'category': cat.name,
                    }
                ul.append(li)
            #data[cat.name] = ul
        return render(request, 'company/category_list.html', {'categorys': ul, })


class CategoryView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'company/category.html')
