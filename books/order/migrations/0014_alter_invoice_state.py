# Generated by Django 4.0.2 on 2022-03-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_invoice_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='state',
            field=models.CharField(blank=True, choices=[('B', 'Basra')], max_length=2, null=True),
        ),
    ]