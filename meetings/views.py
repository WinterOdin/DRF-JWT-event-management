from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from django.db.models import Q

from .serializers import EventSerializer
from .filters import EventFilter
from .models import Event

"""
The code at the end is my first try at this. 
The second one is refactored 
"""


class EventViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    filterset_class = EventFilter

    def get_queryset(self):
        user_id = self.request.user.id

        available = Event.objects.filter(
            Q(invited__id=user_id) | Q(place__manager_id=user_id)
        )
        return available

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def create(self, request, **kwargs):
    #     """
    #     Overrides the standard create method so that we can set User,
    #     based on requesting user
    #     """
    #     event_data = self.request.data
    #     print(event_data)
    #     event_data._mutable = True
    #     event_data['owner'] = self.request.user.id
    #     print(self.request.user.id)

    #     serializer = EventSerializer(data=event_data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def query_filter(object_name, user_id):

#     data  = object_name.objects.filter(
#             Q(invited__id = user_id) |
#             Q(place__manager_id = user_id)
#     )
#     return data


# class EventList(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = EventSerializer

#     def get_queryset(self):
#         user = self.request.user
#         available = query_filter(Event, user.id)

#         return available

# class EventDetailFilter(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = EventSerializer
#     filterset_class = EventFilter

#     def get_queryset(self):
#         user = self.request.user
#         available = query_filter(Event, user.id)

#         return available
