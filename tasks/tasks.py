from Product.models import Product
from Invoice.models import Invoice
from Customer.models import Customer
from datetime import date, timedelta


def get_due_product():
    product_obj = Product.objects
    product_query = product_obj.filter(brand__brand_name__contains="CDO",
                                       next_billing_date__lte=date.today(),
                                       customer__is_active__exact=True)
    due_product = []
    invoice_query = Invoice.objects.all()
    if invoice_query:
        invoice_count = max([int(i.invoice_number[-5:]) if i else 0
                            for i in invoice_query])
    else:
        invoice_count = 0
    print("Query Set")
    for rec in product_query.values():
        print(f"{rec}\n")
        invoice_count += 1
        customer_obj = Customer.objects.get(id=rec.get('customer_id', False))
        product_rec = product_obj.get(id=rec.get('id', False))
        invoice_number = f"INVOICE{str(invoice_count).zfill(5)}"
        due_product.append(Invoice(invoice_number=invoice_number,
                                   customer=customer_obj,
                                   description=f"{rec.get('description', False)}",
                                   product=product_rec,
                                   total_price=rec.get('price', False)))
    print(f"Invoice Created: {create_invoice_for_product(due_product, product_query)}")


def create_invoice_for_product(due_product, product_query):
    new_record = Invoice.objects.bulk_create(due_product)

    for product in product_query:
        next_bill = product.next_billing_date + timedelta(days=30)
        product.next_billing_date = next_bill
        product.previous_billing_date = date.today()
        product.save()
    return new_record


def run():
    get_due_product()
