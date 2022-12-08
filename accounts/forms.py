from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import BookingRequest
from django import forms


STATUS = [
    ('Pending','Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected')
]

FACILITIES = [
    ('Conference Room', 'Conference Room'),
    ('Futsal Court 1', 'Futsal Court 1'),
    ('Futsal Court 2', 'Futsal Court 2'),
    ('Gym', 'Gym'),
    ('IPPT Running Route', 'IPPT Running Route'),
    ('Lecture Theatre', 'Lecture Theatre'),
    ('Mess', 'Mess'),
    ('Multi Purpose Hall', 'Multi Purpose Hall'),
    ('Parade Square (2SIR) Left', 'Parade Square (2SIR) Left'),
    ('Parade Square (5SIR) Right', 'Parade Square (5SIR) Right'),
    ('Planning Room (505)', 'Planning Room (505)'),
    ('Training Shed 603A', 'Training Shed 603A'),
    ('Training Shed 603B', 'Training Shed 603B'),
    ('VIP Lounge', 'VIP Lounge'),
    ('Ballinger Running Route', 'Ballinger Running Route')
]

STARTING_TIME = [
    (730,'07:30'),
    (820,'08:20'),
    (930,'09:30'),
    (1020,'10:20'),
    (1130,'11:30'),
    (1330,'13:30'),
    (1430,'14:30'),
    (1520,'15:20'),
    (1630,'16:30'),
    (1720,'17:20'),
    (1930,'19:30')
]

ENDING_TIME = [
    (820,'08:20'),
    (920,'09:20'),
    (1020,'10:20'),
    (1110,'11:10'),
    (1220,'12:20'),
    (1420,'14:20'),
    (1520,'15:20'),
    (1610,'16:10'),
    (1720,'17:20'),
    (1810,'18:10'),
    (2100,'21:00')
]

PRIORITY = [
    (1, '1'),
    (2, '2'),
    (3, '3')
]


class UserSideBookingRequestForm(ModelForm):

    class Meta:
        model = BookingRequest
        fields = '__all__'
        exclude = ['status', 'unit', 'mod_comments']

        widgets = {
            'activity': forms.TextInput(attrs={"class": "form-control", "placeholder": "Event title"}),
            'facility': forms.Select(attrs={"class": "form-control"}),
            'date_needed': forms.DateInput(attrs={"class": "form-control", "placeholder": "YYYY-MM-DD", "id": "datepicker"}),
            'priority_level': forms.Select(attrs={"class": "form-control"}),
            'starting_time': forms.Select(attrs={"class": "form-control"}),
            'ending_time': forms.Select(attrs={"class": "form-control"}),
            'number_of_pax': forms.NumberInput(attrs={"class": "form-control"}),
            'POC': forms.TextInput(attrs={"class": "form-control", "placeholder": "Rank/Name/Appointment/Contact No."}),
            'remarks': forms.Textarea(attrs={"class": "form-control", "placeholder": "Please provide some compelling reasons if your timeslot is contested"}),
        }

class StaffSideBookingRequestForm(ModelForm):
    class Meta:
        model = BookingRequest
        fields = '__all__'
        exclude = ['unit']

        widgets = {
            'activity': forms.TextInput(attrs={"class": "form-control", "placeholder": "Event title"}),
            'facility': forms.Select(attrs={"class": "form-control"}),
            'date_needed': forms.DateInput(attrs={"class": "form-control"}),
            'priority_level': forms.Select(attrs={"class": "form-control"}),
            'starting_time': forms.Select(attrs={"class": "form-control"}),
            'ending_time': forms.Select(attrs={"class": "form-control"}),
            'number_of_pax': forms.NumberInput(attrs={"class": "form-control"}),
            'POC': forms.TextInput(attrs={"class": "form-control"}),
            'remarks': forms.Textarea(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"}),
            'mod_comments': forms.Textarea(attrs={"class": "form-control"}),
        }

class BookingRequestForm(ModelForm):
    class Meta:
        model = BookingRequest
        fields = '__all__'