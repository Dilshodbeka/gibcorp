# Generated by Django 5.0.2 on 2024-02-28 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_rename_shipping_adress_order_shipping_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shipping_address',
            new_name='shippingAddress',
        ),
    ]
