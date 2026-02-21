from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CreateNewManufacturer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.create_new_manufacturer_header = (By.XPATH, "//h5[text() = 'Create New Manufacturer']")
        self.name_input = (By.ID, "_r_1t_")
        self.order_input = (By.XPATH, "_r_1u_")
        self.upload_image_button = (By.XPATH, "//span[text() = 'Upload Image']")
        self.cancel_button = (By.XPATH, "//button[text()='Cancel']")


    def is_create_new_manufacturer_heading_displayed(self):
        return self.element_is_displayed(self.create_new_manufacturer_header)

    def clisk_on_cancel_button(self):
        if self.element_is_displayed(self.cancel_button):
            self.click(self.cancel_button)

    def enter_new_manufacturer_name(self, new_manufacturer_name):
        if self.element_is_displayed(self.name_input):
            self.send_keys(self.name_input, new_manufacturer_name)

    # def enter_new_manufacturer_order(self, new_manufacturer_order):
    #     if self.element_is_displayed(self.order_input):
    #         self.send_keys(self.order_input, new_manufacturer_order)

    def click_upload_image_button(self):
        if self.element_is_displayed(self.upload_image_button):
            self.click(self.upload_image_button)

    # def create_new_manufacturer_successfully(self):
