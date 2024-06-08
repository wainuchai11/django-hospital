from django.contrib import admin
from .models import Patient, Drug, Treatment

admin.site.register(Patient)
admin.site.register(Drug)
admin.site.register(Treatment)
