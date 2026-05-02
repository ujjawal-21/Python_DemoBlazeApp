from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from library.JSON_reader import JsonReader

class DriverFactory:
    
    
    @staticmethod
    def getDriver():
        json_data = JsonReader.getJsonData()
        options = Options()
        prefs = {
            "credentials_enable_service" : False,
            "profile.password_manager_enabled" : False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-notifications")
        driver: WebDriver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(json_data["app"]["url"])
        driver.implicitly_wait(30)
        return driver