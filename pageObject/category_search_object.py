import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Category_wise_Search:
    grocery_xpath = (By.XPATH, "//img[@alt='Grocery']")
    mobile_phones_xpath = (By.XPATH, "//img[@alt='Mobiles']")
    fashion_xpath = (By.XPATH, "//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div["
                               "1]/div/div[1]/div/div/div/div/div[1]/div[1]/div/div")
    mens_top_wear_xpath = (By.XPATH, "//a[@class='_1BJVlg _11MZbx']")
    electronics_xpath = (By.XPATH, "//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div["
                                   "1]/div/div[1]/div/div/div/div/div[1]/div[2]")
    audio_electronic_xpath = (By.XPATH, "/html/body/div[4]/div[1]/object/a[1]")
    homes_furniture_xpath = (By.XPATH, "//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div["
                                       "2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[3]")
    home_furnishing_xpath = (By.XPATH, "/html/body/div[4]/div[1]/object/a[1]")
    help_3dots_xpath = (By.XPATH, "//img[@class='-dOa_b']")
    customer_care_xpath = (By.XPATH, "//li[normalize-space()='24x7 Customer Care']")
    login_button_xpath = (By.XPATH, "//button[text()='Log in']")
    enter_username_xpath = (By.XPATH, "//input[@type='text']")
    request_OTP_xpath = (By.XPATH, "//button[text()='Request OTP']")
    flipkart_login_window = (By.XPATH, "//*[@id='container']/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div")

    def __init__(self, driver):
        self.driver = driver

    def grocery_link(self):
        self.driver.find_element(*Category_wise_Search.grocery_xpath).click()

    def mobile_phones(self):
        self.driver.find_element(*Category_wise_Search.mobile_phones_xpath).click()

    def fashion(self):
        self.driver.find_element(*Category_wise_Search.fashion_xpath).click()
        self.driver.find_element(*Category_wise_Search.mens_top_wear_xpath).click()

    def electronic(self):
        self.driver.find_element(*Category_wise_Search.electronics_xpath).click()
        self.driver.find_element(*Category_wise_Search.audio_electronic_xpath).click()

    def home_furniture_furnishing(self):
        self.driver.find_element(*Category_wise_Search.homes_furniture_xpath).click()
        self.driver.find_element(*Category_wise_Search.home_furnishing_xpath).click()

    def customer_support_three_dots(self):
        self.driver.find_element(*Category_wise_Search.help_3dots_xpath).click()
        self.driver.find_element(*Category_wise_Search.customer_care_xpath).click()
        login_msg = self.driver.find_element(*Category_wise_Search.flipkart_login_window).text
        return login_msg