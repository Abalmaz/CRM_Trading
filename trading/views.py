from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from trading.mixins import GroupRequiredMixin
from trading.models import Company


class CompanyListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Company
    template_name = 'trading/company_list.html'
    context_object_name = 'companies'

    def get_queryset(self):
        return Company.objects.filter(employees=self.request.user)


class CompanyDetailView(DetailView):
    context_object_name = 'company'
    queryset = Company.objects.all()


class CompanyUpdateView(GroupRequiredMixin, UpdateView):
    group_required = ['superadmin', 'admin', 'manager']
    model = Company
    fields = ['name', ]


def set_session_company(request, pk):
    request.session['company_id'] = pk
    return redirect('home')
