from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

from trading.mixins import GroupRequiredMixin
from trading.models import Company


@login_required(login_url='login')
def home(request):
    return render(request=request, template_name='trading/home.html')


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
