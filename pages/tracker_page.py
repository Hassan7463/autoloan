from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TrackerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.trackers_heading = (By.XPATH, "//h5[text()='Trackers']")

    def is_tracker_page_heading_displayed(self):
        return self.element_is_displayed(self.trackers_heading)