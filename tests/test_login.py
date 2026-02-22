from pages.login_page import LoginPage
from pages.manufacturer_listing_page import ManufacturerListingPage


def test_login_valid_user(driver, login_logout):
    manufacturer_listing_page = ManufacturerListingPage(driver)
    assert manufacturer_listing_page.is_manufacturer_heading_displayed(), "Manufacturer listing page heading is not displayed!"