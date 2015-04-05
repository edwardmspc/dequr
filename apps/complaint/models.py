# -*- coding: utf-8 -*-
from datetime import datetime
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

class Complaint(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    category = models.ForeignKey(Category, blank=True)
    description = models.TextField()
    url = models.CharField(max_length=255, blank=True)
    date_create = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Complaint, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
    
