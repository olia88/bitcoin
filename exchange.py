import unittest
from ddt import ddt, unpack, data
from selenium import webdriver

@ddt
class Exchange(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.get("https://bitcoin-stage.quartsoft.com/")
		self.driver.get("https://bitcoin-stage.quartsoft.com/login")
		# find form fields
		email_field = self.driver.find_element_by_id("email")
		password_field = self.driver.find_element_by_id("password")
		login_btn = self.driver.find_element_by_tag_name("button")
		# fill fields with data
		email_field.send_keys("olia.yemets@gmail.com")
		password_field.send_keys("Magento1")
		login_btn.click()
		exchage_link = self.driver.find_element_by_link_text('Exchange')
		self.assertTrue(exchage_link)

	def test_exchange_with_empty_fields(self):
		driver = self.driver
		exchage_link = driver.find_element_by_link_text('Exchange')
		exchage_link.click()
		exhange_title = driver.find_element_by_class_name('exchange-title')
		exhange_title.is_displayed()
		# press exchange button
		button = driver.find_element_by_css_selector("button[class ='btn col-xs-12 exchange-submit__btn btn-primary']")
		button.click()
		error_fields_is_reqiered = driver.find_elements_by_class_name("md-error")
		# check that 2 error messages are displayed
		self.assertEqual(len(error_fields_is_reqiered), 2)

	def test_exchange_with_negative_amount_from(self):
		driver = self.driver
		exchage_link = driver.find_element_by_link_text('Exchange')
		exchage_link.click()
		exhange_title = driver.find_element_by_class_name('exchange-title')
		exhange_title.is_displayed()
		# find amount from field
		give_btc = driver.find_element_by_id("amount_from-control")
		give_btc.send_keys("-2")
		# press exchange button
		button = driver.find_element_by_css_selector("button[class ='btn col-xs-12 exchange-submit__btn btn-primary']")
		button.click()
		error_fields_is_reqiered = driver.find_elements_by_class_name("md-error")
		# check that 2 error messages are displayed
		self.assertEqual(len(error_fields_is_reqiered), 2)

	def test_exchange_with_negative_amount_to(self):
		driver = self.driver
		exchage_link = driver.find_element_by_link_text('Exchange')
		exchage_link.click()
		exhange_title = driver.find_element_by_class_name('exchange-title')
		exhange_title.is_displayed()
		# find amount from field
		give_btc = driver.find_element_by_id("amount_to-control")
		give_btc.send_keys("-2")
		# press exchange button
		button = driver.find_element_by_css_selector("button[class ='btn col-xs-12 exchange-submit__btn btn-primary']")
		button.click()
		error_fields_is_reqiered = driver.find_elements_by_class_name("md-error")
		# check that 2 error messages are displayed
		self.assertEqual(len(error_fields_is_reqiered), 2)


if __name__ == "__main__":
	unittest.main()