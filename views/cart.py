from time import sleep
from selenium.webdriver.common.by import By
from views.product import Product


class CartPage(Product):

    def __init__(self, driver):
        self.driver = driver

    def verify_cart_page(self):
        assert self.driver.find_element(By.ID, "cart_contents_container")
        sleep(3)

    def verify_cart_page_empty(self):
        assert self.driver.find_element(By.XPATH, "//div[@class='cart_list']")
        sleep(3)

    def click_continue_shopping(self):
        self.driver.find_element(By.ID, "continue-shopping").click()
        sleep(1)

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        sleep(1)


