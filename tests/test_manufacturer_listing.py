from pages.login_page import LoginPage
from pages.manufacturer_listing_page import ManufacturerListingPage


def test_all_button_displayed(driver, base_url, credentials):
    login_page = LoginPage(driver)
    manufacturer_listing_page = ManufacturerListingPage(driver)
    login_page.open(base_url)
    login_page.login(credentials["username"], credentials["password"])
    manufacturer_listing_page.click_active_button()
    manufacturer_listing_page.click_active_button()
    assert manufacturer_listing_page.is_all_button_displayed(), "All button is not displayed!"