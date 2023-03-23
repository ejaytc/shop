# Generated by Django 4.1.7 on 2023-03-23 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_alter_product_is_active_and_more'),
        ('Invoice', '0002_remove_invoice_product_invoice_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='product',
        ),
        migrations.AddField(
            model_name='invoice',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.product'),
        ),
    ]