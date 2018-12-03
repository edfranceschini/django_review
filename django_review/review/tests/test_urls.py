from django.urls import reverse, resolve

class TestUrls:
	
	def test_schema_url(self):
		path = reverse('schema')
		assert resolve(path).view_name == 'schema'
		
		