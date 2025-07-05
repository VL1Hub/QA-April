from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # Locators (solo los necesarios)
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def load(self):
        self.driver.get(self.url)

    def enter_credentials(self, username, password):
        self.find(*self.USERNAME_INPUT).send_keys(username)
        self.find(*self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.find(*self.LOGIN_BUTTON).click()