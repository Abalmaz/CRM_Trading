from django.contrib import admin
from .models import Country, Product, Building, Company, Shop

# Register your models here.
admin.site.register(Country)
admin.site.register(Product)
admin.site.register(Building)
admin.site.register(Company)
admin.site.register(Shop)
