from django.urls import path

from trading import views

urlpatterns = [
    path('', views.CompanyListView.as_view()),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='company'),
]
