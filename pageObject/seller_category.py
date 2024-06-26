from selenium.webdriver.common.by import By


class Seller_Page:
    become_seller_xpath = (By.XPATH, "//a[contains(text(),'Become a Seller')]")
    click_login_xpath = (By.XPATH, "//button[@class='styles__ButtonStyle-sekd9q-0 klTPPh "
                                   "styles__PrimaryButton-sc-a90kxg-10 styles__LoginButton-sc-1lklol6-40 huhqUP']")
    login_text_xapth = (By.XPATH, "//div[@id='app']/div/div/section/header/h4")

    def __init__(self, driver):
        self.driver = driver

    def click_on_become_seller(self):
        self.driver.find_element(*Seller_Page.become_seller_xpath).click()

    def click_on_login_button(self):
        self.driver.find_element(*Seller_Page.click_login_xpath).click()


