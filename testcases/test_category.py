import pytest

from pageObject.category_search_object import Category_wise_Search
from Utilities.readProperties import Readconfig
from Utilities.LogReader import LogGenerator


class Test_Category_Search:
    url = Readconfig.getUrl()
    logs = LogGenerator.loggen()

    def test_grocery(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Category_wise_Search  class")
        self.gro = Category_wise_Search(self.driver)
        self.logs.info("Calling grocery_links method")
        self.gro.grocery_link()
        if self.driver.title == "Flipkart Grocery Store - Buy Groceries Online & Get Rs.1 Deals at Flipkart.com":
            assert True
        else:
            assert False

    def test_mobile_phones(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Category_wise_Search  class")
        self.mob = Category_wise_Search(self.driver)
        self.logs.info("Calling mobile_phones method")
        self.mob.mobile_phones()
        if self.driver.title == "Mobile Phones Online at Best Prices in India":
            assert True
        else:
            assert False

    def test_fashion(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Category_wise_Search  class")
        self.fash = Category_wise_Search(self.driver)
        self.logs.info("Calling fashion method")
        self.fash.fashion()
        if self.driver.title == ("Topwear - Buy Topwear For Men, Women & Kids Online at Best Prices In India | "
                                 "Flipkart.com"):
            assert True
        else:
            assert False

    def test_electronic(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Category_wise_Search  class")
        self.elect = Category_wise_Search(self.driver)
        self.logs.info("Calling electronic method")
        self.elect.electronic()
        if self.driver.title == ("Electronics Best Offers Store Online - Buy Electronics Best Offers Online at Best "
                                 "Price in India | Flipkart.com"):
            assert True
        else:
            assert False

    def test_home_furniture(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Category_wise_Search  class")
        self.hom_furn = Category_wise_Search(self.driver)
        self.logs.info("Calling home_furniture_furnishing method")
        self.hom_furn.home_furniture_furnishing()
        if self.driver.title == ("India Ka Furniture Studio Store Online - Buy India Ka Furniture Studio Online at "
                                 "Best Price in India | Flipkart.com"):
            assert True
        else:
            assert False

    def test_customer_support(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Category_wise_Search  class")
        self.cus_supp = Category_wise_Search(self.driver)
        self.logs.info("Calling customer_support_three method")
        msg = self.cus_supp.customer_support_three_dots()
        if msg == "Login to get help with your recent orders and issues":
            assert True
        else:
            assert False

