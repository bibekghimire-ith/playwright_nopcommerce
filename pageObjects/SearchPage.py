class SearchCustomers:
	# locators...
	txtSearchEmail_id = "#SearchEmail"
	txtFirstName_id = "#SearchFirstName"
	txtLastName_id = "#SearchLastName"

	btnSearch_id = "#search-customers"

	tblSearchList_xpath ="//table[@id='customers-grid']/tbody"
	tblSearchRow_xpath = "//table[@id='customers-grid']/tbody/tr"
	tblSearchColumn_xpath = "//table[@id='customers-grid']/tbody/tr/td"

	def __init__(self, page):
		self.page = page 

	def setSearchEmail(self,email):
		# self.page.locator(self.txtSearchEmail_id).clear()
		self.page.locator(self.txtSearchEmail_id).fill(email)

	def setSearchFirstName(self,fname):
		# self.page.locator(self.txtFirstName_id).clear()
		self.page.locator(self.txtFirstName_id).fill(fname)

	def setSearchLastName(self,lname):
		# self.page.locator(self.txtLastName_id).clear()
		self.page.locator(self.txtLastName_id).fill(lname)

	def clickSearch(self):
		self.page.locator(self.btnSearch_id).click()

	def getNoOfRows(self):
		# return len(self.page.locator(self.tblSearchRow_xpath))
		# len() method does not works with locator
		return self.page.locator(self.tblSearchRow_xpath).count()


	def getNoOfColumns(self):
		return self.page.locator(self.tblSearchColumn_xpath).count()

	def searchCustomerByEmail(self,email):
		# table = self.page.wait_for_selector(self.tblSearchList_xpath)
		self.flag = False
		emailid = ''
		for i in range(1,self.getNoOfRows()+1):
			table = self.page.wait_for_selector(self.tblSearchList_xpath)
			# table = self.page.locator(tblSearchList_xpath)
			emailid = self.page.locator("//table[@id='customers-grid']/tbody/tr['+str(i)+']/td[2]").inner_text()
			print(emailid)
			if email in emailid:
				self.flag = True
				break 
		return self.flag

	def searchCustomerByName(self,name):
		# table = self.page.wait_for_selector(self.tblSearchList_xpath)
		flag = False
		for i in range(1,self.getNoOfRows()+1):
			table = self.page.locator(self.tblSearchList_xpath)
			# cust_name = table.locator("//table[@id='customers-grid']/tbody/tr['+str(i)+']/td[3]").inner_text()
			cust_name = table.locator("//tr['+str(i)+']/td[3]").inner_text()
			print(cust_name)
			if name in cust_name:
				flag = True
				break 
		return flag 


	

