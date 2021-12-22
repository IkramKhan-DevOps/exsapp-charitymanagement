from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

app_name = "admins"
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('projecttype/', ProjectTypeListView.as_view(), name='projecttype-list'),
    path('projecttype/add/', ProjectTypeCreateView.as_view(), name='projecttype-create'),
    path('projecttype/<int:pk>/change/', ProjectTypeUpdateView.as_view(), name='projecttype-update'),
    path('projecttype/<int:pk>/delete/', ProjectTypeDeleteView.as_view(), name='projecttype-delete'),

    path('ngo/<int:pk>/change/', NGOUpdateView.as_view(), name='ngo-update'),
]
