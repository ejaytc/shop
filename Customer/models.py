from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def customer_number_unique():
    customer_query = Customer.objects.all()
    if customer_query:
        invoice_count = max([int(i.customer_number[-5:]) if i else 0
                            for i in customer_query])
        invoice_count += 1
    else:
        invoice_count = 0
    return f"INVOICE{str(invoice_count).zfill(5)}"


class Customer(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _("Active")
        TERMINATED = 'TERMINATED', _("Terminated")

    customer_number = models.CharField(max_length=200,
                                       default=customer_number_unique)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    brand = models.ForeignKey('Brand.Brand',
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    is_terminated = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='customer_added_by_user')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   blank=True,
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   related_name="customer_created_by_user")
    status = models.CharField(max_length=10,
                              choices=Status.choices,
                              default=Status.ACTIVE)

    def __str__(self) -> str:
        return "{}{}{}{}".format(self.first_name,
                                 ' ' if self.first_name else '',
                                 self.last_name,
                                 ' : ' + self.status)

    def save(self, *args, **kwargs):
        print(self.status)
        if self.status == 'ACTIVE':
            self.is_active = True
            self.is_terminated = False
        elif self.status != 'ACTIVE':
            self.is_terminated = True
            self.is_active = False
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        db_table = "Customer"
