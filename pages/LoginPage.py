from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from library.Utility import Utility

class LoginPage:
    
    username = (By.ID, "loginusername")
    password = (By.ID, "loginpassword")
    loginBtn = (By.XPATH, "//button[text()='Log in']")
    
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.ut = Utility(self.driver)
        
    def login(self, uname, passwd):
        self.ut.checkElementVisibility(self.username)
        self.driver.find_element(*self.username).send_keys(uname)
        self.ut.checkElementVisibility(self.password)
        self.driver.find_element(*self.password).send_keys(passwd)
        self.driver.find_element(*self.loginBtn).click()