import pytest 
from pageObjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestLogin:
	baseURL = ReadConfig.getBaseURL()
	username = ReadConfig.getUsername()
	password = ReadConfig.getPassword()

	# Do not use __init__() with pytest
	'''
	def __init__(self,page):
		self.page = page
	'''

	# Logger object...
	logger = LogGen.loggen()

	# Test for homepage
	def test_homePageTitle(self,page):
		self.logger.info("******* TestLogin *******")
		self.logger.info("******* Verifing Homepage Title *******")

		page.goto(self.baseURL)
		act_title = page.locator('title').inner_text()
		if act_title == "Your store. Login12":
			self.logger.info("******* Homepage Title test is passed *******")
			assert True 
		else:
			self.logger.error("******* Homepage Title test is failed ********")
			page.screenshot(path="./Screenshots/test_homePageTitle.png", full_page=True)
			assert False

	# Test for valid login
	def test_login(self,page):
		self.logger.info("******* Verifing Login Test *******")
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
			self.logger.info("******* Login test is passed *******")
			assert True 
		else:
			print(act_title)
			# Takes screenshot if test fails..
			page.screenshot(path="./Screenshots/test_login.png", full_page=True)
			self.logger.error("******* Login test is failed ********")
			assert False
		# page.wait_for_selector("xpath=//a[@clas='nav-link'][@href='/Admin/Customer/List']").click()
		# time.sleep(5)

		