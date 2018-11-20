from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views



urlpatterns = [
	path('', views.api_root),
	path('review/<int:pk>/highlight/', views.ReviewHighlight.as_view(), name = 'review-highlight'),
    path('auth/', include('rest_framework.urls'), name = 'api-root'),
    path('review/', views.ReviewList.as_view(), name = 'review-list'),
	path('review/<int:pk>', views.ReviewDetail.as_view(), name = 'review-detail'),

	
]

urlpatterns = format_suffix_patterns(urlpatterns)
