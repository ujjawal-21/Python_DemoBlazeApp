from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Utility:
    
    def __init__(self, driver):
        self.driver = driver
        
    def __syncEvents(self, event, element):
        match event:
            case "To Be Clickable":
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(element))
            
            case "waitForElementVisibility":
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(element))
            
            case "waitForAlert":
                WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            
    
    def clickEvent(self, element):
        self.__syncEvents("To Be Clickable", element)
        element.click()
        
    def checkElementVisibility(self, locator):
        self.__syncEvents("waitForElementVisibility", locator)
        
    def handleAlert(self):
        self.__syncEvents("waitForAlert", None)
        txt = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return txt