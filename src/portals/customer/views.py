from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from src.portals.admins.models import Donation, Project


class DonationListView(ListView):
    queryset = Donation.objects.all()
    template_name = 'customer/donation_list.html'

    def get_queryset(self):
        return Donation.objects.filter(user=self.request.user)


class DonationCreateView(CreateView):
    model = Donation
    template_name = 'customer/donation_form.html'
    fields = ['project', 'payment_method', 'transaction_id', 'is_active']
    success_url = reverse_lazy("customer-portal:donation-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
