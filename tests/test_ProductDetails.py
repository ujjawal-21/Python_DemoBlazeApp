from pages.HomePage import HomePage
from pages.ProductDetailPage import ProductDetailPage
from library.Utility import Utility
from pages.CartPage import CartPage
import pytest

class TestProductDetails:
    
    @pytest.fixture
    def init(self, setup_with_Logged_in):
        driver = setup_with_Logged_in
        hp = HomePage(driver)
        pdp = ProductDetailPage(driver)
        ut = Utility(driver)
        cp = CartPage(driver)
        return hp, pdp, ut, cp
        
    @pytest.mark.smoke
    def test_productDetails(self, init):
        hp, pdp, _, _ = init
        assert hp.islogoutVisible() == True
        hp.selectProduct("Nexus 6")
        assert pdp.getProductName() == "Nexus 6"
        
    @pytest.mark.regression    
    def test_addToCart(self, init):
        hp, pdp, ut, cp = init
        assert hp.islogoutVisible() == True
        hp.selectProduct("Nexus 6")
        product = pdp.getProductName()
        price = pdp.getPrice()
        pdp.addProductToCart()
        txt = ut.handleAlert()
        assert txt=="Product added."
        hp.click_cart()
        assert cp.getProductName().text == product
        assert cp.getPrice().text == price
        

'''pdp = ProductDetailsTest()
pdp.productDetailTest()
pdp.addToCartTest()'''