from django.contrib import admin
from .models import ConferenceLocation, Event
# Register your models here.


admin.site.register(ConferenceLocation)
admin.site.register(Event)