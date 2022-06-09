from django.urls import resolve
from django.test import TestCase
from KDBES.views import home_page

from KDBES.models import Bevent, Rinfo

from django.http import HttpRequest
from django.template.loader import render_to_string


class MyMainPage(TestCase):
    
   def test_my_mainpage_view(self):
       found = resolve('/')
       self.assertEqual(found.func, home_page)
      
   def test_correct_view(self):
       request = HttpRequest()
       response = home_page(request)
       expected_html = render_to_string('a.html')

   
   def test_saves_necessary(self): 
       self.client.get('/')        
       self.assertEqual(Bevent.objects.count(), 0)
      
class ListViewTest(TestCase):
 
   def test_uses_SInfotemplate(self):
       rinfo_ = Rinfo.objects.create()        
       response = self.client.get(f'/{rinfo_.id}/')
       self.assertTemplateUsed(response, 'b.html')
      
   def test_display_list_item(self):
       correct_rinfo = Rinfo.objects.create()
       Bevent.objects.create(blocation='Area 1', rinfo=correct_rinfo)
       Bevent.objects.create(bcategory='Wedding', rinfo=correct_rinfo)
       other_rinfo = Rinfo.objects.create()
       Bevent.objects.create(blocation='Other Location', rinfo=other_rinfo)
       Bevent.objects.create(bcategory='Other Event', rinfo=other_rinfo)        
      
       response = self.client.get(f'/{correct_rinfo.id}/')
     
       self.assertNotContains(response, 'Other Location')
       self.assertNotContains(response, 'Other Event')
   
   def test_displays_all(self):        
       rinfo_ = Rinfo.objects.create()        
       Bevent.objects.create(blocation='Area 1', rinfo=rinfo_)        
       Bevent.objects.create(bcategory='Wedding', rinfo=rinfo_)
   
   def test_passes_correct_template(self):       
       other_rinfo = Rinfo.objects.create()        
       correct_rinfo = Rinfo.objects.create()        
       response = self.client.get(f'/{correct_rinfo.id}/')
       self.assertEqual(response.context['rinfo'], correct_rinfo)  



 

class InfoTest(TestCase):


  def test_info(self):       
      other_rinfo = Rinfo.objects.create()        
      correct_rinfo = Rinfo.objects.create()        
      
      self.client.post(            
          f'/{correct_rinfo.id}/add_info',            
          data={'bblocation':'New Court Location','bbcategory': 'New Category','bbdate': 'New Date','bbbstime': 'New Start Time'})            
      
      self.assertEqual(Bevent.objects.count(), 1)        
      new_info= Bevent.objects.first()        
      self.assertEqual(new_info.bdate, 'New Date')       
      self.assertEqual(new_info.rinfo, correct_rinfo)
      
  def test_redirects_info(self):        
      other_rinfo = Rinfo.objects.create()        
      correct_rinfo = Rinfo.objects.create()        
      response = self.client.post(            
          f'/{correct_rinfo.id}/add_info',            
         data={'bblocation':'New Court Location','bbcategory': 'New Category','bbdate': 'New Date','bbbstime': 'New Start Time'})       
            
      self.assertRedirects(response, f'/{correct_rinfo.id}/')
      
class MyORMandKDBES(TestCase):

   def test_save_retrieve_info(self):
      rinfo_ = Rinfo()        
      rinfo_.save()
      
      first_info = Bevent()        
      first_info.blocation = 'Area 1' 
      first_info.rinfo =rinfo_ 
      first_info.save()        
               
      second_info = Bevent()      
      second_info.blocation = 'Kadiwa'
      second_info.rinfo = rinfo_         
      second_info.save()
       
       
      saved_rinfo = Rinfo.objects.first()          
      self.assertEqual(saved_rinfo, rinfo_)
                 
      saved_infos = Bevent.objects.all()
      self.assertEqual(saved_infos.count(), 2)
       
      first_saved_info = saved_infos[0]
      second_saved_info = saved_infos[1]             
      self.assertEqual(first_saved_info.blocation, 'Area 1')
      self.assertEqual(first_saved_info.rinfo, rinfo_)
      self.assertEqual(second_saved_info.blocation, 'Kadiwa')
      self.assertEqual(second_saved_info.rinfo, rinfo_)

  