from pages.HomePage import HomePage
from pages.CartPage import CartPage
import pytest

class TestCartPage:
    
    @pytest.fixture
    def init(self, setup_with_Logged_in):
        driver = setup_with_Logged_in
        hp = HomePage(driver)
        cp = CartPage(driver)
        return hp, cp
    
    def test_deleteFromCart(self, init):
        hp, cp = init
        assert hp.islogoutVisible() == True
        hp.click_cart()
        size = cp.clearCart()
        assert size == 0
        
        
    def tes_totalPrice(self, init):
        hp, cp = init
        assert hp.islogoutVisible() == True
        hp.click_cart()
        total = cp.calculateTotalPrice()
        totalPrice = cp.getTotalPrice()
        assert total == totalPrice
        
        
'''ct = CartPageTest()
#ct.totalPriceTest()
ct.deleteFromCart()'''
        