from pages.login_page import LoginPage
from pages.manufacturer_listing_page import ManufacturerListingPage


def test_all_button_displayed(driver, login_logout):
    manufacturer_listing_page = ManufacturerListingPage(driver)
    manufacturer_listing_page.click_active_button()
    manufacturer_listing_page.click_active_button()
    assert manufacturer_listing_page.is_all_button_displayed(), "All button is not displayed!"