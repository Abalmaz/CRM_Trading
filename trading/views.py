from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView

from trading.forms import CompanyForm, ShopForm
from trading.mixins import GroupRequiredMixin
from trading.models import Company, Shop


@login_required(login_url='login')
def home(request):
    return render(request=request, template_name='trading/home.html')


class CompanyUpdateView(GroupRequiredMixin, UpdateView):

    group_required = ['superadmin', 'admin', 'manager']

    model = Company
    fields = ['name', 'country', 'founded_date', 'products', 'buildings']
    success_url = reverse_lazy('home')


class CompanyCreateView(GroupRequiredMixin, CreateView):

    group_required = ['superadmin', 'admin']

    success_url = reverse_lazy('home')
    model = Company
    form_class = CompanyForm
    template_name = 'trading/new_company.html'


class ShopUpdateView(GroupRequiredMixin, UpdateView):

    group_required = ['superadmin', 'admin', 'manager', 'financier']

    model = Shop
    fields = ['name', 'building', 'product']
    success_url = reverse_lazy('home')


class ShopCreateView(GroupRequiredMixin, CreateView):

    group_required = ['superadmin', 'admin', 'manager', 'financier']

    success_url = reverse_lazy('home')
    model = Shop
    form_class = ShopForm
    template_name = 'trading/new_shop.html'


def set_session_company(request, pk):
    request.session['company_id'] = pk
    return redirect('home')
