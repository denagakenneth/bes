from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('PT Schedule', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Schedule Form', headerText)
		inpName = self.browser.find_element_by_id('studentName')
		inpNameF = self.browser.find_element_by_id('FstudentName')
		inpNameL = self.browser.find_element_by_id('LstudentName')
		inpNameM = self.browser.find_element_by_id('MstudentName')
		btn_button = self.browser.find_element_by_id('btn')
		self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
		inpName.click()
		inpName.send_keys('Scathach')
		time.sleep(1)
		inpNameF.send_keys('Skadi')
		time.sleep(1)
		inpNameL.send_keys('Morgan')
		time.sleep(1)
		inpNameM.send_keys('Eresh')
		time.sleep(1)
		btn_button.click()
		time.sleep(1)

	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('scheduleTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Scathach', [rows.text for rows in rows])

if __name__ == '__main__':
	unittest.main(warnings='ignore')