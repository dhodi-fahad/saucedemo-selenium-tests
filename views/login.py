from time import sleep
from selenium.webdriver.common.by import By


class LoginPage:
    def __int__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        sleep(1)

    def click_login_btn(self):
        self.driver.find_element(By.ID, "login").click()
        sleep(1)
