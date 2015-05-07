# -*- coding: utf-8 -*-
from django import forms
from .models import Complaint, ItemFiles


class CreateComplaintStepTwoForm(forms.Form):

    # Contacto
    complete_name = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={"placeholder": "Nombre completo"}))
    email = forms.EmailField(max_length=140, required=False, widget=forms.TextInput(attrs={"placeholder": "Correo electrónico"}))
    cellphone = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={"placeholder": "Telefono"}))
    
    # Localizacion
    place = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={"placeholder": "Lugar"}))
    product_or_service = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={"placeholder": "Producto o servicio"}))
    other_solution = forms.CharField(max_length=140, required=False)

    CHOICES = [
                (0, 'Que me proponga una solucion'),
                (1, 'La devolucion de mi Dinero'),
                (2, 'Que entregue mi producto'),
                (3, 'Otra solucion'),
            ]

    actions_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False)

class CreateComplaintStepOneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateComplaintStepOneForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Título de tu queja"
        self.fields['description'].widget.attrs['placeholder'] = "Descripcion de tu queja"
        self.fields['company'].widget.attrs['placeholder'] = "Nombre de la empresa"

    company = forms.CharField(max_length=140, )
    company_val = forms.CharField(max_length=140, widget=forms.HiddenInput(), required=False)
    terms = forms.BooleanField(required=False)

    class Meta:
        model = Complaint
        fields = "__all__"
        exclude = ['date_create', 'company', 'ipv4', 'audio', 'video']

    def clean_terms(self):
        if not self.cleaned_data["terms"]:
            raise forms.ValidationError(
                "Para publicar debe aceptar nuestros terminos del servicio."
            )        
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("El Correo electrónico ya se encuentra registrado")
        return self.cleaned_data['email']

class AjaxUploadForm(forms.ModelForm):
    class Meta:
        model = ItemFiles
        fields = "__all__"