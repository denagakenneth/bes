from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException


MAX_WAIT = 10
class BSMSTest(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()

   
    
    def wait_for_table(self, row_text):        
        start_time = time.time()
        while True:  
             try:                
                 table = self.browser.find_element_by_id('id_table')                  
                 rows = table.find_elements_by_tag_name('tr')                
                 self.assertIn(row_text, [row.text for row in rows])
                 return
             except (AssertionError, WebDriverException) as e:  
                 if time.time() - start_time > MAX_WAIT:  
                     raise e                  
                 time.sleep(0.5)  
 
    def test_for_first_entry(self):       

        self.browser.get('http://localhost:8000')
       #self.browser.get(self.live_server_url)
        self.assertIn('BARANGAY EVENT SCHEDULE', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('REGISTER YOUR INFORMATION', header_text)  
         
        
        inputlnmae = self.browser.find_element_by_id('lastname')
        inputfname = self.browser.find_element_by_id('firstname')
        inputmname = self.browser.find_element_by_id('middlename')
        inputrradd = self.browser.find_element_by_id('rraddress')
        inputrrrage = self.browser.find_element_by_id('rrage')
        inputrcnum = self.browser.find_element_by_id('rccnumber')
        inputrrruname = self.browser.find_element_by_id('rruname')
        inputrrrpass = self.browser.find_element_by_id('rrpass')

        self.assertEqual(inputlnmae.get_attribute('placeholder'),'Enter Your Last Name')
        self.assertEqual(inputfname.get_attribute('placeholder'),'Enter Your First Name')
        self.assertEqual(inputmname.get_attribute('placeholder'),'Enter Your Middle Name')
        self.assertEqual(inputrradd.get_attribute('placeholder'),'Enter Your Address')
        self.assertEqual(inputrrrage.get_attribute('placeholder'),'Enter Your Age')
        self.assertEqual(inputrcnum.get_attribute('placeholder'),'Enter Your Contact Number')
        self.assertEqual(inputrrruname.get_attribute('placeholder'),'Enter Your Username')
        self.assertEqual(inputrrrpass.get_attribute('placeholder'),'Enter Your Password')
        
        time.sleep(1)
        inputlnmae =  self.browser.find_element_by_id('lastname')
        inputlnmae.click()
        inputlnmae.send_keys('Denaga')
       
        time.sleep(1)
        inputfnmae =  self.browser.find_element_by_id('firstname')
        inputfnmae.click()
        inputfnmae.send_keys('Kenneth')
        
        time.sleep(1)
        inputmnmae =  self.browser.find_element_by_id('middlename')
        inputmnmae.click()
        inputmnmae.send_keys('Faller')

        time.sleep(1)
        inputrradd =  self.browser.find_element_by_id('rraddress')
        inputrradd.click()
        inputrradd.send_keys('Blk. 111 lot 8')

        time.sleep(1)
        inputrrrage =  self.browser.find_element_by_id('rrage')
        inputrrrage.click()
        inputrrrage.send_keys('18')

        time.sleep(1)
        inputrcnum =  self.browser.find_element_by_id('rccnumber')
        inputrcnum.click()
        inputrcnum.send_keys('0905-499-0958')

        time.sleep(1)
        inputrrruname =  self.browser.find_element_by_id('rruname')
        inputrrruname.click()
        inputrrruname.send_keys('kokoyoishi')
        
        time.sleep(1)
        inputrrrpass =  self.browser.find_element_by_id('rrpass')
        inputrrrpass.click()
        inputrrrpass.send_keys('88888888')

        
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()
        

        time.sleep(1)
        
        inputblocation= self.browser.find_element_by_id('bblocation')
        inputbcategory = self.browser.find_element_by_id('bbcategory')
        inputbdate = self.browser.find_element_by_id('bbdate')
        self.assertEqual(inputblocation.get_attribute('placeholder'),'Enter Court Location')
        self.assertEqual(inputbcategory.get_attribute('placeholder'),'Enter Event')
        self.assertEqual(inputbdate.get_attribute('placeholder'),'Enter Date')
        
        time.sleep(1)
        inputblocation =  self.browser.find_element_by_id('bblocation')
        inputblocation.click()
        inputblocation.send_keys('Area 1')
        
        time.sleep(1)
        inputbcategory =  self.browser.find_element_by_id('bbcategory')
        inputbcategory.click()
        inputbcategory.send_keys('Wedding')
        
        time.sleep(1)
        inputbdate =  self.browser.find_element_by_id('bbdate')
        inputbdate.click()
        inputbdate.send_keys('May 22, 2022')
        
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()
        
        
        time.sleep(1)
        
        inputblocation =  self.browser.find_element_by_id('bblocation')
        inputblocation.click()
        inputblocation.send_keys('Kadiwa')
        
        time.sleep(1)
        inputbcategory =  self.browser.find_element_by_id('bbcategory')
        inputbcategory.click()
        inputbcategory.send_keys('Binyag')
        
        time.sleep(1)
        inputbdate =  self.browser.find_element_by_id('bbdate')
        inputbdate.click()
        inputbdate.send_keys('May 26, 2022')
        
        
        bAdd = self.browser.find_element_by_id('bAdd')
        bAdd.click()
        time.sleep(1)

