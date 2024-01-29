from time import sleep

from selenium.webdriver.common.by import By

from views.product import Product


class CheckOutInformation:

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        sleep(1)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        sleep(1)

    def enter_zip_code(self, zip_code):
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        sleep(1)

    def click_continue_btn(self):
        self.driver.find_element(By.ID, "continue").click()
        sleep(1)


class CheckOutOverview(Product):

    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    def verify_overview_page(self):
        self.driver.find_element(By.ID, "checkout_summary_container")
        sleep(1)

    def verify_payment_information(self, pay_info="SauceCard #31337"):
        payment_info = self.driver.find_elements(By.CLASS_NAME, "summary_value_label")[0]
        assert payment_info.text == pay_info
        sleep(1)

    def verify_shipping_information(self, ship_info="Free Pony Express Delivery!"):
        shipping_info = self.driver.find_elements(By.CLASS_NAME, "summary_value_label")[1]
        self.driver.save_screenshot("checkout_overview_shipping_info.png")
        sleep(1)
        assert shipping_info.text == ship_info
        sleep(1)

    def verify_total_price(self, price):
        total_price = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        assert total_price.text == "Item total: $"+price
        sleep(1)
        self.driver.save_screenshot("checkout_overview_total_price.png")

    def verify_tax_price(self, tax):
        tax_price = self.driver.find_element(By.CLASS_NAME, "summary_tax_label")
        assert tax_price.text == "Tax: $"+tax
        sleep(1)
        self.driver.save_screenshot("checkout_overview_tax_price.png")
        sleep(1)

    def verify_total_price_with_tax(self, total):
        total_price_with_tax = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        assert total_price_with_tax.text == "Total: $"+total
        sleep(1)
        self.driver.save_screenshot("checkout_overview_total_price_with_tax.png")
        sleep(1)

    def click_finish_btn(self):
        self.driver.find_element(By.ID, "finish").click()
        sleep(1)

    def click_cancel_btn(self):
        self.driver.find_element(By.ID, "cancel").click()
        sleep(1)

