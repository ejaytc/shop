from django.db import models


def invoice_number_unique():
    rec = Invoice.objects.all().count()
    return f"INVOICE{str(rec).zfill(5-len(str(rec)))}"


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=200,
                                      default=invoice_number_unique)
    customer = models.ForeignKey("Customer.Customer",
                                 blank=True,
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    product = models.ForeignKey("Product.Product",
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)
    total_price = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.invoice_number}"

    class Meta:
        db_table = "Invoice"
