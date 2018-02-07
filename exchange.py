import unittest
from ddt import ddt, unpack, data
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

	def test_exchange_with_not_numeric_amount_to(self):
		driver = self.driver
		exchage_link = driver.find_element_by_link_text('Exchange')
		exchage_link.click()
		exhange_title = driver.find_element_by_class_name('exchange-title')
		exhange_title.is_displayed()
		# find amount from field
		give_btc = driver.find_element_by_id("amount_to-control")
		give_btc.send_keys("test")
		# press exchange button
		button = driver.find_element_by_css_selector("button[class ='btn col-xs-12 exchange-submit__btn btn-primary']")
		button.click()
		error_fields_is_reqiered = driver.find_elements_by_class_name("md-error")
		# check that 2 error messages are displayed
		self.assertEqual(len(error_fields_is_reqiered), 3)

	def test_exchange_with_not_numeric_amount_from(self):
		driver = self.driver
		exchage_link = driver.find_element_by_link_text('Exchange')
		exchage_link.click()
		exhange_title = driver.find_element_by_class_name('exchange-title')
		exhange_title.is_displayed()
		# find amount from field
		give_btc = driver.find_element_by_id("amount_from-control")
		give_btc.send_keys("test")
		# press exchange button
		button = driver.find_element_by_css_selector("button[class ='btn col-xs-12 exchange-submit__btn btn-primary']")
		button.click()
		error_fields_is_reqiered = driver.find_elements_by_class_name("md-error")
		# check that 2 error messages are displayed
		self.assertEqual(len(error_fields_is_reqiered), 3)

	def test_exchange_with_amount_from_bigger_than_amount_in_wallet(self):
		driver = self.driver
		current_language = driver.find_element_by_css_selector("li[class='language dropdown']").text
		if current_language == "EN":
			pass
		else:
			current_language.click()
			language_dropdown = driver.find_element_by_class_name("dropdown-toggle")
			en = driver.find_element_by_link_text("en").click()
		# go to wallet page
		account_dropdown = driver.find_element_by_css_selector("li[class='account dropdown']")
		dropdown = ActionChains(driver)\
			.move_to_element(account_dropdown)\
			.click(driver.find_element_by_xpath("//a[@href='/wallets']"))\
			.perform()
		# grab btc balance
		wait = WebDriverWait(driver, 20)
		wait.until(EC.presence_of_element_located((By.XPATH, ".//tr[1]//td[2]")))
		btc_balance = driver.find_element_by_xpath(".//tr[1]//td[2]").text
		# go to exchange page
		exchage_link = driver.find_element_by_link_text('Exchange')
		exchage_link.click()
		exhange_title = driver.find_element_by_class_name('exchange-title')
		exhange_title.is_displayed()
		# find amount from field
		give_btc = driver.find_element_by_id("amount_from-control")
		exchange_btc = float(btc_balance) + int(1)
		give_btc.send_keys(str(exchange_btc))
		# press exchange button
		button = driver.find_element_by_css_selector("button[class ='btn col-xs-12 exchange-submit__btn btn-primary']")
		button.click()
		error_fields = driver.find_elements_by_class_name("md-error")
		driver.save_screenshot('account_dropdown.png')
		# check that 1 error messages are displayed
		self.assertEqual(len(error_fields), 1)




	def test_exchange_same_currency(self):
		driver = self.driver
		exchage_link = driver.find_element_by_link_text('Exchange')
		exchage_link.click()
		exhange_title = driver.find_element_by_class_name('exchange-title')
		exhange_title.is_displayed()
		# grab currency to
		#currency_to = driver.find_element_by_id("md-input-14scx0m8b")
		#currency_to_value = currency_to.text
		#currency_to.click()
		#currency_to_value = driver.

		# find currency from
		currency_from = driver.find_element_by_class_name("md-input md-input md-select-value")
		currency_from.click()
		select_currency_usd = driver.find_element_by_class_name()

		# press exchange button
		button = driver.find_element_by_css_selector("button[class ='btn col-xs-12 exchange-submit__btn btn-primary']")
		button.click()
		error_fields_is_reqiered = driver.find_elements_by_class_name("md-error")
		# check that 2 error messages are displayed
		self.assertEqual(len(error_fields_is_reqiered), 2)


if __name__ == "__main__":
	unittest.main()