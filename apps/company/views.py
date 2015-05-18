# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from apps.category.models import Category, SubCategory


class CategorysView(View):
    def get(self, request,  *args, **kwargs):
        ul = []
        for cat in Category.objects.all():
            if SubCategory.objects.filter(category=cat).count() > 0:
                q = SubCategory.objects.filter(category=cat).order_by('name')
                for item in q:
                    li = {
                        'category': cat.name,
                        'cat_slug': cat.slug,
                        'sub_category': item.name,
                        'sub_slug': item.slug,
                    }
                    ul.append(li)
            else:
                li = {
                    'category': cat.name,
                    'cat_slug': cat.slug,
                    'sub_category': "",
                    'sub_slug': "",
                }
                ul.append(li)
        return render(request, 'company/all_category.html', {'categorys': ul, })


class CategoryView(View):
    def get(self, request, slug=None,  *args, **kwargs):
        print slug
        if slug:
            if Category.objects.filter(slug=slug).exists():
                li = Category.objects.get(slug=slug,)
                return render(request, 'company/single_category.html', {
                    'data': li, })
            elif SubCategory.objects.filter(slug=slug).exists():
                li = SubCategory.objects.get(slug=slug,)
                return render(request, 'company/single_category.html', {
                    'data': li, })
            else:
                raise Http404
        else:
            raise Http404
