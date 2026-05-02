from pages.HomePage import HomePage
import os
from library.CustomLogger import LogGen

class TestHomePage:
    
    
    def test_Home(self, setup):
        self.logger = LogGen.getLogs()
        self.logger.info("*********Test-001 Home Page Test*********")
        driver = setup
        lp = HomePage(driver)
        self.logger.info("*********Verifying total products*********")
        count = lp.getTotalProducts()
        if count == 9:
            self.logger.info("*********Total products count matched*********")
            assert True 
        else:
            self.logger.info("*********Total products count mismatched*********")
            if os.path.exists("..\\Logs"):
                print("true")
            else:
                print("false")
            screenshot_path = os.path.join(os.path.dirname(os.getcwd()), "screenshots", "test_Home.png")
            print(screenshot_path)
            driver.save_screenshot("..\\screenshots\\test_Home1.png")
            assert False 
        
'''hp = HomePageTest()
hp.testHome()'''