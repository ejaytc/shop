# Generated by Django 4.1.7 on 2023-03-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
