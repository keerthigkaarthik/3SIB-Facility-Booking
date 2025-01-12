from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    def NoOfPend(self):
        return len(self.bookingrequest_set.filter(status='Pending'))

    def NoOfAcc(self):
        return len(self.bookingrequest_set.filter(status='Approved'))

class BookingRequest(models.Model):
    STATUS = [
        ('Pending','Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]

    FACILITIES = [
        ('Conference Room', 'Conference Room'),
        ('Futsal Court 1', 'Futsal Court 1 (closer to BDE)'),
        ('Futsal Court 2', 'Futsal Court 2 (closer to 2SIR)'),
        ('Gym', 'Gym'),
        ('IPPT Running Route', 'IPPT Running Route'),
        ('Lecture Theatre', 'Lecture Theatre/Auditorium'),
        ('Mess', 'Mess'),
        ('Multi Purpose Hall', 'Multi Purpose Hall'),
        ('Parade Square (2SIR) Left', 'Parade Square (2SIR) Left'),
        ('Parade Square (5SIR) Right', 'Parade Square (5SIR) Right'),
        ('Full Parade Square', 'Full Parade Square'),
        ('Planning Room (505)', 'Planning Room (505)'),
        ('Training Shed 603A', 'Training Shed 603A'),
        ('Training Shed 603B', 'Training Shed 603B'),
        ('VIP Lounge', 'VIP Lounge'),
        ('Ballinger Running Route', 'Ballinger Running Route'),
        ('Ballinger Motorised Circuit', 'Ballinger Motorised Circuit')
    ]

    STARTING_TIME = [
        (730,'07:30 (Period 1)'),
        (820,'08:20 (Period 2)'),
        (930,'09:30 (Period 3)'),
        (1020,'10:20 (Period 4)'),
        (1130,'11:30 (Period 5A)'),
        (1330,'13:30 (Period 5B)'),
        (1430,'14:30 (Period 6)'),
        (1520,'15:20 (Period 7)'),
        (1630,'16:30 (Period 8)'),
        (1720,'17:20 (Period 9)'),
        (1930,'19:30 (Night)')
    ]

    ENDING_TIME = [
        (820,'08:20 (Period 1)'),
        (920,'09:20 (Period 2)'),
        (1020,'10:20 (Period 3)'),
        (1110,'11:10 (Period 4)'),
        (1220,'12:20 (Period 5A)'),
        (1420,'14:20 (Period 5B)'),
        (1520,'15:20 (Period 6)'),
        (1610,'16:10 (Period 7)'),
        (1720,'17:20 (Period 8)'),
        (1810,'18:10 (Period 9)'),
        (2100,'21:00 ')
    ]

    PRIORITY = [
        (1, '1 (Bilat/ROT/Test)'),
        (2, '2 (UTS Training Activities)'),
        (3, '3 (Admin/Cohesion Activities)')
    ]

    activity = models.CharField(max_length=100)
    facility = models.CharField(max_length=100, choices=FACILITIES)
    date_needed = models.DateField()
    priority_level = models.IntegerField(choices=PRIORITY)
    starting_time = models.IntegerField(choices=STARTING_TIME)
    ending_time = models.IntegerField(choices=ENDING_TIME)
    number_of_pax = models.IntegerField()
    POC = models.CharField(max_length=1000)

    remarks = models.CharField(max_length=10000, null=True)
    mod_comments = models.CharField(max_length=10000, null=True)
    status = models.CharField(max_length=100, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    unit = models.ForeignKey(customer, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.unit.name + " " + self.activity + ' ' + f"{self.date_needed}"
