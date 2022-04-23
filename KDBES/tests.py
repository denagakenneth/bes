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

		resp = self.client.post('/', data={'MresName' :'MNameNew'})
		self.assertIn('MNameNew', resp.content.decode())
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

		resp = self.client.post('/', data={'resContact' :'ContactNew'})
		self.assertIn('ContactNew', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')

'''class ORM(TestCase):

   def test_saving_and_retrieving_items(self):
      list_ = List()        
      list_.save()
      
      first_item = Item()        
      first_item.donatorsname = 'The first (ever) list item' 
      first_item.list = list_ 
      first_item.save()        
               
      second_item = Item()      
      second_item.am = 'Item the second'
      second_item.list = list_         
      second_item.save()
       
       
      saved_list = List.objects.first()          
      self.assertEqual(saved_list, list_)
                 
      saved_items = Item.objects.all()
      self.assertEqual(saved_items.count(), 2)
       
      first_saved_item = saved_items[0]
      second_saved_item = saved_items[1]      	     
      self.assertEqual(first_saved_item.fullname, 'The first (ever) list item')
      self.assertEqual(first_saved_item.list, list_)
      self.assertEqual(second_saved_item.ni, 'Item the second')
      self.assertEqual(second_saved_item.list, list_)'''

