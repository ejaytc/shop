# Generated by Django 4.1.7 on 2023-03-23 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_product_status_alter_product_added_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_number',
            new_name='product_number',
        ),
    ]
