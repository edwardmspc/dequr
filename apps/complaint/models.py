# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
from apps.company.models import Category, Company, SubCategory
from apps.users.models import User


class Complaint(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True)
    category = models.ForeignKey(Category, null=True)
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True)
    
    #image = models.ImageField(upload_to="complaint_documents", null=True, blank=True)
    #video = models.URLField(blank=True, null=True)

    slug = models.SlugField(editable=False, blank=True, null=True)
    ipv4 = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True, default=None)
    date_create = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = '%s' % (slugify(self.title))
        super(Complaint, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class ItemFiles(models.Model):
    complaint = models.ForeignKey(Complaint, null=True, blank=True)
    image = models.ImageField(upload_to="complaint_documents", null=True, blank=True)
    audio = models.FileField(upload_to="complaint_documents", null=True, blank=True)

class ComplaintContact(models.Model):
    # Relacion
    complaint = models.ForeignKey(Complaint)

    # Contacto
    complete_name = models.CharField(max_length=140, null=True, blank=True)
    email = models.EmailField(max_length=140, null=True, blank=True)
    cellphone = models.CharField(max_length=140, null=True, blank=True)

class ComplaintLocation(models.Model):
    # Relacion
    complaint = models.ForeignKey(Complaint)

    # Localizacion
    place = models.CharField(max_length=140, null=True, blank=True)
    product_or_service = models.CharField(max_length=140, null=True, blank=True)
    other_solution = models.CharField(max_length=140, null=True, blank=True)

class ComplaintRequest(models.Model):
    # Relacion
    complaint = models.ForeignKey(Complaint)
    
    CHOICES = [
                (0, 'Que me proponga una solucion'),
                (1, 'La devolucion de mi Dinero'),
                (2, 'Que entregue mi producto'),
                (3, 'Otra solucion'),
            ]

    actions_radio = models.CharField(choices=CHOICES, max_length=140, null=True, blank=True)