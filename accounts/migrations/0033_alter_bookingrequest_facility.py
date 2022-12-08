# Generated by Django 4.0 on 2022-05-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_alter_bookingrequest_facility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='facility',
            field=models.CharField(choices=[('Conference Room', 'Conference Room'), ('Futsal Court 1', 'Futsal Court 1 (closer to BDE)'), ('Futsal Court 2', 'Futsal Court 2 (closer to 2SIR)'), ('Gym', 'Gym'), ('IPPT Running Route', 'IPPT Running Route'), ('Lecture Theatre', 'Lecture Theatre/Auditorium'), ('Mess', 'Mess'), ('Multi Purpose Hall', 'Multi Purpose Hall'), ('Parade Square (2SIR) Left', 'Parade Square (2SIR) Left'), ('Parade Square (5SIR) Right', 'Parade Square (5SIR) Right'), ('Full Parade Square', 'Full Parade Square'), ('Planning Room (505)', 'Planning Room (505)'), ('Training Shed 603A', 'Training Shed 603A'), ('Training Shed 603B', 'Training Shed 603B'), ('VIP Lounge', 'VIP Lounge'), ('Ballinger Running Route', 'Ballinger Running Route'), ('Ballinger Motorised Circuit', 'Ballinger Motorised Circuit')], max_length=100),
        ),
    ]
