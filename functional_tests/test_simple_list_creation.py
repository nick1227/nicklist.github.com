

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get(self.server_url)
		#self.browser.get('http://192.168.136.6:8088/ws/')
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		#1
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
		
		inputbox.send_keys(' Buy peacock feathers')
		
		inputbox.send_keys(Keys.ENTER)
		#self.check_for_row_in_list_table('1: Buy peacock feathers')
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# 2
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys(' Use peacock feathers to make a fly')	
		inputbox.send_keys(Keys.ENTER)
		
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		#table = self.browser.find_element_by_id('id_list_table')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
		#				"New to-do item did not appear in table ---its text was:\n%s " %(table.text,))
		#self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		
		
		self.browser.quit()
		self.browser = webdriver.Firefox()
		
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')	
		inputbox.send_keys(Keys.ENTER)
		
		
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url,edith_list_url)	

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)
		
