import pytest 
from pageObjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

# from playwright.async_api import async_playwright
# import asyncio


class Test_DDT_Login:
	baseURL = ReadConfig.getBaseURL()
	path = "./TestData/LoginData.xlsx"

	# Logger object...
	logger = LogGen.loggen()

	status = []
	# Test for valid login
	# @pytest.mark.asyncio
	def test_login(self,page):
		self.logger.info("********* Test_DDT_Login *******")
		self.logger.info("******* Verifing Login Test *******")
		page.goto(self.baseURL)
		# self.lp.navigate()
		self.lp = LoginPage(page)

		self.rows = ExcelUtils.getRowCount(self.path,'Sheet1')

		
		for row in range(2, self.rows+1):
			self.username = ExcelUtils.readData(self.path,'Sheet1',row,1)
			self.password = ExcelUtils.readData(self.path,'Sheet1',row,2)
			self.exp = ExcelUtils.readData(self.path,'Sheet1',row,3)

			self.lp.setUsername(self.username)
			self.lp.setPassword(self.password)
			self.lp.clickLogin()			

			print(self.username,self.password)

			act_title = page.locator('title').inner_text()
			exp_title = "Dashboard / nopCommerce administration"

			if act_title == exp_title: # Successful Login
				if self.exp == "Pass": # Expected output Pass
					self.logger.info('****** Test Passed ******')
					self.lp.clickLogout()
					self.status.append('Pass')
				elif self.exp == "Fail":	# Doesnot match with expected output
					self.logger.info('****** Test Failed ******')
					self.lp.clickLogout()
					self.status.append('Fail')
			elif act_title != exp_title: # Failed Login
				if self.exp == "Pass": 
					self.logger.info('****** Test Failed ******')
					# self.lp.clickLogout()
					self.status.append('Fail')
					page.reload()
					# self.lp.navigate()
				elif self.exp == "Fail":	
					self.logger.info('****** Test Passed ******')
					# self.lp.clickLogout()
					self.status.append('Pass')
					# self.lp.navigate()
					page.reload()

		if "Fail" not in self.status:
			self.logger.info("******* Test_DDT_Login is passed ********")
			assert True 
		else:
			self.logger.info("******* Test_DDT_Login is failed ********")
			assert False 

		self.logger.info("******* End of Test_DDT_Login ********")

		
		