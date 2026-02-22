from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.tracker_page import TrackerPage


class InsurancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.insurance_heading = (By.XPATH, "//h5[text()='Insurance']")

    def is_insurance_page_heading_displayed(self):
        return self.element_is_displayed(self.insurance_heading)