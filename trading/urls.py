from django.urls import path
from django.contrib.auth import views as auth_views

from trading import views

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='home'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='company'),
    path('set/<int:pk>', views.set_session_company, name='set_company'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='trading/login.html'), name='login'),
]
