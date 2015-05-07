# -*- coding: utf-8 -*-
import json
import ast
from dequr import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from apps.company.models import Company, SubCategory, Category
from apps.complaint.models import Complaint, ComplaintContact, ComplaintLocation, ComplaintRequest, ItemFiles
from formtools.wizard.views import SessionWizardView
from .forms import CreateComplaintStepOneForm, CreateComplaintStepTwoForm, AjaxUploadForm
from django.core.files.storage import FileSystemStorage
from dequr import settings
from django.core.urlresolvers import reverse
from apps.users.forms import LoginTraditionalForm, UserCreateForm
from django.contrib.auth import login, authenticate


FORMS = [
            ("0", CreateComplaintStepOneForm),
            ("1", CreateComplaintStepTwoForm),
        ]

class CreateComplaintStepOneWizard(SessionWizardView):
    TEMPLATES = {
                    "0": "complaint/create_complaint_step_one.html",
                    "1": "complaint/create_complaint_step_two.html",
                }

    def get_context_data(self, form, **kwargs):
        context = super(CreateComplaintStepOneWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == '0':
            try:
                del self.request.session['form_data']
            except KeyError:
                pass
            try:
                del self.request.session['image_tmp']
            except KeyError:
                pass
        elif self.steps.current == '1':
            aux = self.get_cleaned_data_for_step("0")['company']
            context.update({'company': aux, })
        return context

    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        # Salvamos los forms y guardamos en una session
        form_data = [form.cleaned_data for form in form_list]
        #print form_data
        try:
            form_data[0]["category"] = form_data[0]["category"].id
        except AttributeError:
            form_data[0]["category"] = None

        try:
            form_data[0]["subcategory"] = form_data[0]["subcategory"].id
        except AttributeError:
            form_data[0]["subcategory"] = None

        self.request.session['form_data'] = form_data
        return redirect(reverse("complaint:create_complaint_last_step"))

class IndexView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/single_page.html')

# class PostView(View):
#     def get(self, request,  *args, **kwargs):
#         form = CreateComplaintStepOneForm()
#         return render(request, 'complaint/post_page.html', {'form':form})

#     def post(self, request, *args, **kwargs):
#         form = CreateComplaintStepOneForm(request.POST, request.FILES)

#         if form.is_valid():
#             #form.save()
#             return render(request, 'complaint/post_page.html', {'form': form})
#         else:
#             return render(request, 'complaint/post_page.html', {'form': form})

# class StepOneView(View):
#     def get(self, request,  *args, **kwargs):
#         return render(request, 'complaint/step_one.html')

class CreateComplaintLastStepView(View):

    def get(self, request,  *args, **kwargs):
        if request.session.get("form_data", None):
            ##
            # Publicar como aninimo o como usuario
            ##
            if request.session.get("invited", None) or request.user.is_authenticated():
                i=0
                form_list = self.request.session['form_data']
                for form in form_list:
                    
                    #Procesamos los 2 formularios
                    if i==0:
                        #Get category
                        try:
                            form["category"] = Category.objects.get(id=form["category"])
                        except Category.DoesNotExist:
                            form["category"] = None

                        #Get subcategory si no None
                        try:
                            form["subcategory"] = SubCategory.objects.get(id=form["subcategory"])
                        except SubCategory.DoesNotExist:
                            form["subcategory"] = None

                        #Get company si no la crea
                        try:
                            if form["company_val"]:
                                company = Company.objects.get(id=form["company_val"])
                            else:
                                company = Company.objects.get(name__icontains=form["company"])
                        except Company.DoesNotExist:
                            company = Company(name=form["company"], category=form["category"], subcategory=form["subcategory"])
                            company.save()

                        # Get de la ip del usuario
                        ip = request.META.get('REMOTE_ADDR')

                        complaint = Complaint(title=form["title"],
                                                description=form["description"],
                                                company=company,
                                                category=form["category"],
                                                subcategory=form["subcategory"],
                                                ipv4=ip,
                                                )
                        ##
                        # Publicar como usuario si esta conectado
                        ##
                        if request.user.is_authenticated():
                           complaint.user = request.user

                        #Guardamos la instancia
                        complaint.save()
                    elif i==1:
                        complaint_contact = ComplaintContact(complaint=complaint,
                                                                complete_name=form["complete_name"],
                                                                email=form["email"],
                                                                cellphone=form["cellphone"],)
                        complaint_location = ComplaintLocation(complaint=complaint,
                                                                place=form["place"],
                                                                product_or_service=form["product_or_service"],
                                                                other_solution=form["other_solution"],)
                        complaint_request = ComplaintRequest(complaint=complaint, actions_radio=form["actions_radio"],)

                        # Guardamos la instancia
                        complaint_contact.save()
                        complaint_location.save()
                        complaint_request.save()

                        if request.session.get("image_tmp", None) and request.session.get("image_tmp", None)!=[]:
                            for x in request.session['image_tmp']:
                                #Get ItemFiles si no None
                                try:
                                    item_object = ItemFiles.objects.get(id=x['id'])
                                except ItemFiles.DoesNotExist:
                                    item_object = None

                                if item_object:
                                    item_object.complaint=complaint
                                    item_object.save()

                    i=i+1
                
                #Al terminar ir a la url
                return redirect("/done/")
            else:
                login_error = None
                login_form = LoginTraditionalForm()
                register_form = UserCreateForm()
                return render(request, 'complaint/create_complaint_last_step.html',{
                    "company": self.request.session['form_data'][0]["company"],
                    'login_form':login_form,
                    'register_form':register_form, 'login_error':login_error,
                    })
        else:
            #Error 404
            return redirect("/")

    def post(self, request,  *args, **kwargs):
        login_error = None
        login_form = LoginTraditionalForm()
        register_form = UserCreateForm()

        if 'invited' in request.POST["form"]:
            self.request.session['invited'] = True
            return redirect(reverse("complaint:create_complaint_last_step"))
        elif 'register' in request.POST["form"]:
            register_form = UserCreateForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                user = authenticate(username=request.POST['username'],
                    password=request.POST['password1'])
                login(request, user)
                return redirect(reverse("complaint:create_complaint_last_step"))
        elif 'login' in request.POST["form"]:
            login_form = LoginTraditionalForm(request.POST)
            if login_form.is_valid():
                user = authenticate(username=request.POST['username'],
                    password=request.POST['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(reverse("complaint:create_complaint_last_step"))
                    else:
                        login_error = "* El usuario se encuentra inactivo"
                else:
                    login_error = "* El usuario o contraseña son incorrectos"
        return render(request, 'complaint/create_complaint_last_step.html', {'login_form':login_form,
            'register_form':register_form, 'login_error':login_error,})

class CategoryView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/category.html')

class ProfileView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'complaint/profile.html')

##
# View Asincronas
##
class MultiUploadAjax(View):
    def post(self, request,  *args, **kwargs):
        if request.is_ajax():
            form = AjaxUploadForm(request.POST, request.FILES)
            if form.is_valid():
                item = form.save()
                if request.FILES.get('image', None):
                    data = {'id':item.id, 'image':item.image.url, }
                else:
                    data = {'id':item.id, 'image':None}

                data_temp = []
                try:
                    data_temp = self.request.session['image_tmp']
                    data_temp.append(data)
                except:
                   data_temp.append(data)
                self.request.session['image_tmp'] = data_temp
            else:
                data = { 'status':'200', }

            mimetype = 'application/json'
            data_json = json.dumps(data)
            return HttpResponse(data_json, mimetype) 
        else:
            # render() a form with data (No AJAX)
            # redirect to results ok, or similar may go here 
            pass

class AjaxCompany(View):
    def get(self, request,  *args, **kwargs):
        if request.is_ajax():
            q = request.GET.get('term', '')
            companys = Company.objects.filter(name__icontains=q).order_by('name')[:6]
            results = []
            for company in companys:
                company_json = {}
                company_json['id'] = company.id
                company_json['label'] = company.name
                company_json['value'] = company.name
                if company.image:
                    company_json['image'] = company.image.url
                else:
                    company_json['image'] = "https://cdn2.iconfinder.com/data/icons/metro-uinvert-dock/128/Default.png"
                results.append(company_json)
            data = json.dumps(results)
        else:
            data = 'fail'

        mimetype = 'application/json'
        return HttpResponse(data, mimetype)        

class AjaxLoadCategoryFromAutocompleteCompany(View):
    def get(self, request,  *args, **kwargs):
        if request.is_ajax():
            q = request.GET.get('term', '')
            company = Company.objects.get(id=q)
            company_json = {}
            company_json['id'] = company.id
            company_json['category'] = company.category_id
            company_json['subcategory'] = company.subcategory_id
            data = json.dumps(company_json)
        else:
            data = 'fail'

        mimetype = 'application/json'
        return HttpResponse(data, mimetype)

class AjaxLoadSubCategory(View):
    def get(self, request,  *args, **kwargs):
        if request.is_ajax():
            q = request.GET.get('term', '')
            subcategorys = SubCategory.objects.filter(category=q)
            results = []
            for subcategory in subcategorys:
                subcategory_json = {}
                subcategory_json['id'] = subcategory.id
                subcategory_json['name'] = subcategory.name
                results.append(subcategory_json)
            data = json.dumps(results)
        else:
            data = 'fail'

        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
