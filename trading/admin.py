from django.contrib import admin
from .models import Country, Product, Building, Company, Shop, EmployeeCompany,\
                    Role


class EmployeeCompanyInline(admin.TabularInline):
    model = EmployeeCompany
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = (EmployeeCompanyInline,)


admin.site.register(Country)
admin.site.register(Product)
admin.site.register(Building)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Shop)
admin.site.register(Role)
