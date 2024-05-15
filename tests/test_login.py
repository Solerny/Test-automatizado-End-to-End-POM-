from page_object.home_page import HomePage
from page_object import home_page
from selenium_wrapper.base import Base
from selenium.webdriver.common.by import By


class TestLogin(Base):


    def test_1_view_page(self):
        driver = self.driver
        driver.get(home_page.base_url)
        element = HomePage(driver).view_page()
        self.assertTrue(element, "La pagina de inicio no se cargo correctamente")

    def setUp(self):
        super().setUp()
        self.driver.implicitly_wait(10)

    def test_2_login(self):
        driver = self.driver
        user = "standard_user"
        password = "secret_sauce"
        HomePage(driver).send_text_user(user)
        HomePage(driver).send_password(password)
        HomePage(driver).click_element()
        error = HomePage(driver).view_error()
        self.assertFalse(error, 'Mensaje de error de inicio de sesión mostrado')

    def test_3_inventory(self):
        driver = self.driver
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
        self.assertTrue(add_to_cart_button.is_displayed(),"El usuario no está logeado en el catálogo")
