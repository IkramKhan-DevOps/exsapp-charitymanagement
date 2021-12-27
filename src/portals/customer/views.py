from django.views.generic import ListView, UpdateView, CreateView

from src.portals.admins.models import Donation


class DonationListView(ListView):
    queryset = Donation.objects.all()
    template_name = 'customer/donation_list.html'

    def get_queryset(self):
        return Donation.objects.filter(user=self.request.user)


class DonationCreateView(CreateView):
    queryset = Donation.objects.all()
    template_name = 'customer/donation_form.html'
    fields = ['project', 'payment_method', 'transaction_id', 'is_active']
