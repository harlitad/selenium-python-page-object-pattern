from pages.dashboard_page import DashboardPage
from tests.test_login import TestLogin

class TestDashboard:
    def test_text_dashboard(self, browser):
        login = TestLogin()
        login.test_valid_login(browser)
        dashboard_page = DashboardPage(browser)

        assert dashboard_page.get_heading_page() == "Dashboard Explore"
        assert dashboard_page.get_text_body_dashboard() == "Start creating your amazing application!"

        browser.implicitly_wait(10)