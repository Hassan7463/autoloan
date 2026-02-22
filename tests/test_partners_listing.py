from pages.partners_listing_page import PartnersListingPage
from pages.menus_page import MenuPage

def test_partners_page_heading_displayed(driver, login_logout):
    menus = MenuPage(driver)
    partners_listing_page = PartnersListingPage(driver)
    menus.click_partners_menu()
    assert partners_listing_page.is_partners_page_heading_displayed(), "Partners listing page is not displayed!"