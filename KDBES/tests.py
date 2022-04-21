from django.urls import resolve
from django.test import TestCase
from KDBES.views import MainPage

class HomePageTest(TestCase):
	def test_root_url_resolves_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)
	
	def test_mainpage_if_ returns_correct_view(self):
	        request = HttpRequest()
	        response = MainPage(request)
	        html = response .content.decode('utf8')
	        self.assertTrue(html.startwith('<html>'))
	        self.assertIn('<title>barangay event schedule<title>', html)
	        self.assertTrue(html.endswith('</html>'))
