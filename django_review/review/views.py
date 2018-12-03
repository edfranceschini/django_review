from django.contrib.auth.models import User

from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer, UserSerializer


def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip


@api_view(['GET'])
def api_root(request, format = None):
	return Response({
		'users': reverse('user-list', request = request, format = format),
		'reviews': reverse('review-list', request = request, format = format)
	})


class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	
	@action(detail = True, renderer_classes = [renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		review = self.get_object()
		user = self.request.user
		return Response(review.highlighted.filter(user = user))
	
	def perform_create(self, serializer):
		ip = get_client_ip(self.request)
		serializer.save(user = self.request.user, ip_address = ip)
	
	def get_queryset(self):
		return Review.objects.all().filter(user = self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
