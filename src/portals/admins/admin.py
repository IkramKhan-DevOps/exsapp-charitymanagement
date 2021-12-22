from django.contrib import admin
from .models import (
    ProjectType, Donation, Ngo, Project
)


class NgoAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'contact_no', 'contact_email', 'is_active', 'created_on', 'updated_on'
    ]


class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'is_active'
    ]


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'project_type', 'required_amount', 'donation_amount', 'is_completed',
        'is_active', 'created_on'
    ]


class DonationAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'project', 'payment_method', 'transaction_id', 'amount', 'is_completed',
        'is_active', 'created_on'
    ]


admin.site.register(Ngo, NgoAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Donation, DonationAdmin)
