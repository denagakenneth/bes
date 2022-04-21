# from selenium import webdriver
# import unittest

# class PageTest(unittest.TestCase):
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()
# 	#def tearDown(self):
# 		#self.browser.quit()
# 	def test_browser_title(self):
# 		self.browser.get('http://localhost:8000')
# 		self.assertIn('Philikula',self.browser.title)
# 		#self.fail('Finish the test!')
# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Barangay Event Schedule', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Resident Form', headerText)
		inpName = self.browser.find_element_by_id('applicantName')
		btn_P_button = self.browser.find_element_by_id('btnP')
		self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
		inpName.click()
		inpName.send_keys('1: Mr Arthur Leni')
		time.sleep(1)
		btn_Pindot_button.click()
		time.sleep(1)
		 
		'''S
		inputbox = self.browser.find_element_by_id('idNewEntry')
		self.assertEqual(inputbox.get_attribute('placeholder')), 'Persons name you have'
		inputbox.send_keys('Mickey Mouse')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		table = self.browser.find_element_by_id('idListTable')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(any(row.text == '1: Mickey Mouse'))
		'''
		# table = self.browser.find_element_by_id('regtable')
		# rows = table.find_elements_by_tag_name('tr')
		#self.assertTrue(any(rows.text == '1: Mr.Jim_Guy'), "No Table Here!")
		#self.assertIn('1: Mr Arthur Leni, [rows.text for rows in rows])

	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('regtable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Mr.Jim_Guy', [rows.text for rows in rows])

if __name__ == '__main__':
	unittest.main(warnings='ignore')
