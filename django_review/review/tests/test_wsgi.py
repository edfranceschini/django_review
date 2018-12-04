from webtest import TestApp
from django_review.wsgi import application


class WSGI_Test:
	app = TestApp(application)
	
	
	def test_index_page(self):
		res = self.app.get('/')
		assert res.status == '200 OK'
