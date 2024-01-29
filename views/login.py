from time import sleep
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        sleep(1)

    def click_login_btn(self):
        self.driver.find_element(By.ID, "login-button").click()
        sleep(1)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()
        sleep(1)
