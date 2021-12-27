from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

from src.portals.admins.models import Donation, Project


class NewsFeedView(TemplateView):
    template_name = 'customer/news-feed.html'

    def get_context_data(self, **kwargs):
        context = super(NewsFeedView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(is_completed=False)
        return context


class DonationListView(ListView):
    queryset = Donation.objects.all()
    template_name = 'customer/donation_list.html'

    def get_queryset(self):
        return Donation.objects.filter(user=self.request.user)


class DonationCreateView(CreateView):
    model = Donation
    template_name = 'customer/donation_form.html'
    fields = ['payment_method', 'transaction_id', 'is_active']
    success_url = reverse_lazy("customer-portal:donation-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = get_object_or_404(Project.objects.all(), pk=self.kwargs['pk'])
        return super().form_valid(form)
