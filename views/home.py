from time import sleep
from selenium.webdriver.common.by import By
from views.product import Product


class HomePage(Product):

    def __int__(self, driver):
        self.driver = driver

    def verify_home_page(self):
        """

        :return:
        """
        self.driver.find_element(By.ID, "inventory_container")
        sleep(1)

    def click_cart(self):
        """
        
        """""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        sleep(1)

    def add_product_to_cart(self, product_name: str, description: str, price: str, idx: int = 0):
        """

        :param idx:
        :param price:
        :param description:
        :param product_name:
        :return:
        """
        self.verify_product(product_name, description, price, idx)
        self.click_add_to_cart(idx)

        sleep(1)
