from django.urls import path
from django.views.generic import TemplateView
from .views import DonationCreateView, DonationListView, DashboardView

app_name = "customer-portal"
urlpatterns = [

    path(
        'dashboard', DashboardView.as_view(), name='dashboard'
    ),
    path('donation/', DonationListView.as_view(), name='donation-list'),
    path('project/<int:pk>/donate/', DonationCreateView.as_view(), name='donate'),

]
