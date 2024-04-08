import pytest

from Utilities.readProperties import Readconfig
from pageObject.sanity_testing_object import sanity_testing
from Utilities.LogReader import LogGenerator
import requests


class Test_sanity:
    link = Readconfig.getUrl()
    logs = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_product_link(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Get response from application link")
        response = requests.get(self.link)
        self.logs.info("Validating response code with expected code")
        assert response.status_code == 200, "assertion successfully"

    @pytest.mark.sanity
    def test_home_page(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Opening application link")
        self.driver.get(self.link)
        self.driver.save_screenshot("D:\\Python\\Flipkart\\Screenshot\\fail_test_home_page.png")
        self.logs.info("Asserting home page title")
        assert self.driver.title == ("Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, "
                                     "Books & More. Best Off!")

    @pytest.mark.sanity
    def test_login_button(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Opening application link")
        self.driver.get(self.link)
        self.logs.info("Calling sanity_testing object class")
        self.lg = sanity_testing(self.driver)
        self.logs.info("Getting login_status")
        login_status = self.lg.login_button()
        self.logs.info("Asserting login_status")
        assert login_status == True

    @pytest.mark.sanity
    def test_search_box(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Opening application link")
        self.driver.get(self.link)
        self.logs.info("Calling sanity_testing object class")
        self.se = sanity_testing(self.driver)
        self.logs.info("Getting search input box ouput")
        ass_search = self.se.search_input_box()
        self.logs.info("Assert search")
        assert ass_search
