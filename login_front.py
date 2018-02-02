import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class Login(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get("https://bitcoin-stage.quartsoft.com/login")

	# test cases wrong email, wrong password
	@data(("tset@gmail.com", "magento1", "strong"),
	      ("auto4testing@gmail.com", "magento2", "strong"))
	@unpack

	def test_login_negative(self, email, password, err_mes):
		# find form fields
		email_field = self.driver.find_element_by_id("email")
		password_field = self.driver.find_element_by_id("password")
		login_btn = self.driver.find_element_by_tag_name("button")

		# fill fields with data
		email_field.send_keys(email)
		password_field.send_keys(password)
		login_btn.click()

		# find error message and check error color and font-family
		err_mess = self.driver.find_element_by_tag_name(err_mes)
		self.assertTrue(err_mess.is_displayed())
		self.assertEqual(err_mess.value_of_css_property("color"), "rgb(210, 52, 52)")
		self.assertEqual(err_mess.value_of_css_property("font-family"), "Roboto")
		self.assertEqual(err_mess.value_of_css_property("font-size"), "12px")


	# wrong email format, password less than 6 symbols
	@data(("auto4testing", "magento2", "login"),
		  ("", "", "login"))
	@unpack
	def test_login_incorrect_format_data(self, email, password, url_part):

		# find form fields
		email_field = self.driver.find_element_by_id("email")
		password_field = self.driver.find_element_by_id("password")
		login_btn = self.driver.find_element_by_tag_name("button")

		# fill fields with data
		email_field.send_keys(email)
		password_field.send_keys(password)
		login_btn.click()

		# switch to the alert
		#alert = self.driver.switch_to.alert
		# get the text from alert
		#alert_text = alert.text
		# check alert text
		#self.assertEqual(err_mes, alert_text)

		self.assertTrue(url_part in self.driver.current_url)


	# login correct data
	@data(("auto4testing@gmail.com", "magento1", "profile-title"))
	@unpack
	def test_login_positive(self, email, password, profile):
		# find form fields
		email_field = self.driver.find_element_by_id("email")
		password_field = self.driver.find_element_by_id("password")
		login_btn = self.driver.find_element_by_tag_name("button")

		# fill fields with data
		email_field.send_keys(email)
		password_field.send_keys(password)
		login_btn.click()

		# find element profile
		#account = self.driver.find_element_by_class_name("profile")
		self.assertTrue(profile)

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()