from django.contrib import admin
from .models import Company, SubCompany


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'email', 'phone',
                    'twitter', 'facebook', 'web_url', 'is_approved',)
    list_filter = ('category', 'subcategory',)
admin.site.register(Company, CompanyAdmin)


class SubCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company',)
    list_filter = ('company',)

admin.site.register(SubCompany, SubCompanyAdmin)
