import pytest 
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class TestAddCustomer:
	baseURL = ReadConfig.getBaseURL()
	username = ReadConfig.getUsername()
	password = ReadConfig.getPassword()

	# Logger object...
	logger = LogGen.loggen()

	def random_string(self):
		s=8 
		word = ''.join(random.choices(string.ascii_uppercase+string.digits, k=s))
		return word  


	def test_addCustomer(self,page):
		self.logger.info("******* Verifing test_addCustomer Test *******")
		self.logger.info("***** Login to the System ******")
		page.goto(self.baseURL)

		# self.lp.navigate()
		self.lp = LoginPage(page)
		self.lp.setUsername(self.username)
		self.lp.setPassword(self.password)
		self.lp.clickLogin()
		act_title = page.locator('title').inner_text()
		# time.sleep(2)
		if act_title == "Dashboard / nopCommerce administration":
			print(act_title)
			self.logger.info("******* Successful Login *******")

			# Add Customer goes here...
			self.customer = AddCustomer(page)
			self.customer.navigate_to_AddCustomers()
			
			time.sleep(3)
			# Customer Information...
			email = self.random_string() + "@gmail.com"
			self.customer.setEmail(email)
			self.customer.setPassword('password123')
			self.customer.setFirstname('john')
			self.customer.setLastname('doe')
			self.customer.setGender("Male")
			dob = "7/6/2022"
			self.customer.setDOB(dob)
			self.customer.setCompany("MyCompany")
			self.customer.setTaxExempt()
			self.customer.setNewsletter2()
			time.sleep(2)
			# self.customer.setCustomerRole("Vendors")
			self.customer.setRoleVendor()
			# Select Vendor if only Customer role is set to Vendor
			self.customer.selectVendor('2')
			self.customer.disableActive()
			self.customer.addAdminComment("Added comment...")
			page.click("button[name=\"save\"]")

			time.sleep(5)
			# Validation...
			msg = page.locator("div.alert.alert-success").inner_text()
			print(msg)
			if "The new customer has been added successfully." in msg:
				self.logger.info("***** Customer Added Successfully *****")
				assert True 
				self.logger.info("******** Test Passed ********")
			else:		
				self.logger.info(msg)		
				self.logger.error("******** Test Failed ********")
				assert False
			
			
			
		else:
			print(act_title)
			# Takes screenshot if test fails..
			page.screenshot(path="./Screenshots/test_login.png", full_page=True)
			self.logger.error("******* Login Failed ********")
			assert False
		# page.wait_for_selector("xpath=//a[@clas='nav-link'][@href='/Admin/Customer/List']").click()
		# time.sleep(5)

		

