# Generated by Django 4.0 on 2022-04-08 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_rename_num_pax_bookingrequest_number_of_pax'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingrequest',
            old_name='event_title',
            new_name='activity',
        ),
    ]
