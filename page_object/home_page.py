from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

base_url = "https://www.saucedemo.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.input_user = 'user-name'
        self.input_password = 'password'
        self.button = 'login-button'
        self.xpath_error = '//*[@id="login_button_container"]/div/form/div[3]'
        self.xpath_logged_in_button = '//*[@id="inventory_container"]/div/div[2]/div[2]/div[1]/div'

    def get_page_login(self):
        return self.driver.find_element(By.ID, self.button)

    def get_logged_in_button(self):
        return self.driver.find_element(By.XPATH, self.xpath_logged_in_button)

    def is_user_logged_in(self):
        try:
            return self.get_logged_in_button().is_displayed()
        except NoSuchElementException:
            return False
    def get_error(self):
        return self.driver.find_element(By.XPATH, self.xpath_error)

    def view_error(self):
        try:
            return self.get_error().is_displayed()
        except NoSuchElementException:
            return False

    def get_input_user(self):
        return self.driver.find_element(By.ID, self.input_user)

    def get_input_password(self):
        return self.driver.find_element(By.ID, self.input_password)

    def send_text_user(self, user):
        self.get_input_user().send_keys(user)

    def send_password(self, password):
        self.get_input_password().send_keys(password)

    def view_page(self):
        return self.get_page_login().is_displayed()

    def click_element(self):
        self.get_page_login().click()

