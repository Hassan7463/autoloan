from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.manufacturers_menu = (By.XPATH, "//a[normalize-space()='Manufacturers']")
        self.cars_menu = (By.XPATH, "//a[normalize-space()='Cars']")
        self.partners_menu = (By.XPATH, "//a[normalize-space()='Partners']")
        self.tracker_menu = (By.XPATH, "//a[normalize-space()='Tracker']")
        self.insurance_menu = (By.XPATH, "//a[normalize-space()='Insurance']")

    def click_manufacturers_menu(self):
        if self.element_is_displayed(self.manufacturers_menu):
            self.click(self.manufacturers_menu)


    def click_cars_menu(self):
        if self.element_is_displayed(self.cars_menu):
            self.click(self.cars_menu)

    def click_partners_menu(self):
        if self.element_is_displayed(self.partners_menu):
            self.click(self.partners_menu)

    def click_tracker_menu(self):
        if self.element_is_displayed(self.tracker_menu):
            self.click(self.tracker_menu)

    def click_insurance_menu(self):
        if self.element_is_displayed(self.insurance_menu):
            self.click(self.insurance_menu)