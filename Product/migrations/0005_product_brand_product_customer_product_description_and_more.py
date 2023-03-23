# Generated by Django 4.1.7 on 2023-03-23 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0002_alter_brand_table'),
        ('Customer', '0006_alter_customer_date_updated'),
        ('Product', '0004_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Brand.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Customer.customer'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_terminated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='next_billing_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='previous_billing_date',
            field=models.DateField(auto_now=True),
        ),
    ]