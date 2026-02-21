from dataclasses import asdict

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver    # self helps tp define and use the class level variable
        self.username_input = (By.XPATH, "//input[@id='_r_0_']")
        self.password_input = (By.XPATH, "//input[@id='_r_1_']")
        self.signin_button = (By.XPATH, "//button[text()='Sign in']")

    def open(self, base_url):
        self.driver.get(base_url)

    def enter_username(self, username):
        self.send_keys(self.username_input, username)

    def enter_password(self, password):
        self.send_keys(self.password_input, password)

    def click_login(self):
        self.click(self.signin_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()