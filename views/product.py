from time import sleep
from selenium.webdriver.common.by import By


"""

Product
Product name
Product details
Product price
Product Quantity
Remove from Cart button
Checkout button
Continue Shopping button

"""


class Product:

    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self, idx=0):
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_name = item_container.find_element(By.CLASS_NAME, "inventory_item_name")
        return item_name.text

    def verify_product_name(self, name, idx=0):
        """

        :param name:
        :param idx:
        :return:
        """
        item_name = self.get_product_name(idx)
        assert item_name == name, f"Expected {name}, but got {item_name}"
        sleep(1)

    def get_product_description(self, idx=0):

        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_description = item_container.find_element(By.CLASS_NAME, "inventory_item_desc")
        return item_description.text

    def verify_product_description(self, description, idx=0):
        item_description = self.get_product_details(idx)
        assert item_description == description, f"Expected {description}, but got {item_description}"
        sleep(1)

    def get_product_price(self, idx=0):
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_price = item_container.find_element(By.CLASS_NAME, "inventory_item_price")
        return item_price.text.replace("$", "")

    def verify_product_price(self, price, idx=0):
        """
        :param idx:
        :param price: # 0.0
        """
        item_price = self.get_product_price(idx)
        assert item_price == price, f"Expected {price}, but got {item_price}"
        sleep(1)

    def get_product_quantity(self):
        qty = self.driver.find_element(By.CLASS_NAME, "cart_quantity")[self.position].text
        return int(qty)

    def click_remove_from_cart(self, idx=0):
        """
        
        :param idx: 
        :return: 
        """""
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_container.find_element(By.CLASS_NAME, "btn_secondary").click()
        sleep(1)

    def click_add_to_cart(self, idx=0):
        """
        
        :param idx: 
        :return: 
        """""
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_container.find_element(By.CLASS_NAME, "btn_primary").click()
        sleep(1)

    def click_product(self, idx=0):
        """

        :param idx:
        :return:
        """
        item_container = self.driver.find_element(By.CLASS_NAME, "inventory_item")[idx]
        item_container.find_element(By.CLASS_NAME, "inventory_item_name").click()
        sleep(1)






