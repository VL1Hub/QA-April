from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductsPage(BasePage):
    # Solo el locator que necesitamos
    TITLE = (By.CLASS_NAME, "title")

    def is_title_displayed(self, expected_text):
        return expected_text in self.find(*self.TITLE).text