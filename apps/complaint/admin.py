from django.contrib import admin
from .models import Complaint, ComplaintContact, ComplaintLocation, ComplaintRequest


admin.site.register(Complaint)
admin.site.register(ComplaintContact)
admin.site.register(ComplaintLocation)
admin.site.register(ComplaintRequest)
