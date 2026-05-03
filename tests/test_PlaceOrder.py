from pages.HomePage import HomePage
from pages.PlaceOrderPage import PlaceOrderPage
from pages.CartPage import CartPage
from library.ExcelUtil import ExcelReader
import pytest

class TestPlaceOrder:
    data = ExcelReader.getTestData('resource\\testData.xlsx',"Sheet1")

    @pytest.fixture
    def init(self, setup_with_Logged_in):
        driver = setup_with_Logged_in
        hp = HomePage(driver)
        cp = CartPage(driver)
        pop = PlaceOrderPage(driver)
        
        return hp, cp, pop
    
    @pytest.mark.parametrize("row", data)
    def test_placeOrder(self, init, row):
        hp, cp, pop = init
        assert hp.islogoutVisible() == True
        hp.click_cart()
        cp.placeOrder()
        
        pop.set_cust_name(row["cname"])
        pop.set_cust_country(row["country"])
        pop.set_cust_city(row["city"])
        pop.set_cust_card(row["card"])
        pop.set_cust_month(row["month"])
        pop.set_cust_year(row["year"])
        pop.click_purchase()
        
        assert pop.getConfirmation() == "Thank you for your purchase!"


'''pot = PlaceOrderTest()
pot.test_placeOrder()'''