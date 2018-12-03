from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView

from trading.forms import CompanyForm, ShopForm
from trading.mixins import GroupRequiredMixin
from trading.models import Company, Shop


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'trading/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx['current_role'] = self.request.user.get_current_role(
            self.request.company)
        print(ctx['current_role'])
        return ctx


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
    form_class = ShopForm
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
