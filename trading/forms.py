from django import forms

from trading.models import Company, Shop, Product, Building


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'country', 'founded_date',
                  'products', 'buildings')


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'products', 'building')

    def __init__(self, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['products'].queryset = Product.objects.filter(
            companies=company)
        self.fields['building'].queryset = Building.objects.filter(
            companies=company
        )
