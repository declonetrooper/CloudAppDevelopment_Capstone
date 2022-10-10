from django.contrib import admin
from .models import *

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2



# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['make', 'name', 'dealerid', 'types', 'year']
    list_filter = ['types', 'make', 'dealerid', 'year',]
    search_fields = ['make', 'name']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)