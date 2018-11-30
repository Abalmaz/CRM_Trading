from django.contrib.auth.models import Group, AbstractUser
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class User(AbstractUser):
    def get_current_role(self, company):
        return self.company.filter(company=company).first().role

    def get_current_groups(self, company):
        user_group = []
        for group in self.get_current_role(company).groups.values_list(
                'name', flat=True):
            user_group.append(group)
        return user_group

    def get_current_permissions(self, company):
        user_perm = []
        for group in self.get_current_role(company).groups.all():
            for perm in group.permissions.all():
                user_perm.append(perm.codename)
        return user_perm


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


class Role(models.Model):
    SUPERADMIN = 1
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
    id = models.PositiveSmallIntegerField(choices=ROLES, primary_key=True)
    groups = models.ManyToManyField(Group, related_name='roles')

    def __str__(self):
        return self.get_id_display()


class EmployeeCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='employee')
    employee = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='company')
    is_default = models.BooleanField(default=False)
    role = models.ForeignKey(Role,
                             related_name='user_role_company',
                             on_delete=models.CASCADE)

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
