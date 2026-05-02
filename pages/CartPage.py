from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from library.Utility import Utility

class CartPage:
    deleteBtns = (By.XPATH, "//tbody[@id='tbodyid']//tr//child::td//child::a")
    addedProduct = (By.XPATH, "(//tbody[@id='tbodyid']//tr//child::td)[2]")
    addedPrice = (By.XPATH, "(//tbody[@id='tbodyid']//tr//child::td)[3]")
    prices = (By.XPATH, "//tbody[@id='tbodyid']//tr//td[3]")
    totalPrice = (By.ID, "totalp")
    placeOrderBtn = (By.XPATH, "//button[@class='btn btn-success']")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.ut = Utility(self.driver)
        
    def clearCart(self):
        deleteBtn = self.driver.find_elements(*self.deleteBtns)
        for btn in deleteBtn:
            self.ut.checkElementVisibility(self.deleteBtns)
            btn.click()
        
        size = len(deleteBtn)
        return size
            
    def getProductName(self):
        self.ut.checkElementVisibility(self.addedProduct)
        return self.driver.find_element(*self.addedProduct)
    
    def getPrice(self):
        self.ut.checkElementVisibility(self.addedPrice)
        return self.driver.find_element(*self.addedPrice)
    
    def getTotalPrice(self):
        try:
            self.ut.checkElementVisibility(self.totalPrice)
            t_Price = self.driver.find_element(*self.totalPrice)
            totPrice = int(t_Price.text)
        except:
            totPrice = 0
        return totPrice
    
    def calculateTotalPrice(self):
        total = 0
        try:
            self.ut.checkElementVisibility(self.prices)
            totPrice = self.driver.find_elements(*self.prices)
            for price in totPrice:
                total = total + int(price.text)
        except:
            total = 0
            
        return total
    
    def placeOrder(self):
        btn = self.driver.find_element(*self.placeOrderBtn)
        self.ut.clickEvent(btn)