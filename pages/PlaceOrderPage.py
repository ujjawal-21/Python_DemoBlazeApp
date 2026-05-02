from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from library.Utility import Utility

class PlaceOrderPage:
    cust_name = (By.ID, "name")
    cust_country = (By.ID, "country")
    cust_city = (By.ID, "city")
    cust_card = (By.ID, "card")
    cust_month = (By.ID, "month")
    cust_year = (By.ID, "year")
    purchaseBtn = (By.XPATH, "//button[text()='Purchase']")
    confirmationText = (By.XPATH, "//div[@class='sa-icon sa-custom']//following-sibling::h2")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.ut = Utility(self.driver)
        
    def set_cust_name(self, cname):
        self.ut.checkElementVisibility(self.cust_name)
        self.driver.find_element(*self.cust_name).send_keys(cname)
        
    def set_cust_country(self, country):
        self.ut.checkElementVisibility(self.cust_country)
        self.driver.find_element(*self.cust_country).send_keys(country)
        
    def set_cust_city(self, city):
        self.ut.checkElementVisibility(self.cust_city)
        self.driver.find_element(*self.cust_city).send_keys(city)
        
    def set_cust_card(self, card):
        self.ut.checkElementVisibility(self.cust_card)
        self.driver.find_element(*self.cust_card).send_keys(card)
        
    def set_cust_month(self, month):
        self.ut.checkElementVisibility(self.cust_month)
        self.driver.find_element(*self.cust_month).send_keys(month)
        
    def set_cust_year(self, year):
        self.ut.checkElementVisibility(self.cust_year)
        self.driver.find_element(*self.cust_year).send_keys(year)
        
    def click_purchase(self):
        btn = self.driver.find_element(*self.purchaseBtn)
        self.ut.clickEvent(btn)
        
    def getConfirmation(self):
        self.ut.checkElementVisibility(self.confirmationText)
        return self.driver.find_element(*self.confirmationText).text