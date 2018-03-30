from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox(executable_path=r"geckodriver/geckodriver")
	def tearDown(self):
		time.sleep(8)
		self.browser.quit()		
	def test_tracking(self):
		self.browser.get('http://localhost:8000/admin')
		username = self.browser.find_element_by_xpath('//input[@id="id_username"]')
		username.send_keys("admin")
		password = self.browser.find_element_by_xpath('//input[@id="id_password"]')
		password.send_keys('amiyaab123')
		self.browser.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
		self.browser.get('http://localhost:8000/tracking/submission')
		self.assertIn("Avrtti", self.browser.title)
		title = self.browser.find_element_by_xpath('//input[@id="id_title"]')
		title.send_keys("Master in Computer Application")
		selectbox = self.browser.find_element_by_xpath('//select[@id="id_type_of_submission"]')
		all_options = selectbox.find_elements_by_tag_name("option")
		for option in all_options:
		    print("Value is: %s" % option.get_attribute("value"))
		    print(option.text)
		    if option.text == "Workbook":
		    	option.click()

		grade = self.browser.find_element_by_xpath('//input[@id="id_grade"]')
		grade.send_keys("Masters")
		subject = self.browser.find_element_by_xpath('//input[@id="id_subject"]')
		subject.send_keys("Data Structure")
		description = self.browser.find_element_by_xpath('//textarea[@id="id_description"]')
		description.send_keys("Data Structure")
		url = self.browser.find_element_by_xpath('//input[@id="id_dat_link"]')
		url.send_keys("dat://mca-amiyatulu.hashbase.io")
		self.browser.find_element_by_id("submitbutton").click()
		self.fail('Finish the test!')


if __name__ == "__main__":
	unittest.main()

