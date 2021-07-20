from django.contrib import admin
from .models import Animal, Visit, Immunization, Photo

# Register your models here.
admin.site.register(Animal)
admin.site.register(Visit)
admin.site.register(Immunization)
admin.site.register(Photo)
