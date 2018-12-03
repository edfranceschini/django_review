from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view),
    path('admin/', admin.site.urls),
    path('api/', include('review.api-urls')),
    
]
