# Generated by Django 4.0.2 on 2022-03-01 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_invoice_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='state',
        ),
    ]