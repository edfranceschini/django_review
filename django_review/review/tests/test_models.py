from django.contrib.auth.models import User
from review.models import Profile, Company, Review
from rest_framework.authtoken.models import Token

import pytest

@pytest.mark.django_db
class TestModels:
	
	def test_user(self):
		user = create_test_user()
		assert user.id is not None
		
	def test_profile_user(self):
		user = create_test_user()
		profile = Profile.objects.get(user = user)
		assert profile.user_id == user.id
		
	def test_profile_repr(self):
		user = create_test_user()
		profile = Profile.objects.get(user = user)
		assert str(profile) == user.username
		
	def test_auth_token(self):
		user = create_test_user()
		assert Token.objects.get(user = user)
		
	def test_company(self):
		company = create_test_compasny()
		assert str(company) == company.name
		
	def test_review_repr(self):
		review = create_test_review(rating = 1)
		assert str(review) == review.title
		
	def test_fail_review_rating(self):
		with pytest.raises(ValueError) as e_info:
			review = create_test_review(rating = 6)
		
	def test_review_ip_address(self):
		review = create_test_review(rating = 1)
		assert review.ip_address is not None
		
	def test_review_submission_date(self):
		review = create_test_review(rating = 1)
		assert review.sub_date is not None
		
		
	###### Models creation methods
		
def create_test_user():
	user = User.objects.create(first_name = 'Johnny',
	                           last_name = 'Test',
	                           username = 'jtest')
	user.save()
	return user


def create_test_compasny():
	company = Company.objects.create(name = 'TestCrashDummies', address = 'Test site #1')
	company.save()
	return company
	
	
def create_test_review(rating):
	review = Review.objects.create(user = create_test_user(),
	                               company = create_test_compasny(),
	                               title = 'Test Coverage',
	                               rating = rating,
	                               summary = 'Test summary',
	                               )
	review.save()
	return review