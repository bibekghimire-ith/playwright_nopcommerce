import time

class AddCustomer:
	# Locators...
	# lnk_customerMenu_xpath = ".nav.nav-pills > li:nth-child(4) > a > p"
	lnk_customerMenu_xpath = ".nav-link.active > p > .right"
	lnk_customer_xpath = ".nav-item.has-treeview.menu-open > .nav > li > .nav-link >> nth=0" # li.has-treeview:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)
	# lnk_customer_xpath = ".nav-item.has-treeview.menu-open > .nav > li > .nav-link > p >> nth=0" 
	# (path).first.click()

	btn_addNew_txt = "text=Add new"

	txt_Email_id = "#Email"
	txt_password_id = "#Password"
	txt_firstname_id = "#FirstName"
	txt_lastname_id = "#LastName"

	radio_genderMale_id = "#Gender_Male"
	radio_genderFemale_id = "#Gender_Female"

	txt_dob_id = "input#DateOfBirth"
	txt_company_id = "input#Company"

	check_isTaxExempt_id = "#IsTaxExempt"

	select_newsletter_xpath = "text=Newsletter Your store nameTest store 2 >> div[role=\"listbox\"]"
	select_option1_xpath = "li[role=\"option\"]:has-text(\"Your store name\")"
	select_option2_xpath = "li[role=\"option\"]:has-text(\"Test store 2\")"

	role_path = "input.k-input.k-readonly"
	# role_path = "//div[@class='k-multiselect-wrap k-floatwrap']"
	role_registered_xpath = "div[role=\"listbox\"]:has-text(\"Registered\")"
	role_administrator_xpath = "li[role=\"option\"]:has-text(\"Administrators\")"
	role_guest_xpath = "li[role=\"option\"]:has-text(\"Guests\")"
	role_moderators_xpath = "li[role=\"option\"]:has-text(\"Forum Moderators\")"
	remove_registered_xpath = "text=RegisteredAdministratorsForum ModeratorsGuestsRegisteredVendors >> [aria-label=\"delete\"]"
	role_vendors_link = "li[role=\"option\"]:has-text(\"Vendors\")"

	# select_vendor_xpath = "li[role=\"option\"]:has-text(\"Vendors\")"

	check_active_id = "#Active"

	# Select 1
    # page.wait_for_selector("select[name=\"VendorId\"]").select_option("1")
    # Select 2
    # page.wait_for_selector("select[name=\"VendorId\"]").select_option("2")

	txt_comment_xpath = "textarea[name=\"AdminComment\"]"

	def __init__(self,page):
		self.page = page

	def navigate_to_AddCustomers(self):
		# self.page.wait_for_selector("a.nav-link.active").click()
		# print("*"*40)
		# self.page.wait_for_selector(".nav-item.has-treeview.menu-open > .nav > li > .nav-link > p").first.click()
		# self.page.wait_for_selector(self.lnk_customerMenu_xpath).click()
		# print("***************************************************")
		# self.page.wait_for_selector(self.lnk_customer_xpath).first.click()
		# self.page.wait_for_selector(self.lnk_customer_xpath).click()
		self.page.goto('https://admin-demo.nopcommerce.com/Admin/Customer/List')
		time.sleep(5)
		self.page.wait_for_selector(self.btn_addNew_txt).click()

	def setEmail(self,email):
		self.page.wait_for_selector(self.txt_Email_id).fill(email)

	def setPassword(self,password):
		self.page.fill(self.txt_password_id, password)

	def setFirstname(self, fname):
		self.page.wait_for_selector(self.txt_firstname_id).fill(fname)

	def setLastname(self,lname):
		self.page.wait_for_selector(self.txt_lastname_id).fill(lname)

	# Set Gender...
	def setGender(self,gender):
		if gender == "Male":
			self.page.wait_for_selector(self.radio_genderMale_id).check()
		elif gender == "Female":
			self.page.wait_for_selector(self.radio_genderFemale_id).click()
		else:
			self.page.wait_for_selector(self.radio_genderMale_id).check()

		

	def setDOB(self,dob): # Format: 7/6/2022
		self.page.wait_for_selector(self.txt_dob_id).fill(dob)

	def setCompany(self,company):
		self.page.wait_for_selector(self.txt_company_id).fill(company)

	def setTaxExempt(self):
		self.page.wait_for_selector(self.check_isTaxExempt_id).check()

	def setNewsletter1(self):
		self.page.wait_for_selector(self.select_newsletter_xpath).click()
		time.sleep(1)
		self.page.wait_for_selector(self.select_option1_xpath).click()

	def setNewsletter2(self):
		self.page.wait_for_selector(self.select_newsletter_xpath).click()
		time.sleep(1)
		self.page.wait_for_selector(self.select_option2_xpath).click()

	

	def selectVendor(self,option):
		self.page.wait_for_selector("select[name=\"VendorId\"]").click()
		# self.page.wait_for_selector("select[name=\"VendorId\"]").select_option("1")
		self.page.wait_for_selector("select[name=\"VendorId\"]").select_option(option)

	def disableActive(self):
		self.page.wait_for_selector(self.check_active_id).click()
		# self.page.wait_for_selector(self.check_active_id).check()

	def addAdminComment(self,comment):
		self.page.wait_for_selector(self.txt_comment_xpath).fill(comment)


	def setRoleRegistered(self):
		self.page.wait_for_selector(self.remove_registered_xpath).click()
		self.page.wait_for_selector(self.role_path).click()
		self.page.wait_for_selector(self.role_registered_xpath).click()

	def setRoleAdministrator(self):
		# self.page.wait_for_selector(self.remove_registered_xpath).click()
		self.page.wait_for_selector("input.k-input[aria-labelledby=\"SelectedCustomerRoleIds_label\"]").click()
		self.page.wait_for_selector(self.role_administrator_xpath).click()

	def setRoleModerator(self):
		# self.page.wait_for_selector(self.remove_registered_xpath).click()
		self.page.wait_for_selector("input.k-input[aria-labelledby=\"SelectedCustomerRoleIds_label\"]").click()
		self.page.wait_for_selector(self.role_moderators_xpath).click()

	def setRoleVendor(self):
		# self.page.wait_for_selector(self.remove_registered_xpath).click()
		self.page.wait_for_selector("input.k-input[aria-labelledby=\"SelectedCustomerRoleIds_label\"]").click()
		time.sleep(2)
		self.page.wait_for_selector(self.role_vendors_link).click()

	def setRoleGuest(self):
		self.page.wait_for_selector(self.remove_registered_xpath).click()
		self.page.wait_for_selector(self.role_path).click()
		self.page.wait_for_selector(self.role_guest_xpath).click()

	# Remove Registered
	def removeRegistered(self):
		self.page.wait_for_selector(self.remove_registered_xpath).click()
