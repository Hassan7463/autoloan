from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage


class ManufacturerListingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.all_button = (By.XPATH, "//button[text()='All']")
        self.active_button = (By.XPATH, "//button[text()='All']")
        self.inactive_button = (By.XPATH, "//button[text()='All']")
        self.manufacturer_header = (By.XPATH, "//h5[text() = 'Manufacturers']")
        self.add_new_button =  (By.XPATH, "//button[text() = 'Add New']")

    def is_manufacturer_heading_displayed(self):
        return self.element_is_displayed(self.manufacturer_header)

    def is_add_new_button_displayed(self):
        return self.element_is_displayed(self.add_new_button)

    def is_all_button_displayed(self):
        return self.element_is_displayed(self.all_button)

    def click_add_new_button(self):
        if self.element_is_displayed(self.add_new_button):
            self.click(self.add_new_button)

    def click_active_button(self):
        if self.element_is_displayed(self.active_button):
            self.click(self.active_button)

    def click_inactive_button(self):
        if self.element_is_displayed(self.inactive_button):
            self.click(self.inactive_button)