from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView

from trading.forms import CompanyForm
from trading.mixins import GroupRequiredMixin
from trading.models import Company


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


def set_session_company(request, pk):
    request.session['company_id'] = pk
    return redirect('home')
