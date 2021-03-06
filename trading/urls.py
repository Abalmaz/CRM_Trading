from django.urls import path
from django.contrib.auth import views as auth_views

from trading import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('set/<int:pk>', views.set_session_company, name='set_company'),
    path('new_company/', views.CompanyCreateView.as_view(), name='new_company'),
    path('update/<int:pk>', views.CompanyUpdateView.as_view(), name='update'),
    path('new_shop/', views.ShopCreateView.as_view(), name='new_shop'),
    path('shop_update/<int:pk>', views.ShopUpdateView.as_view(),
         name='shop_update'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='trading/login.html'), name='login'),
]
