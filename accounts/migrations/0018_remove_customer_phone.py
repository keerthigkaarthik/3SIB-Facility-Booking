# Generated by Django 4.0 on 2022-04-05 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_customer_user_alter_bookingrequest_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
