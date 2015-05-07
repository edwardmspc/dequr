from django.contrib import admin
from .models import Complaint, ComplaintContact, ComplaintLocation, ComplaintRequest, ItemFiles


admin.site.register(Complaint)
admin.site.register(ComplaintContact)
admin.site.register(ComplaintLocation)
admin.site.register(ComplaintRequest)
admin.site.register(ItemFiles)
