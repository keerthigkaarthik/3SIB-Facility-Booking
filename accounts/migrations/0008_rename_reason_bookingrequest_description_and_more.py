# Generated by Django 4.0 on 2022-04-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_bookingrequest_event_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingrequest',
            old_name='reason',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='bookingrequest',
            name='time_needed',
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='bookingrequest',
            name='updated_by_admin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bookingrequest',
            name='date_needed',
            field=models.DateField(null=True),
        ),
    ]
