from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
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


""" GENERIC VIEWS CRUD > PROJECT """


class ProjectListView(ListView):
    queryset = Project.objects.all()


class ProjectCreateView(CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('admins:project-list')


class ProjectUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('admins:project-list')


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('admins:project-list')


""" GENERIC VIEWS CRUD > DONATION """


class DonationListView(ListView):
    queryset = Donation.objects.all()


class DonationUpdateView(UpdateView):
    model = Donation
    fields = '__all__'
    success_url = reverse_lazy('admins:donation-list')


class DonationDeleteView(DeleteView):
    model = Donation
    success_url = reverse_lazy('admins:donation-list')


""" VIEW > PAYMENTS """


class PaymentVerificationEasyPaisa(View):

    def get(self, request):
        return render(request=request, template_name="admins/easypaisa_payment_verification.html")

    def post(self, request):

        transaction_id = request.POST['transaction_id']
        transaction = Donation.objects.filter(transaction_id=transaction_id)

        # IF TRANSACTION ID EXISTS OR NOT
        if transaction:
            transaction = transaction[0]

            # IF PROJECT CLOSED
            if not transaction.project.is_completed:

                # IF TRANSACTION ALREADY EXISTS
                if not transaction.is_completed:

                    # SAVE DONOR
                    transaction.user.donations_total += 1
                    transaction.user.donations_amount += transaction.amount
                    if Donation.objects.filter(user=transaction.user, project=transaction.project):
                        transaction.user.donations_projects += 1
                    transaction.user.save()

                    # SAVE PROJECT
                    transaction.project.donation_amount += transaction.amount
                    transaction.project.save()

                    # SAVE DONATION
                    transaction.is_completed = True
                    transaction.save()

                    messages.success(
                        request, f"Donation {transaction.pk} amount {transaction.amount} paid by "
                                 f"{transaction.user} verified successfully.")
                else:
                    messages.error(request, "This transaction is  already verified.")

            else:
                messages.error(request, "This project has been closed by administration.")
        else:
            messages.error(request, "No transaction record available with requested ID.")

        return render(request=request, template_name="admins/easypaisa_payment_verification.html")
