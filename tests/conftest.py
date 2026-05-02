import pytest
from library.Driver_Factory import DriverFactory
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def setup():
    driver = DriverFactory.getDriver()
    yield driver
    driver.quit()
    
@pytest.fixture
def setup_with_Logged_in():
    driver = DriverFactory.getDriver()   
    hp = HomePage(driver)
    hp.click_login()
    lp = LoginPage(driver)
    lp.login("ujjawal", "admin")
    yield driver
    driver.close()

@pytest.fixture 
def config():
    return{
            "username": os.getenv("APP_USERNAME"),
            "password": os.getenv("APP_PASSWORD")
        }