from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from library.Utility import Utility
import re

class ProductDetailPage:
    productName = (By.TAG_NAME, "h2")
    price = (By.XPATH, "//h3")
    AddtoCartBtn = (By.XPATH, "//a[text()='Add to cart']")
    
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.ut = Utility(self.driver)
    
    def getProductName(self):
        self.ut.checkElementVisibility(self.productName)
        product = self.driver.find_element(*self.productName)
        return product.text
    
    def getPrice(self):
        self.ut.checkElementVisibility(self.price)
        raw_price = self.driver.find_element(*self.price).text
        priceWithspecialChars = re.sub("[a-zA-Z\s]", "", raw_price)
        price = re.sub("[^0-9]", "", priceWithspecialChars)
        return price
        
    def addProductToCart(self):
        cartBtn = self.driver.find_element(*self.AddtoCartBtn)
        self.ut.clickEvent(cartBtn)