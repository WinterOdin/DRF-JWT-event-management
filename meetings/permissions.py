# from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser, SAFE_METHODS

# class EventAttendancePermission(BasePermission):
#     message = "You are not invited to this event."

#     def has_object_permission(self, request, view, object):
#         return request.method == 'GET' and object.invited(request.user)

# class EventOwnerPermission(BasePermission):
#     def has_object_permission(self, request, view, object):
#         if request.method in SAFE_METHODS:
#             return True
#         return object.owner == request.user


