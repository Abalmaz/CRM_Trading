from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=80)
    country = models.ForeignKey(Country,
                                on_delete=models.PROTECT,
                                related_name='buildings')
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=80)
    country = models.ForeignKey(Country,
                                on_delete=models.PROTECT,
                                related_name='companies')
    founded_date = models.DateField()
    products = models.ManyToManyField(Product, related_name='companies')
    buildings = models.ManyToManyField(Building, related_name='companies')
    employees = models.ManyToManyField(User,
                                       related_name='companies',
                                       through='EmployeeCompany')

    def __str__(self):
        return self.name


class EmployeeCompany(models.Model):
    SUPERADMIN=1
    ADMIN = 2
    MANAGER = 3
    SELLER = 4
    FINANCIER = 5
    ROLES = (
        (SUPERADMIN, 'superadmin'),
        (ADMIN, 'admin'),
        (MANAGER, 'manager'),
        (SELLER, 'seller'),
        (FINANCIER, 'financier'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.SmallIntegerField(choices=ROLES)
    is_default_company = models.BooleanField(default=False)

    class Meta:
        unique_together = (("company", "employee"),)


class Shop(models.Model):
    name = models.CharField(max_length=80)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='shops')
    products = models.ManyToManyField(Product, related_name='shops')
    building = models.ForeignKey(Building,
                                 on_delete=models.CASCADE,
                                 related_name='shops')

    def __str__(self):
        return self.name
