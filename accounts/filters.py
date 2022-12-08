from django.db.models import fields
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class AllRequestsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_needed", lookup_expr='gte')
    end_date = DateFilter(field_name="date_needed", lookup_expr='lte')
    title = CharFilter(field_name="activity", lookup_expr='icontains')
    class Meta:
        model = BookingRequest
        fields = ['unit', 'facility', 'priority_level']


class UserRequestFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_needed", lookup_expr='gte')
    end_date = DateFilter(field_name="date_needed", lookup_expr='lte')
    title = CharFilter(field_name="activity", lookup_expr='icontains')
    class Meta:
        model = BookingRequest
        fields = ['facility', 'priority_level', 'status']

