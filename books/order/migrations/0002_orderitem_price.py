# Generated by Django 4.0.3 on 2022-04-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=113.0, error_messages={'name': {'max_length': 'the price must be between 0 and 999.99.'}}, help_text='format: maximum price 999.99', max_digits=6, verbose_name='regular store price'),
            preserve_default=False,
        ),
    ]