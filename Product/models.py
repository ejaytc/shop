from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


def product_number_unique():
    product_query = Product.objects.all()
    if product_query:
        invoice_count = max([int(i.product_number[-5:]) if i else 0
                            for i in product_query])
        invoice_count += 1
    else:
        invoice_count = 0
    return f"INVOICE{str(invoice_count).zfill(5)}"


class Product(models.Model):
    class Currency(models.TextChoices):
        USDOLLAR = 'USD', _('US Dollar')
        PhILPESO = 'PHP', _('Philipine Peso')

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _("Active")
        TERMINATED = 'TERMINATED', _("Terminated")

    product_number = models.CharField(max_length=50,
                                      default=product_number_unique)
    currency = models.CharField(max_length=3,
                                choices=Currency.choices,
                                default=Currency.PhILPESO)
    price = models.FloatField(default=0.0)
    customer = models.ForeignKey('Customer.Customer',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    brand = models.ForeignKey('Brand.Brand',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL)
    next_billing_date = models.DateField(blank=True)
    previous_billing_date = models.DateField(blank=True)
    is_active = models.BooleanField(default=True)
    is_terminated = models.BooleanField(default=False)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='added_by_user')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="created_by_user")
    status = models.CharField(max_length=10,
                              choices=Status.choices,
                              default=Status.ACTIVE)

    def __str__(self) -> str:
        return "{}{}".format(str(self.brand) + ' : ' 
                             if self.brand else '',
                             self.product_number)

    class Meta:
        db_table = "Product"
