# Generated by Django 4.1.7 on 2023-03-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0005_alter_customer_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
