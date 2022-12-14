from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('meetings.urls')),
    path('api/user/', include('auth_app.urls'), name='auth'),
    path('docs/', include_docs_urls(title='EventAPI')),
    path('schema', get_schema_view(
        title = 'EventAPi',
        description = 'Recruitment task for tango',
        version = '1.0.0',
    ), name = 'tango-event-schema'),
]
