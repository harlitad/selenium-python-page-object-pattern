from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage():

    TOAST_LOGIN_SUCCESS = (By.XPATH, "//body/div[3]/div[3]/div[1]/div[1]/div[1]")
    HEADING_PAGE = (By.CSS_SELECTOR, "h1.font-bold.text-3xl")
    TEXT_BODY_DASHBOARD = (By.CSS_SELECTOR, "p.font-medium.text-xl")

    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    @property
    def get_title_toast_login_success(self):
        title_toast = WebDriverWait(self.driver, 30000).until(
            EC.presence_of_element_located(self.TOAST_LOGIN_SUCCESS))
        print("title", title_toast.text)
        return title_toast.text

    def get_heading_page(self):
        text_heading = WebDriverWait(self.driver, 30000).until(
            EC.presence_of_element_located(self.HEADING_PAGE))
        return text_heading.text

    def get_text_body_dashboard(self):
        text_body_dashboard = self.driver.find_element(*self.TEXT_BODY_DASHBOARD)
        return text_body_dashboard.text