from django.urls import path
from .views import CreateNewUser, BlacklistToken

urlpatterns = [
    path('create/', CreateNewUser.as_view(), name='newuser'),
    path('logout/blacklist/', BlacklistToken.as_view(),
        name='blacklist')
]
