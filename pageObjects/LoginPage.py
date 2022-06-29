class LoginPage:

	# Locators...
	textbox_username_id = "#Email"
	textbox_password_id = "#Password"
	button_login_xpath = "xpath=/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
	link_logout_linktext = "text=Logout"
	link_logout_xpath = "xpath=/html/body/div[3]/nav/div/ul/li[3]/a"
	button_login = "text=Log In"

	def __init__(self,page):
		self.page = page

	@property
	def username_field(self):
		return self.page.wait_for_selector(self.textbox_username_id)

	def setUsername(self,username):
		# self.username_field.fill(username)
		self.page.locator(self.textbox_username_id).fill(username)

	def setPassword(self,password):
		# self.page.fill(self.textbox_password_id, password)
		self.page.locator(self.textbox_password_id).fill(password)

	def clickLogin(self):
		self.page.click(self.button_login_xpath)
		# self.page.locator(self.button_login).click()

	def clickLogout(self):
		self.page.click(self.link_logout_xpath)

	def navigate(self):
		self.page.goto("https://admin-demo.nopcommerce.com/login")
		

