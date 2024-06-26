import pytest

from Utilities.readProperties import Readconfig
from pageObject.seller_category import Seller_Page


class Test_Seller:
    link = Readconfig.getUrl()

    @pytest.mark.seller
    def test_seller_login(self, setup):
        self.driver = setup
        self.driver.get(self.link)
        self.sel = Seller_Page(self.driver)
        self.sel.click_on_become_seller()
        self.sel.click_on_login_button()
