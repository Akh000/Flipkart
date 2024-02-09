import time
import requests
from selenium.webdriver.common.by import By


class Search_Option:
    close_login_xpath = (By.XPATH, "/html/body/div[3]/div/span")
    search_option_xpath = (By.XPATH, "//input[@type='text']")
    shoes_kid_xpath = (By.XPATH, "//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div["
                                 "1]/header/div[1]/div[2]/form/ul/li[8]/div/a/div[2]")
    first_option_tag_xpath = (By.XPATH, "//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div/div/div["
                                        "2]/div[1]/div/div[1]/div/div/div/div/div[1]")

    def __init__(self, driver):
        self.driver = driver

    def search_option(self, search):
        # self.driver.find_element(*Search_Option.close_login_xpath).click()
        self.driver.find_element(*Search_Option.search_option_xpath).send_keys(search)
        time.sleep(3)
        self.driver.find_element(*Search_Option.shoes_kid_xpath).click()

    def broken_images_and_link(self, data):
        time.sleep(2)
        dict1 = {}
        i = j = 1
        if data == 'images':
            list_images = self.driver.find_elements(By.TAG_NAME, "img")
            for image in list_images:
                image = image.get_attribute('src')
                response = requests.head(image)
                if response.status_code == 200:
                    dict1['Fine Images' + str(j)] = image
                    j += 1
                else:
                    dict1['Broken Images' + str(i)] = image
                    i += 1
        else:
            list_link = self.driver.find_elements(By.TAG_NAME, "a")
            for link in list_link:
                links = link.get_attribute('href')
                response = requests.head(links)
                if response.status_code == 200:
                    dict1['Fine Link' + str(j)] = links
                    j += 1
                else:
                    dict1['Broken Link' + str(i)] = links
                    i += 1
        return dict1
