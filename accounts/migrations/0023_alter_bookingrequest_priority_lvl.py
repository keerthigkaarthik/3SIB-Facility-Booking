# Generated by Django 4.0 on 2022-04-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_bookingrequest_mod_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='priority_lvl',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100, null=True),
        ),
    ]
