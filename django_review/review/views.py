from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import renderers
from rest_framework.authtoken import views as rest_framework_views

from .models import Review
from .serializers import ReviewRUDSerializer, UserSerializer


class ReviewHighlight(generics.GenericAPIView):
	queryset = Review.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer,)
	
	def get(self, request, *args, **kwargs):
		review = self.get_object()
		return Response(review.highlighted)


@api_view(['GET'])
def api_root(request, format = None):
	return Response({
		# 'users': reverse('user-list', request = request, format = format),
		'reviews': reverse('review-list', request = request, format = format)
	})


class ReviewList(APIView):
	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
	
	def get(self, request, format = None):
		snippets = Review.objects.all().filter(user = self.request.user)
		serializer = ReviewRUDSerializer(snippets, many = True)
		return Response(serializer.data)
	
	def post(self, request, format = None):
		serializer = ReviewRUDSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
	def get_object(self, pk):
		try:
			return Review.objects.get(pk = pk, user = self.request.user)
		except Review.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format = None):
		Review = self.get_object(pk)
		serializer = ReviewRUDSerializer(Review)
		return Response(serializer.data)
	
	def put(self, request, pk, format = None):
		Review = self.get_object(pk)
		serializer = ReviewRUDSerializer(Review, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format = None):
		Review = self.get_object(pk)
		Review.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
