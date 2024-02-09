import pytest

from pageObject.search_object import Search_Option
from Utilities.readProperties import Readconfig
from Utilities.LogReader import LogGenerator


class Test_search:
    url = Readconfig.getUrl()
    logs = LogGenerator.loggen()

    def test_search_001(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Search_Option class")
        self.se = Search_Option(self.driver)
        self.logs.info("Calling search_option method")
        self.se.search_option('shoes')
        print(self.driver.title)
        if self.driver.title == "Shoes Kids- Buy Products Online at Best Price in India - All Categories | Flipkart.com":
            assert True
        else:
            assert False


class Test_Broken_link_text_images:
    url = Readconfig.getUrl()
    logs = LogGenerator.loggen()

    @pytest.mark.skip
    def test_Broken_Images(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Search_Option class")
        self.img = Search_Option(self.driver)
        self.logs.info("Getting Broken Images")
        broken_img = self.img.broken_images_and_link('images')
        print(broken_img)

    @pytest.mark.skip
    def test_Broken_Links(self, setup):
        self.logs.info("Browser is opening")
        self.driver = setup
        self.logs.info("Enter the URL")
        self.driver.get(self.url)
        self.logs.info("Object is creating for Search_Option class")
        self.img = Search_Option(self.driver)
        self.logs.info("Getting Broken links")
        broken_link = self.img.broken_images_and_link('links')
        print(broken_link)


