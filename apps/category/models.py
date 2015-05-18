from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=140, unique=True)
    image = models.ImageField(upload_to="category_logos", blank=True)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True)
    name = models.CharField(max_length=140, unique=True)
    image = models.ImageField(upload_to="subcategory_logos", blank=True)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
