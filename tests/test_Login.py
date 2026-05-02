from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
import pytest
from library.ReadProperties import ReadConfig
from library.CustomLogger import LogGen
#from library.JSON_reader import JsonReader

class TestLogin:
    logger = LogGen.getLogs()
    USERNAME = ReadConfig.getUsername()
    PASSWORD = ReadConfig.getPassword()
    
    @pytest.mark.parametrize("run", range(3))
    def test_login(self, setup, run):
        driver = setup
        #json_data = JsonReader.getJsonData()
        hp = HomePage(driver)
        hp.click_login()
        lp = LoginPage(driver)
        #lp.login(json_data["login"]["username"], json_data["login"]["password"]) //using json
        #lp.login(config["username"], config["password"]) //using env
        self.logger.info("************Verifying Login************")
        lp.login(self.USERNAME, self.PASSWORD)
        try:
            if hp.islogoutVisible():
                self.logger.info("************Login successful************")
                assert True
            else:
                self.logger.info("************Login Failed************")
                driver.save_screenshot("..\\screenshots\\test_login.png")
                assert False 
        except Exception as e:
            self.logger.info("************Login Failed************")
            driver.save_screenshot("..\\screenshots\\test_login.png")
            raise e
        
'''lt = LoginTest()
lt.test_login()'''