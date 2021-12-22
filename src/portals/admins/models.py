from django.db import models


class Ngo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available for this ngo.")
    address = models.TextField(null=True, blank=True)
    contact_no = models.TextField(max_length=20)
    contact_email = models.TextField(max_length=255, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "NGO"

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available.")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Projects Types"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available.")
    project_type = models.ForeignKey('ProjectType', on_delete=models.SET_NULL, null=True, blank=False)
    required_amount = models.FloatField(default=1000)
    donation_amount = models.FloatField(default=0)
    is_completed = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class Donation(models.Model):
    PAYMENT_METHOD_CHOICE = (
        ('e', 'EasyPaisa'),
    )
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=False)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=False)
    payment_method = models.CharField(max_length=1, default='e', choices=PAYMENT_METHOD_CHOICE)
    amount = models.FloatField(default=0)
    transaction_id = models.CharField(
        max_length=1000, null=False, blank=False,
        help_text="Enter transaction id here, transaction id will be provided by your service provider "
                  "i.e EasyPaisa provide you through sms over a successful transaction"
    )
    is_completed = models.BooleanField(
        default=False, help_text="Make Sure you are careful about this check? If you check this it will mark this "
                                 "transaction as successful so if user has paid then you can check this."
    )

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return str(self.pk)
