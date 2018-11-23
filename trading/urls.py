from django.urls import path

from trading import views

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='home'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='company'),
    path('set/<int:pk>', views.set_session_company, name='set_company'),
]
