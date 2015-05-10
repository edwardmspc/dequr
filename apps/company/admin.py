from django.contrib import admin
from .models import Category, SubCategory, Company 

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Company)