from pages.create_new_manufacturer_page import CreateNewManufacturer
from pages.login_page import LoginPage
from pages.manufacturer_listing_page import ManufacturerListingPage


def test_create_new_manufacturer_heading_displayed(driver, base_url,credentials):
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(credentials["username"], credentials["password"])
    manufacturer_listing_page = ManufacturerListingPage(driver)
    manufacturer_listing_page.click_add_new_button()
    create_new_manufacturer_page = CreateNewManufacturer(driver)
    assert create_new_manufacturer_page.is_create_new_manufacturer_heading_displayed(), "Create New Manufacturer heading is not displayed!"

def test_cancel_button_functionality(driver, base_url, credentials):
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(credentials["username"], credentials["password"])
    manufacturer_listing_page = ManufacturerListingPage(driver)
    manufacturer_listing_page.click_add_new_button()
    create_new_manufacturer_page = CreateNewManufacturer(driver)
    create_new_manufacturer_page.clisk_on_cancel_button()
    assert manufacturer_listing_page.is_manufacturer_heading_displayed(), "Manufacturer listing page heading is not displayed!"