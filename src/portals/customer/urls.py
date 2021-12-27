from django.urls import path
from django.views.generic import TemplateView
from .views import DonationCreateView, DonationListView

app_name = "customer-portal"
urlpatterns = [

    path(
        'dashboard',
        TemplateView.as_view(template_name='customer/dashboard.html'),
        name='dashboard'
    ),
    path('my/donation/', DonationListView.as_view(), name='donations-list'),
    path('my/donation/add/', DonationCreateView.as_view(), name='donation-create'),

]
