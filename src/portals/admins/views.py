from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView,
    TemplateView)

from src.accounts.models import User
from .models import (
    Donation, Project, ProjectType, Ngo
)


""" GENERIC VIEWS CUSTOM > DASHBOARD AND NGO """


class DashboardView(TemplateView):
    template_name = 'admins/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['total'] = User.objects.all().count()
        context['admins'] = User.objects.filter(is_superuser=True).count()
        context['staff'] = User.objects.filter(is_staff=True).count()
        context['customers'] = User.objects.filter(is_customer=True, is_active=True).count()
        context['in_active'] = User.objects.filter(is_active=False).count()
        return context


class NGOUpdateView(UpdateView):
    model = Ngo
    fields = '__all__'

    def get_object(self, queryset=None):
        return Ngo.objects.first() if Ngo.objects.all() else Ngo.objects.create()


""" GENERIC VIEWS CRUD > PROJECT TYPE """


class ProjectTypeListView(ListView):
    queryset = ProjectType.objects.all()


class ProjectTypeCreateView(CreateView):
    model = ProjectType
    fields = '__all__'
    success_url = reverse_lazy('admins:projecttype-list')


class ProjectTypeUpdateView(UpdateView):
    model = ProjectType
    fields = '__all__'
    success_url = reverse_lazy('admins:projecttype-list')


class ProjectTypeDeleteView(DeleteView):
    model = ProjectType
    success_url = reverse_lazy('admins:projecttype-list')
