from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authtoken_views

from . import views

router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('token/obtain/', authtoken_views.obtain_auth_token, name = 'token'),
    path('auth/', include('rest_framework.urls'), name = 'auth'),
    path('v1/', include(router.urls)),
]