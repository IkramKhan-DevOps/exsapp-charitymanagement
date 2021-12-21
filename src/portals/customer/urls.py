from django.urls import path
from django.views.generic import TemplateView

app_name = "customer-portal"
urlpatterns = [
    path('dashboard', TemplateView.as_view(template_name='customer/dashboard.html'), name='dashboard')
]
