from pages.login_page import LoginPage
from pages.manufacturer_listing_page import ManufacturerListingPage


def test_login_valid_user(driver, base_url, credentials, login_login):
    # login_page = LoginPage(driver)
    manufacturer_listing_page = ManufacturerListingPage(driver)
    # login_page.open(base_url)
    # login_page.login(credentials["username"], credentials["password"])
    assert manufacturer_listing_page.is_manufacturer_heading_displayed(), "Manufacturer listing page heading is not displayed!"