import pytest

# Better not to use this / Use when pytest-playwright is not used
@pytest.fixture()
def navigate(self,page):
	page.goto("https://admin-demo.nopcommerce.com/login")
