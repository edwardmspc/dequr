from django.contrib import admin
from .models import Category, SubCategory


class SubCategoryAdmin(admin.ModelAdmin):
    def show_category(self, obj):
        return ("%s" % (obj.category))
    show_category.short_description = 'Categoria padre'
    list_display = ('name', 'show_category',)
    list_filter = ('category',)

admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
