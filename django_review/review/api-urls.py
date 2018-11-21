from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_framework_views


from . import views



urlpatterns = [
	path('', views.api_root),
	path('review/<int:pk>/highlight/', views.ReviewHighlight.as_view(), name = 'review-highlight'),
    path('review/', views.ReviewList.as_view(), name = 'review-list'),
	path('review/<int:pk>', views.ReviewDetail.as_view(), name = 'review-detail'),
	path('auth/', rest_framework_views.obtain_auth_token, name='get_auth_token'),
	
]

urlpatterns = format_suffix_patterns(urlpatterns)
