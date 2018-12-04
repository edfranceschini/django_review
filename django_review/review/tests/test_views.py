from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from review.models import Review
from review.tests.test_models import create_test_user, create_test_compasny



class ReviewTests(APITestCase):
	
	def test_list_reviews_unauthorized(self):
		response = self.client.get('/api/v1/reviews/')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
	
	def test_create_review(self):
		
		url = '/api/v1/reviews/'
		data = {
					'user': create_test_user().id,
		            'company': create_test_compasny().id,
					'title': 'Test Review',
					'rating': 2,
					'summary': 'Test of summary',
		        }
		response = self.client.post(url, data)
		self.assertEqual(len(response.data), 1)

