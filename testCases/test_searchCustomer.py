import pytest 
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchPage import SearchCustomers
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class TestSearchCustomer:
	baseURL = ReadConfig.getBaseURL()
	username = ReadConfig.getUsername()
	password = ReadConfig.getPassword()

	# Logger object...
	logger = LogGen.loggen()

	def random_string(self):
		s=8 
		word = ''.join(random.choices(string.ascii_uppercase+string.digits, k=s))
		return word  

	logger.info("******* Starting Search Customer Test *******")
	def search_setup(self,page):
		self.logger.info("***** Login to the System ******")
		page.goto(self.baseURL)

		# self.lp.navigate()
		self.lp = LoginPage(page)
		self.lp.setUsername(self.username)
		self.lp.setPassword(self.password)
		self.lp.clickLogin()
		time.sleep(3)
		# Navigating to Search Page...
		lnkCustomersMenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
		page.locator(lnkCustomersMenu_xpath).click()
		time.sleep(2)
		lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
		page.locator(lnkCustomers_menuitem_xpath).click()
		self.logger.info("***** Search Page *****")


	# Search Customer by Email
	def test_searchCustomerByEmail(self,page):
		self.search_setup(page)
		self.logger.info("******* Starting test_searchCustomerByEmail *******")

		email = "brenda_lindgren@nopCommerce.com"

		self.search_cust = SearchCustomers(page)
		self.search_cust.setSearchEmail(email)
		# fname = "James"
		# lname = "Pan"
		# self.search_cust.setSearchFirstName(fname)
		# self.search_cust.setSearchLastName(lname)
		self.search_cust.clickSearch()
		time.sleep(3)
		status = self.search_cust.searchCustomerByEmail(email)
		print(status)
		assert True == status
		self.logger.info("******** test_searchCustomerByEmail Passed ********")
		'''
		if (status):
			assert True
			self.logger.info("******** test_searchCustomerByEmail Passed ********")
		else:
			assert False 
			self.logger.error("******** test_searchCustomerByEmail Failed ********")
		self.logger.info("******* Completed test_searchCustomerByEmail *******")
		'''

	# Search Customer By Name
	def test_searchCustomerByName(self,page):
		self.search_setup(page)
		self.logger.info("******* Starting test_searchCustomerByName *******")

		name = "James Pan"
		fname = "James"
		lname = "Pan"

		self.search_cust = SearchCustomers(page)
		
		self.search_cust.setSearchFirstName(fname)
		self.search_cust.setSearchLastName(lname)
		self.search_cust.clickSearch()
		time.sleep(3)
		status = self.search_cust.searchCustomerByName(name)
		if (status):
			assert True
			self.logger.info("******** test_searchCustomerByName Passed ********")
		else:
			assert False 
			self.logger.error("******** test_searchCustomerByName Failed ********")
		self.logger.info("******* Completed test_searchCustomerByName *******")


	