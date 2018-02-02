import unittest
from ddt import ddt, unpack, data
from selenium import webdriver
import MySQLdb

conn = MySQLdb.connect('localhost', '', '', 'tour')
cursor = conn.cursor()

@ddt
class UserProfile(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.get("https://bitcoin-stage.quartsoft.com/")

	@data(("auto4testing+1@gmail.com", "magento1"))
	@unpack
	def test_login(self, email, password):
		driver = self.driver
		driver.get("https://bitcoin-stage.quartsoft.com/login")
		# find form fields
		email_field = driver.find_element_by_id("email")
		password_field = driver.find_element_by_id("password")
		login_btn = driver.find_element_by_tag_name("button")
		# fill fields with data
		email_field.send_keys(email)
		password_field.send_keys(password)
		login_btn.click()
		account = driver.find_element_by_class_name("profile-title")
		self.assertTrue(account)

	def test_field_validation(self):
		driver = self.driver
		# entity
		name_field = driver.find_element_by_tag_name()
		name_title = driver.find_element_by_tag_name()


if __name__ == "__main__":
	unittest.main()