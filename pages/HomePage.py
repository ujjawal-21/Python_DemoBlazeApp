from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from library.Utility import Utility

class HomePage:
    totalProducts = (By.XPATH, "//div[@id='tbodyid']//h4//a")
    login_link = (By.ID, "login2")
    logout_link = (By.ID, "logout2")
    cart_link = (By.ID, "cartur")
    
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.ut = Utility(self.driver)
        
    def getTotalProducts(self):
        products = self.driver.find_elements(*self.totalProducts)
        for product in products:
            print(product.text)
            
        return len(products)
            
    def click_login(self):
        element = self.driver.find_element(*self.login_link)
        self.ut.clickEvent(element)
        
    def islogoutVisible(self):
        flag = False
        self.ut.checkElementVisibility(self.logout_link)
        logoutElement = self.driver.find_element(*self.logout_link)
        if logoutElement.text == 'Log out':
            flag = True
            
        return flag
    
    def selectProduct(self, productName):
        products = self.driver.find_elements(*self.totalProducts)
        for product in products:
            if product.text == productName:
                self.ut.clickEvent(product)
                break
        
    def click_cart(self):
        cart = self.driver.find_element(*self.cart_link)
        self.ut.clickEvent(cart)