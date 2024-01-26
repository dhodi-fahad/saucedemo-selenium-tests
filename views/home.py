from time import sleep
from selenium.webdriver.common.by import By


class HomePage:

    def __int__(self, driver):
        self.driver = driver

    def verify_home_page(self):
        self.driver.find_element(By.ID, "inventory_container")
        sleep(1)
