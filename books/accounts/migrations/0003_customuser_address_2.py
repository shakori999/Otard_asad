# Generated by Django 4.0.2 on 2022-03-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_address_customuser_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address_2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]