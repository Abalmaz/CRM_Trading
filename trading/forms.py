from django import forms

from trading.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'country', 'founded_date',
                  'products', 'buildings')
