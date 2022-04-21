from django.test import TestCase
from django.urls import resolve
from msystem.views import MainPage
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve

class HomePageTest(TestCase):
	"""
	def test_root_url_resolves_to_mainpage_view(self): 
		found=resolve('/')
		self.assertEqual(found.func, MainPage)
		
	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>Philikula</title>', html)
		self.assertTrue(html.endswith(''))

		stringPage = render_to_string('mainpage.html')
		self.assertEqual(html, stringPage)
		self.assertTemplateUsed(response, 'mainpage.html')"""
def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	
def test_responding_post_request(self):
		resp = self.client.post('/', data={'attribute' :'NewName'})
		self.assertIn('NewName', resp.content.decode())
		self.assertInTemplateUsed(resp, 'mainpage.html')
