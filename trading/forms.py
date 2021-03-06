from django import forms

from trading.models import Company, Shop


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'country', 'founded_date', 'buildings')


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'products', 'building')
