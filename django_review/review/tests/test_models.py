
import pytest

@pytest.mark.django_db
class TestModels:
	
	def test_profile_user(self):
		profile = mixer.blend('review.Profile')
		assert profile.username != ''
	