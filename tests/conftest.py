import pytest
from library.Driver_Factory import DriverFactory
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from dotenv import load_dotenv
import os
import pytest_html
import datetime

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
    
#--------Screenshot --------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")

        if driver:
            # Get test name
            test_name = item.name

            # Generate timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Create screenshots folder
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # Final file name
            file_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            # Save screenshot
            driver.save_screenshot(file_path)
            
            # Attach to pytest-html report
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(file_path))
            report.extra = extra

            print(f"Screenshot saved at: {file_path}")
    
    
# ---- HTML Report -----

def pytest_html_report_title(report):
    report.title = "Demo Blaze App Test Report"
    
def pytest_configure(config):
    config._metadata = {
        "Project Name": "Demo Blaze",
        "Tester": "Ujjawal",
        "Browser": "Chrome",
        "Environment": "QA"
    }