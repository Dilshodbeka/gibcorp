# Generated by Django 5.0.2 on 2024-02-28 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_rename_shipping_address_order_shippingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shippingAddress',
            new_name='shipping_address',
        ),
    ]
