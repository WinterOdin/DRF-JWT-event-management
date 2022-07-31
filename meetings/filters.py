import django_filters 
from .models import Event

class EventFilter(django_filters.FilterSet):

    class Meta:
        model = Event
        fields = {
            'start_date':['icontains','lte','gte'],
            'place__id':['iexact'],
            'name':['icontains'],
            'agenda':['icontains']
        }