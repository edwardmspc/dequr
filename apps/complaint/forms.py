# -*- coding: utf-8 -*-
from django import forms
from .models import Complaint


class CreateComplaintStepTwoForm(forms.Form):

    # Contacto
    complete_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(max_length=140, required=False)
    cellphone = forms.CharField(max_length=140, required=False)
    
    # Localizacion
    place = forms.CharField(max_length=140, required=False)
    product_or_service = forms.CharField(max_length=140, required=False)
    other_solution = forms.CharField(max_length=140, required=False)

    CHOICES = [
                (0, 'Que me proponga una solucion'),
                (1, 'La devolucion de mi Dinero'),
                (2, 'Que entregue mi producto'),
                (3, 'Otra solucion'),
            ]

    actions_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False)

class CreateComplaintStepOneForm(forms.ModelForm):
    company = forms.CharField(max_length=140, )
    company_val = forms.CharField(max_length=140, widget=forms.HiddenInput(), required=False)
    terms = forms.BooleanField(required=False)

    class Meta:
        model = Complaint
        fields = "__all__"
        exclude = ['date_create', 'company', 'ipv4']

    def clean_terms(self):
        if not self.cleaned_data["terms"]:
            raise forms.ValidationError(
                "Para publicar debe aceptar nuestros terminos del servicio."
            )        
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("El Correo electrónico ya se encuentra registrado")
        return self.cleaned_data['email']

    # def __init__(self, *args, **kwargs):
    #     super(ComplaintPOSTForm, self).__init__(*args, **kwargs)
    #     if self.errors:
    #         for f_name in self.fields:
    #             if f_name in self.errors:
    #                 classes = self.fields[f_name].widget.attrs.get('class', '')
    #                 classes += ' has-error'
    #                 self.fields[f_name].widget.attrs['class'] = classes