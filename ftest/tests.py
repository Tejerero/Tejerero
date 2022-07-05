from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3
class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	#def tearDown(self):
	#	self.browser.quit()

	def checking_if_in_table_list(self,row_text):
		start_time = time.time()
		while time.time()-start_time<cWait:
			#time.sleep(0.2)
			try:
				table = self.browser.find_element_by_id('infoTable')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time()-start_time>cWait:
					raise e
		
	def test_another_entry_different_url(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Flavours 101', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Cooking Class Booking', headerText)

		ClientFirstname = self.browser.find_element_by_id('firstname')
		ClientSurname = self.browser.find_element_by_id('surname')
		ClientNumber = self.browser.find_element_by_id('number')
		ClientEmail = self.browser.find_element_by_id('email')

		self.assertEqual(ClientFirstname.get_attribute('placeholder'),'First Name')

		btnNext = self.browser.find_element_by_id('btnNext')

		self.assertEqual(ClientSurname.get_attribute('placeholder'),'Surname')
		self.assertEqual(ClientNumber.get_attribute('placeholder'),'Phone Number')
		self.assertEqual(ClientEmail.get_attribute('placeholder'),'Email')

		ClientFirstname.click()
		ClientFirstname.send_keys('Aprilyn')
		time.sleep(0.1)
		ClientSurname.click()
		ClientSurname.send_keys('Tejerero')
		time.sleep(0.1)
		ClientNumber.click()
		ClientNumber.send_keys('09285764024')
		time.sleep(0.1)
		ClientEmail.click()
		ClientEmail.send_keys('aprilyn.tejerero@gsfe.tupcavite.edu.ph')
		time.sleep(0.1)

		btnNext.click()
		#self.checking_if_in_table_list('1. Aprilyn Tejerero 09285764024 aprilyn.tejerero@gsfe.tupcavite.edu.ph')
		#viewlist_url = self.browser.current_url
		#self.assertRegex(viewlist_url, '/flsys/.+')
