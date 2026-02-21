from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LogoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.user_dropdown = (By.XPATH, "//img[contains(@src,'ui-avatars.com')]")
        self.logout_link = (By.XPATH, "//li[normalize-space()='Sign Out']")

    def open_user_dropdown(self):
        self.click(self.user_dropdown)

    def click_sign_out(self):
        self.click(self.logout_link)

    def logout(self):
        self.open_user_dropdown()
        self.click_sign_out()