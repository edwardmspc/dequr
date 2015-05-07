from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=140)
    category = models.ForeignKey(Category, null=True, blank=True)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
        
class Company(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to="company_logos", blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True)

    def __unicode__(self):
        return self.name

class SubCompany(models.Model):
    name = models.CharField(max_length=140)
    company = models.ForeignKey(Company, null=True, blank=True)
    def __unicode__(self):
        return self.name