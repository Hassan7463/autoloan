from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait_timeout = 10

    def click(self, locator):
        element = WebDriverWait(self.driver, self.wait_timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        element = WebDriverWait(self.driver, self.wait_timeout).until(EC.element_to_be_clickable(locator))
        element.send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, self.wait_timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def element_is_displayed(self, locator):
        try:
            return WebDriverWait(self.driver, self.wait_timeout).until(EC.visibility_of_element_located(locator))

        except TimeoutException:
            return False

    def element_is_enabled(self, locator):
        try:
            return WebDriverWait(self.driver, self.wait_timeout).until(EC.visibility_of_element_located(locator))

        except TimeoutException:
            return False

    def element_is_selected(self, locator):
        try:
            return WebDriverWait(self.driver, self.wait_timeout).until(EC.visibility_of_element_located(locator))

        except TimeoutException:
            return False

    def navigate_to(self, url):
        self.driver.get(url)