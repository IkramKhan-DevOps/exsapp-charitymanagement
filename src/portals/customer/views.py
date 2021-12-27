from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView

from src.accounts.decorators import customer_required
from src.portals.admins.models import Donation, Project


@method_decorator(customer_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


@method_decorator(customer_required, name='dispatch')
class NewsFeedView(TemplateView):
    template_name = 'customer/news-feed.html'

    def get_context_data(self, **kwargs):
        context = super(NewsFeedView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(is_completed=False)
        return context


@method_decorator(customer_required, name='dispatch')
class DonationListView(ListView):
    queryset = Donation.objects.all()
    template_name = 'customer/donation_list.html'

    def get_queryset(self):
        return Donation.objects.filter(user=self.request.user)


class DonateForm(ModelForm):
    class Meta:
        model = Donation
        fields = ['payment_method', 'transaction_id']


@method_decorator(login_required, name='dispatch')
class DonationCreateView(View):

    def get(self, request, pk):
        if request.user.is_superuser or request.user.is_staff:
            messages.warning(request, "Admins are not allowed to donate.")
            return redirect('admins:dashboard')

        project = get_object_or_404(Project.objects.all(), pk=self.kwargs['pk'])
        return render(request, 'customer/donation_form.html', context={'form': DonateForm()})

    def post(self, request, pk):
        form = DonateForm(request.POST)
        project = get_object_or_404(Project.objects.all(), pk=self.kwargs['pk'])

        if form.is_valid():
            form.instance.user = request.user
            form.instance.project = project
            form.save()
            messages.success(request, "Your transaction has been added, check your status after 24hrs")
        return render(request, 'customer/donation_form.html', context={'form': DonateForm()})
