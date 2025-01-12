# Generated by Django 4.0 on 2022-03-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=100, null=True)),
                ('date_needed', models.CharField(max_length=100, null=True)),
                ('time_needed', models.CharField(max_length=100, null=True)),
                ('reason', models.CharField(max_length=10000, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]