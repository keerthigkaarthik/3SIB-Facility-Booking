# Generated by Django 4.0 on 2022-04-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_bookingrequest_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingrequest',
            name='priority_lvl',
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='priority_level',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1),
            preserve_default=False,
        ),
    ]
