import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from apps.company.models import (Company, SubCompany)
from apps.category.models import (Category, SubCategory)


class IndexView(View):
    def get(self, request,  *args, **kwargs):

        if request.is_ajax():
            if request.GET.get('convert_to_father', None):
                subcompany_id = request.GET.get('convert_to_father', None)
                child = SubCompany.objects.get(id=subcompany_id)
                parent = Company(name=child.name)
                parent.save()
                child.delete()
                data = {}
                mimetype = 'application/json'
                return HttpResponse(data, mimetype)

            if request.GET.get('hide_asignadas', None) == '1':
                subcompanys = SubCompany.objects.filter(company=None)[:3]
                results = []
                for subcompany in subcompanys:
                    subcompany_json = {}
                    subcompany_json['id'] = subcompany.id
                    subcompany_json['name'] = subcompany.name
                    results.append(subcompany_json)
                data = json.dumps(results)
                mimetype = 'application/json'
                return HttpResponse(data, mimetype)
            elif request.GET.get('hide_asignadas', None) == '0':
                subcompanys = SubCompany.objects.all()
                results = []
                for subcompany in subcompanys:
                    subcompany_json = {}
                    subcompany_json['id'] = subcompany.id
                    subcompany_json['name'] = subcompany.name
                    results.append(subcompany_json)
                data = json.dumps(results)
                mimetype = 'application/json'
                return HttpResponse(data, mimetype)
        else:
            company = Company.objects.all()
            subcompany = SubCompany.objects.all()[:100]
            return render(request, 'adminpanel/inicio.html', {
                'subcompanys': subcompany, 'companys': company, })
