from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver    # self helps tp define and use the class level variable
        self.username_input = (By.XPATH, "//input[@id='_r_0_']")
        self.password_input = (By.XPATH, "//input[@id='_r_1_']")
        self.signin_button = (By.XPATH, "//button[text()='Sign in']")

    def open(self, base_url):
        self.driver.get(base_url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()