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
        
        :return: 
        """""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        sleep(1)

