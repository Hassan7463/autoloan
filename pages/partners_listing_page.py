from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PartnersListingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.partners_heading = (By.XPATH, "//h5[text()='Partners']")

    def is_partners_page_heading_displayed(self):
        return self.element_is_displayed(self.partners_heading)