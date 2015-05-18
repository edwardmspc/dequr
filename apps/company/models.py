from django.db import models
from apps.category.models import Category, SubCategory


class Company(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True)
    name = models.CharField(max_length=140, unique=True)
    image = models.ImageField(upload_to="company_logos", blank=True)
    email = models.EmailField(max_length=140, blank=True)
    is_approved = models.BooleanField(default=False, blank=True)
    phone = models.CharField(max_length=140, blank=True)
    web_url = models.CharField(max_length=140, blank=True)
    facebook = models.CharField(max_length=140, blank=True)
    twitter = models.CharField(max_length=140, blank=True)

    def __unicode__(self):
        return self.name


class SubCompany(models.Model):
    company = models.ForeignKey(Company, null=True, blank=True)
    name = models.CharField(max_length=140)

    def __unicode__(self):
        return self.name
