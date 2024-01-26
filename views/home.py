from time import sleep
from selenium.webdriver.common.by import By


class HomePage:

    def __int__(self, driver):
        self.driver = driver

    def click_product(self, idx=0):
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_container.find_element(By.CLASS_NAME, "inventory_item_name").click()
        sleep(1)

    def verify_home_page(self):
        self.driver.find_element(By.ID, "inventory_container")
        sleep(1)

    def verify_product_name(self, name, idx=0):
        """

        :param name:
        :param idx:
        :return:
        """
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_name = item_container.find_element(By.CLASS_NAME, "inventory_item_name")
        assert item_name.text == name, f"Expected {name}, but got {item_name.text}"
        sleep(1)

    def verify_product_description(self, description, idx=0):
        """

        :param description:
        :param idx:
        :return:
        """
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_description = item_container.find_element(By.CLASS_NAME, "inventory_item_desc")
        assert item_description.text == description, f"Expected {description}, but got {item_description.text}"
        sleep(1)

    def verify_product_price(self, price, idx=0):
        """

        :param price: # $0.0
        :param idx:
        :return:
        """
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_price = item_container.find_element(By.CLASS_NAME, "inventory_item_price")
        assert item_price.text == price, f"Expected {price}, but got {item_price.text}"
        sleep(1)

    def click_add_to_cart(self, idx=0):
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_container.find_element(By.CLASS_NAME, "btn_primary").click()
        sleep(1)

    def click_remove_from_cart(self, idx=0):
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_container.find_element(By.CLASS_NAME, "btn_secondary").click()
        sleep(1)

    def click_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        sleep(1)

