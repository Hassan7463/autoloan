import pytest
from selenium import webdriver
from dotenv import load_dotenv    # to load environment variables in this current file
import os                         # to read the environment file

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