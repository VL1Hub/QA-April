from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    VERIFY_PRODUCT = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    BACK_BTN = (By.ID, "continue-shopping")

    def verify_product_in_cart(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.VERIFY_PRODUCT)
        ).text

    def remove_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BTN)
        ).click()

    def go_back_to_products(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACK_BTN)
        ).click()