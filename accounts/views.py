from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta

# Create your views here.
@login_required(login_url='login')
@home_page_filter()
def home(request):
    all_cus = customer.objects.order_by('name')

    all_req = BookingRequest.objects.order_by('date_created')

    total_pend = len(BookingRequest.objects.filter(status='Pending', date_needed__gte = date.today()))

    upcoming = date.today() + relativedelta(weeks=+1)

    upcoming_appr = BookingRequest.objects.filter(status = 'Approved', date_needed__gte = date.today(), date_needed__lte = upcoming).order_by('date_needed', 'starting_time')
    upcoming_pend = BookingRequest.objects.filter(status = 'Pending', date_needed__gte = date.today(), date_needed__lte = upcoming)

    context = {'all_cus': all_cus, 'all_req': all_req, 'upcoming_appr': upcoming_appr, 'upcoming_pend': upcoming_pend, 'total_pend': total_pend}
    return render(request, 'accounts/home.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['moderator', 'customer'])
def all_pending(request):
    mod = False
    if request.user.groups.all()[0].name== 'moderator':
        mod = True

    pending_set = BookingRequest.objects.filter(status='Pending').order_by('date_needed', 'facility', '-priority_level', 'date_created')

    high_pri_pend = len(BookingRequest.objects.filter(status='Pending', priority_level=3))
    med_pri_pend = len(BookingRequest.objects.filter(status='Pending', priority_level=2))
    low_pri_pend = len(BookingRequest.objects.filter(status='Pending', priority_level=1))

    filter = AllRequestsFilter(request.GET, pending_set)

    pending_set = filter.qs

    context = {'pending_set': pending_set, 'filter': filter, 'mod': mod, 'high_pri_pend': high_pri_pend, 'med_pri_pend': med_pri_pend,"low_pri_pend":low_pri_pend}

    return render(request, 'accounts/pending.html', context)

@login_required(login_url='login')
def all_accepted(request):
    
    accepted_set = BookingRequest.objects.filter(status='Approved').order_by('date_needed', 'facility', 'starting_time')
    if request.user.groups.all()[0].name == 'duty clerk':
        accepted_set = BookingRequest.objects.filter(status='Approved', date_needed = date.today()).order_by('starting_time')
    
    filter = AllRequestsFilter(request.GET, queryset=accepted_set)
    accepted_set = filter.qs

    context = {'accepted_set': accepted_set, 'filter': filter}
    
    return render(request, 'accounts/accepted.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['moderator', 'customer'])
def users(request, pk):
    user = customer.objects.get(id=pk)

    bookings = user.bookingrequest_set.order_by('status', 'date_needed', 'facility', 'starting_time')
    total_rejected = len(user.bookingrequest_set.filter(status='Rejected'))
    total_approved = len(user.bookingrequest_set.filter(status='Approved'))
    total_pending = len(user.bookingrequest_set.filter(status='Pending'))
    filter = UserRequestFilter(request.GET, queryset=bookings)
    bookings = filter.qs

    context = {'user': user, 'bookings': bookings, 'total_rejected': total_rejected, 'total_approved':total_approved, 'total_pending':total_pending, 'filter':filter}
    return render(request, 'accounts/users.html', context)

@login_required(login_url='login')
def indivrequest(request, pk):
    owner = False
    mod = False
    curr_request = BookingRequest.objects.get(id=pk)
    group = request.user.groups.all()[0].name
    if group == 'moderator':
        mod = True
    elif group == 'customer' and request.user.customer == curr_request.unit:
        owner = True
    
    context = {'request': curr_request, 'mod': mod, 'owner': owner}
    return render(request, 'accounts/indivrequest.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createBooking(request):
    user = request.user.customer

    customer_form = UserSideBookingRequestForm()

    if request.method == 'POST':
        actual_form = request.POST.copy()
        actual_form['unit'] = user
        actual_form['status'] = 'Pending'
        actual_form['mod_comments'] = 'Nil'
        form = BookingRequestForm(actual_form)
        if form.is_valid():
            curr_event_st = int(actual_form['starting_time'])
            curr_event_ed = int(actual_form['ending_time'])
            if curr_event_ed < curr_event_st:
                print('Error')
                messages.info(request, "You cannot end before you start!")
            elif datetime.strptime(actual_form['date_needed'], '%Y-%m-%d').date() < date.today():
                messages.info(request, "You cannot make a request after the date has already passed!")
            else:
                form.save()
                return redirect('/')
    context = {'form': customer_form, 'curr_user': user}
    return render(request, 'accounts/booking_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['moderator', 'customer'])
def updateBooking(request, pk):
    No_collisions= True
    updating = True
    owner = False
    group = request.user.groups.all()[0].name
    booking = BookingRequest.objects.get(id=pk)
    same_time_place_approved = BookingRequest.objects.filter(status = "Approved", date_needed = booking.date_needed, facility = booking.facility).order_by('starting_time')
    same_time_place_pending = BookingRequest.objects.filter(status = "Pending", date_needed = booking.date_needed, facility = booking.facility).order_by('starting_time')
    if request.method == 'GET' and group == 'moderator':
        form = StaffSideBookingRequestForm(instance=booking)
    elif request.method == 'GET' and group == 'customer' and booking.status == 'Pending':
        if booking.unit != request.user.customer:
            return redirect('/')
        else:
            owner = True
            form = UserSideBookingRequestForm(instance=booking)
    elif request.method == 'GET' and group == 'customer' and booking.status != 'Pending':
        return redirect('/')

    if request.method == 'POST' and group == 'moderator':
        actual_form = request.POST.copy()
        actual_form['unit'] = booking.unit
        form = BookingRequestForm(actual_form, instance=booking)
        if form.is_valid():
            curr_event_st = int(actual_form['starting_time'])
            curr_event_ed = int(actual_form['ending_time'])
            if curr_event_ed <= curr_event_st:
                No_collisions = False
                messages.info(request, "You cannot end before you start!")
            if datetime.strptime(actual_form['date_needed'], '%Y-%m-%d').date() < date.today():
                No_collisions = False
                messages.info(request, "You cannot make a request after the date has already passed!")
            if actual_form['status'] == 'Approved':
                new_date = datetime.strptime(actual_form['date_needed'], '%Y-%m-%d').date()
                new_facility = actual_form['facility']
                same_time_place_approved = BookingRequest.objects.filter(status = "Approved", date_needed = new_date, facility = new_facility)
                for i in same_time_place_approved:
                    if i == booking:
                        pass
                    else:
                        if curr_event_st >= i.starting_time and curr_event_st < i.ending_time:
                            No_collisions = False
                            messages.info(request, f'{i.unit.name} {i.activity} already approved for {i.get_starting_time_display()} to {i.get_ending_time_display()} at {i.facility} on {i.date_needed}')
                        elif curr_event_ed > i.starting_time and curr_event_ed <= i.ending_time:
                            No_collisions = False
                            messages.info(request, f'{i.unit.name} {i.activity} already approved for {i.get_starting_time_display()} to {i.get_ending_time_display()} at {i.facility} on {i.date_needed}')
                        elif curr_event_st < i.starting_time and curr_event_ed > i.ending_time:
                            No_collisions = False
                            messages.info(request, f'{i.unit.name} {i.activity} already approved for {i.get_starting_time_display()} to {i.get_ending_time_display()} at {i.facility} on {i.date_needed}')
                
            if No_collisions:
                form.save()
                return redirect('/')
    elif request.method == 'POST' and group == 'customer':
        No_collisions = True
        actual_form = request.POST.copy()
        actual_form['unit'] = booking.unit
        actual_form['status'] = 'Pending'
        actual_form['mod_comments'] = booking.mod_comments
        curr_event_st = int(actual_form['starting_time'])
        curr_event_ed = int(actual_form['ending_time'])
        if curr_event_ed <= curr_event_st:
            No_collisions = False
            messages.info(request, "You cannot end before you start!")
        if datetime.strptime(actual_form['date_needed'], '%Y-%m-%d').date() < date.today():
            No_collisions = False
            messages.info(request, "You cannot make a request after the date has already passed!")
        form = BookingRequestForm(actual_form, instance=booking)
        if form.is_valid():
            if No_collisions:
                form.save()
                return redirect('/')


    

    context = {'form': form, 'owner': owner, 'booking':booking,'updating': updating, 'other_approved': same_time_place_approved, 'other_pending':same_time_place_pending}
    return render(request, 'accounts/booking_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def deleteBooking(request, pk):
    booking = BookingRequest.objects.get(id=pk)
    if request.method == 'GET' and request.user.customer != booking.unit:
        return redirect('/')
    if request.method == 'POST' and request.user.customer == booking.unit:
        booking.delete()
        return redirect('/')

    context = {'booking':booking}

    return render(request, 'accounts/delete_booking.html', context)


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        usernam = request.POST.get('username')
        passwo = request.POST.get('password')

        user = authenticate(request=request, username=usernam, password=passwo)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html')

def logoutuser(request):

    logout(request)

    return redirect('login')