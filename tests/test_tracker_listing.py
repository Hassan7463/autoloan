from pages.tracker_page import TrackerPage
from pages.menus_page import MenuPage

def test_tracker_page_heading_is_displayed(driver, login_logout):
    menu = MenuPage(driver)
    tracker_page = TrackerPage(driver)
    menu.click_tracker_menu()
    assert tracker_page.is_tracker_page_heading_displayed(), "Tracker listing page heading is not displayed"