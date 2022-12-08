from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('approved', views.all_accepted, name='all_accepted'),
    path('requests', views.all_pending, name='all_pending'),
    path('users/<str:pk>/', views.users, name='users'),
    path('request/<str:pk>/', views.indivrequest, name='indivrequest'),

    path('create_booking', views.createBooking, name='createBooking'),
    path('update_booking/<str:pk>', views.updateBooking, name='updateBooking'),
    path('delete_booking/<str:pk>', views.deleteBooking, name='deleteBooking'),

    path('login', views.loginpage, name='login'),
    path('logout', views.logoutuser, name='logout')
]