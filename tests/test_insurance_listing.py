from pages.insurance_page import InsurancePage
from pages.menus_page import MenuPage

def test_insurance_listing_page_heading_displayed(driver, login_logout):
    menu = MenuPage(driver)
    insurance_page = InsurancePage(driver)
    menu.click_insurance_menu()
    assert insurance_page.is_insurance_page_heading_displayed(), "Insurance listing page heading is not displayed!"