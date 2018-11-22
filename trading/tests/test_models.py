from django.test import TestCase

from trading.models import Product, Country, Building, Company, Shop


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='clothing')

    def test_product_name_max_length(self):
        max_length = self.product._meta.get_field('name').max_length
        self.assertEquals(max_length, 80)

    def test_object_name_is_product_name(self):
        expected_object_name = '{}'.format(self.product.name)
        self.assertEquals(expected_object_name, str(self.product))


class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name='Canada')

    def test_country_name_max_length(self):
        max_length = self.country._meta.get_field('name').max_length
        self.assertEquals(max_length, 80)

    def test_object_name_is_country_name(self):
        expected_object_name = '{}'.format(self.country.name)
        self.assertEquals(expected_object_name, str(self.country))


class BuildingModelTest(TestCase):
    def setUp(self):
        country = Country.objects.create(name='Canada')
        self.building = Building.objects.create(name='Khortica',
                                                country=country,
                                                address='Shevchenko Str, 1')

    def test_building_name_max_length(self):
        max_length = self.building._meta.get_field('name').max_length
        self.assertEquals(max_length, 80)

    def test_object_name_is_building_name(self):
        expected_object_name = '{}'.format(self.building.name)
        self.assertEquals(expected_object_name, str(self.building))


class CompanyModelTest(TestCase):
    def setUp(self):
        country = Country.objects.create(name='Canada')
        self.company = Company.objects.create(name='Inditex',
                                              country=country,
                                              founded_date='1985-06-12')

    def test_company_name_max_length(self):
        max_length = self.company._meta.get_field('name').max_length
        self.assertEquals(max_length, 80)

    def test_object_name_is_company_name(self):
        expected_object_name = '{}'.format(self.company.name)
        self.assertEquals(expected_object_name, str(self.company))


class ShopModelTest(TestCase):
    def setUp(self):
        country = Country.objects.create(name='Canada')
        building = Building.objects.create(name='Khortica', country=country)
        company = Company.objects.create(name='Inditex',
                                         country=country,
                                         founded_date='1985-06-12')
        self.shop = Shop.objects.create(name='Zara',
                                        company=company,
                                        building=building)

    def test_shop_name_max_length(self):
        max_length = self.shop._meta.get_field('name').max_length
        self.assertEquals(max_length, 80)

    def test_object_name_is_shop_name(self):
        expected_object_name = '{}'.format(self.shop.name)
        self.assertEquals(expected_object_name, str(self.shop))
