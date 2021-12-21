from django.urls import path, include
from django.views.generic import TemplateView

app_name = "admin-portal"
urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name='admins/dashboard.html'), name='dashboard')
]
