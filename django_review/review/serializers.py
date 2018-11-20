from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Review


class ReviewRUDSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = ('id', 'user', 'company', 'title', 'rating', 'summary', 'ip_address', 'sub_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	review = serializers.HyperlinkedRelatedField(many = True, view_name = 'review-detail', read_only = True)
	user = serializers.ReadOnlyField(source = 'user.username')
	
	class Meta:
		model = User
		fields = ('id', 'user', 'review')
