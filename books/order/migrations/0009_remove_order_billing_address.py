# Generated by Django 4.0.2 on 2022-03-01 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_billing_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
    ]
