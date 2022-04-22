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
		inpName = self.browser.find_element_by_id('resName')
		inpNameF = self.browser.find_element_by_id('Fresname')
		inpNameL = self.browser.find_element_by_id('LresName')
		inpNameM = self.browser.find_element_by_id('MresName')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
		inpName.click()
		inpName.send_keys('Arthur')
		time.sleep(1)
		inpNameF.send_keys('Arc')
		time.sleep(1)
		inpNameL.send_keys('Leni')
		time.sleep(1)
		inpNameM.send_keys('l')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)

	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('resTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Arthur', [rows.text for rows in rows])

if __name__ == '__main__':
	unittest.main(warnings='ignore')