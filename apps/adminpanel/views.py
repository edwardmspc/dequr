import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from apps.company.models import (Company, SubCompany)
from apps.category.models import (Category, SubCategory)


class AJAXChangeFacebookView(View):
    def get(self, request,  *args, **kwargs):
        #if request.is_ajax():
        if True:
            company_id = request.GET.get('company', None)
            facebook_string = request.GET.get('facebook', None)
            company = Company.objects.get(id=company_id)
            company.facebook = facebook_string
            company.save()
            data = {}
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)


class AJAXChangeTwitterView(View):
    def get(self, request,  *args, **kwargs):
        #if request.is_ajax():
        if True:
            company_id = request.GET.get('company', None)
            twitter_string = request.GET.get('twitter', None)
            company = Company.objects.get(id=company_id)
            company.twitter = twitter_string
            company.save()
            data = {}
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)


class AJAXChangeWebUrlView(View):
    def get(self, request,  *args, **kwargs):
        #if request.is_ajax():
        if True:
            company_id = request.GET.get('company', None)
            web_url_string = request.GET.get('web_url', None)
            company = Company.objects.get(id=company_id)
            company.web_url = web_url_string
            company.save()
            data = {}
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)


class AJAXChangePhoneView(View):
    def get(self, request,  *args, **kwargs):
        #if request.is_ajax():
        if True:
            company_id = request.GET.get('company', None)
            phone_string = request.GET.get('phone', None)
            company = Company.objects.get(id=company_id)
            company.phone = phone_string
            company.save()
            data = {}
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)


class AJAXChangeEmailView(View):
    def get(self, request,  *args, **kwargs):
        #if request.is_ajax():
        if True:
            company_id = request.GET.get('company', None)
            email_string = request.GET.get('email', None)
            company = Company.objects.get(id=company_id)
            company.email = email_string
            company.save()
            data = {}
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)


class AJAXChangeSubCategoryView(View):
    def get(self, request,  *args, **kwargs):
        #if request.is_ajax():
        if True:
            company_id = request.GET.get('company', None)
            category_id = request.GET.get('category', None)
            company = Company.objects.get(id=company_id)
            subcategory = SubCategory.objects.get(id=category_id)
            company.subcategory = subcategory
            company.save()
            data = {}
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)


class AJAXChangeCategoryView(View):
    def get(self, request,  *args, **kwargs):
        #if request.is_ajax():
        if True:
            company_id = request.GET.get('company', None)
            category_id = request.GET.get('category', None)
            company = Company.objects.get(id=company_id)
            category = Category.objects.get(id=category_id)
            company.category = category
            company.subcategory = None
            company.save()
            data = {}
            mimetype = 'application/json'
            return HttpResponse(data, mimetype)


class ParentView(View):
    def get(self, request,  *args, **kwargs):
        company = Company.objects.all()
        category = Category.objects.all()
        subcategory = SubCategory.objects.all()
        return render(request, 'adminpanel/parent.html', {
                               'companys': company, 'categorys': category,
                               'subcategorys': subcategory, })


class IndexView(View):
    def get(self, request,  *args, **kwargs):

        if request.is_ajax():
            if request.GET.get('delete_child', None):
                subcompany_id = request.GET.get('delete_child', None)
                child = SubCompany.objects.get(id=subcompany_id)
                child.delete()
                data = {}
                mimetype = 'application/json'
                return HttpResponse(data, mimetype)

            if request.GET.get('convert_to_father', None):
                subcompany_id = request.GET.get('convert_to_father', None)
                child = SubCompany.objects.get(id=subcompany_id)
                parent = Company(name=child.name)
                parent.save()
                child.delete()
                results = []
                for company in Company.objects.all():
                    company_json = {}
                    company_json['id'] = company.id
                    company_json['name'] = company.name
                    results.append(company_json)
                data = json.dumps(results)
                mimetype = 'application/json'
                return HttpResponse(data, mimetype)

            if request.GET.get('checkbox_masive', None) and \
               request.GET.get('select_masive', None):
                company_id = request.GET.get('select_masive', None)
                subcompany_ids = request.GET.get('checkbox_masive', None)
                subcompany_ids = subcompany_ids.split(",")
                parent = Company.objects.get(id=company_id)
                for x in subcompany_ids:
                    child = SubCompany.objects.get(id=x)
                    child.company = parent
                    child.save()
                data = {}
                mimetype = 'application/json'
                return HttpResponse(data, mimetype)

            if request.GET.get('create_fahter', None):
                q = request.GET.get('create_fahter', None)
                if not Company.objects.filter(name=q).exists():
                    parent = Company(name=q)
                    parent.save()
                results = []
                for company in Company.objects.all():
                    company_json = {}
                    company_json['id'] = company.id
                    company_json['name'] = company.name
                    results.append(company_json)
                data = json.dumps(results)
                mimetype = 'application/json'
                return HttpResponse(data, mimetype)

            if request.GET.get('search', None):
                q = request.GET.get('search', None)
                subcompanys = SubCompany.objects.all().filter(company=None)
                subcompanys = subcompanys.filter(name__icontains=q)
                results = []
                for subcompany in subcompanys:
                    subcompany_json = {}
                    subcompany_json['id'] = subcompany.id
                    subcompany_json['name'] = subcompany.name
                    results.append(subcompany_json)

                results2 = []
                for company in Company.objects.all():
                    company_json = {}
                    company_json['id'] = company.id
                    company_json['name'] = company.name
                    results2.append(company_json)
                final = {'q': results, 'company': results2}
                data = json.dumps(final)
                mimetype = 'application/json'
                return HttpResponse(data, mimetype)
        else:
            company = Company.objects.all()
            subcompany = SubCompany.objects.all().filter(company=None)
            companys_count = subcompany.count()
            subcompany = subcompany[:100]
            return render(request, 'adminpanel/inicio.html', {
                'subcompanys': subcompany, 'companys_count': companys_count,
                'companys': company, })