"""
	# Set Customer Role...
	def setCustomerRole(self,role):
		# self.page.wait_for_selector(self.role_path).click()
		# self.page.wait_for_selector(self.remove_registered_xpath).click()
		# time.sleep(3)
		self.page.wait_for_selector(self.role_path).click()
		time.sleep(2)

		if role == "Registered":
			pass
			# self.listitem = self.page.wait_for_selector(self.role_registered_xpath).click()
		elif role == "Administrators":
			self.listitem = self.page.wait_for_selector(self.role_administrator_xpath).click()
		elif role == "Guests":
			# Remove Registered first...
			self.page.wait_for_selector(self.remove_registered_xpath).click()
			self.page.wait_for_selector(self.role_path).click()
			time.sleep(2)
			self.listitem = self.page.wait_for_selector(self.role_guest_xpath).click()
		elif role == "Vendors":
			self.listitem = self.page.wait_for_selector(self.role_vendors_link).click()
		else: 
			# Set default role as Guests
			# self.page.wait_for_selector(self.remove_registered_xpath).click()
			# self.page.wait_for_selector(self.role_path).click()
			# time.sleep(2)
			self.listitem = self.page.wait_for_selector(self.role_guest_xpath).click()		
		# time.sleep(3)
		# self.listitem.click()
		# self.page.evaluate("arguments[0].click();", self.listitem)
"""

	


'''
	lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
	lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
	btnAddnew_xpath = "//a[@class='btn bg-blue']"
	txtEmail_xpath = "//input[@id='Email']"
	txtPassword_xpath = "//input[@id='Password']"
	txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
	lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
	lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
	lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
	lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
	drpmgrOfVendor_xpath = "//*[@id='VendorId']"
	rdMaleGender_id = "Gender_Male"
	rdFeMaleGender_id = "Gender_Female"
	txtFirstName_xpath = "//input[@id='FirstName']"
	txtLastName_xpath = "//input[@id='LastName']"
	txtDob_xpath = "//input[@id='DateOfBirth']"
	txtCompanyName_xpath = "//input[@id='Company']"
	txtAdminContent_xpath = "//textarea[@id='AdminComment']"
	btnSave_xpath = "//button[@name='save']"'''