from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    # locator
    EMAIL = (By.ID, "ui-sign-in-email-input")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".firebaseui-id-submit")
    PASSWORD = (By.ID, "ui-sign-in-password-input")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, ".firebaseui-id-submit.firebaseui-button.mdl-button.mdl-js-button.mdl-button--raised.mdl-button--colored")
    UNAUTHORIZED_CARD_TITLE = (By.CSS_SELECTOR, ".firebaseui-id-page-unauthorized-user h1.firebaseui-title")

    # method constructor
    def __init__(self, browser: webdriver.Remote):
        self.driver = browser

    def load(self):
        self.driver.get("https://staging-partner-explore.misterb2b.com/login")

    def set_email(self, email):
        email_field = self.driver.find_element(*self.EMAIL)
        email_field.send_keys(email)

    def click_next_button(self):
        next_button = self.driver.find_element(*self.NEXT_BUTTON)
        next_button.click()

    def set_password(self, password):
        # password_field = self.driver.find_element(*self.PASSWORD)
        password_field = WebDriverWait(self.driver, 3000).until(EC.presence_of_element_located(self.PASSWORD))
        password_field.send_keys(password)

    def click_signin_button(self):
        signin_button = self.driver.find_element(*self.SIGNIN_BUTTON)
        signin_button.click()

    def get_title_unauthorized_card(self):
        card = self.driver.find_element(*self.UNAUTHORIZED_CARD_TITLE)
        return card.text
        