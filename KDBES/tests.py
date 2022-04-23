#from django.urls import resolve
from django.test import TestCase
from KDBES.views import MainPage
#from django.http import HttpRequest
#from django.template.loader import render_to_string
#from django.urls import resolve
#from django.urls import render
#from django.urls import response

class HomePageTest(TestCase):

	def test_mainpage_as_seen_client(self):
		resp = self.client.get('/')
		self.assertTemplateUsed(resp, 'mainpage.html')
	
	def test_responding_post_request(self):
		resp = self.client.post('/', data={'brgyid' :'idNew'})
		self.assertIn('idNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'FresName' :'FNameNew'})
		self.assertIn('FNameNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'LresName' :'LNameNew'})
		self.assertIn('LNameNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'resAddress' :'AddressNew'})
		self.assertIn('AddressNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')

		resp = self.client.post('/', data={'resAge' :'AgeNew'})
		self.assertIn('AgeNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')