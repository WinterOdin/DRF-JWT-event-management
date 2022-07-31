from django.utils.translation import gettext_lazy as _
from django.db.models import CheckConstraint, Q, F
from django.core.exceptions import ValidationError
from auth_app.models import CustomUser
from django.utils import timezone
from datetime import timedelta
from django.db import models


# Create your models here.
class ConferenceLocation(models.Model):
    OPTIONS = [
        ('available','available'),
        ('booked','booked')
    ]

    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    booked = models.CharField(max_length=15, choices=OPTIONS, null=True, blank=True)


    def __str__(self):
        return f'Conference room: {self.name} managed {self.manager}'

class Event(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='meeting_owner')
    place = models.ForeignKey(ConferenceLocation, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    agenda = models.TextField(_(
        'agenda'), max_length=200, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    invited = models.ManyToManyField(CustomUser, related_name='meeting_participant')

    def clean(self):

        if self.start_date > self.end_date:
            raise ValidationError({'end_date':'End date cannot be smaller then start date.'})
        
        if self.end_date > (self.start_date + timedelta(hours=8)):
            raise ValidationError({'end_date':'Meetings should not exceed 8 hours.'})

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(end_date__lte=F('start_date') + timedelta(hours=8)), 
                name='check_end_datetime',
            ),
        ]
    
            

    def __str__(self):
        return f'Event owner: {self.owner}'