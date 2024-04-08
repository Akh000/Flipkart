from selenium.webdriver.common.by import By


class sanity_testing:
    login_button_xpath = (By.XPATH, "//span[normalize-space()='Login']")
    search_input_xpath = (By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")

    def __init__(self, driver):
        self.driver = driver

    def login_button(self):
        login = self.driver.find_element(*sanity_testing.login_button_xpath).is_enabled()
        return login

    def search_input_box(self):
        search_input = self.driver.find_element(*sanity_testing.search_input_xpath)
        self.driver.execute_script("arguments[0].focus();", search_input)
        is_focused = self.driver.switch_to.active_element == search_input
        print(is_focused)
        return is_focused
