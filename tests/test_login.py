from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin():
    def test_valid_login(self, browser: webdriver.Remote):
        dashboard_page = DashboardPage(browser)
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("admin@admin.com")
        login_page.click_next_button()
        login_page.set_password("admin10")
        login_page.click_signin_button()

        assert dashboard_page.get_heading_page() == "Dashboard Explore"

    def test_unauthorized_email(self, browser: webdriver.Remote):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email("admin@admin.mail")
        login_page.click_next_button()
        assert login_page.get_title_unauthorized_card() == "Not Authorized"
