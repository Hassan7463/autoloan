import pytest
from selenium import webdriver
from dotenv import load_dotenv    # to load environment variables in this current file
import os                         # to read the environment file

from pages import login_page
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

load_dotenv()

@pytest.fixture       # fixture is use to change the scope and the reuse it again and again
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver        # use to tear down the
    driver.quit()

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture
def credentials():
    return {
        "username": os.getenv("APP_USERNAME"),
        "password": os.getenv("APP_PASSWORD")
    }

@pytest.fixture
def login_logout(driver, base_url, credentials):
    signin_page = LoginPage(driver)
    logout_page = LogoutPage(driver)

    # Login
    signin_page.open(base_url)
    signin_page.login(credentials["username"], credentials["password"])

    # Allow test to run while logged in
    yield login_page

    # logout (runs after test complete)
    try:
        logout_page.logout()
    except Exception:
        pass