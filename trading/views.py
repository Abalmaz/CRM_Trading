from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView

from trading.models import Company


class CompanyListView(ListView):
    model = Company
    template_name = 'trading/company_list.html'
    context_object_name = 'companies'


class CompanyDetailView(DetailView):
    context_object_name = 'company'
    queryset = Company.objects.all()


def set_session_company(request, pk):
    request.session['company_id'] = pk
    return redirect('home')


