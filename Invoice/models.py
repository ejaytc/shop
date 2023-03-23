from django.db import models


def invoice_number_unique():
    invoice_query = Invoice.objects.all()
    if invoice_query:
        invoice_count = max([int(i.invoice_number[-5:]) if i else 0
                            for i in invoice_query])
        invoice_count += 1
    else:
        invoice_count = 0
    return f"INVOICE{str(invoice_count).zfill(5)}"


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
