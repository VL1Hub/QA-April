from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    SAUCE_LABS_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ICON = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    TEXT_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SAUCE_LABS_BACKPACK)
        ).click()

    def get_cart_badge_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ICON)
        ).text

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

    def get_button_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TEXT_BUTTON)
        ).text