from time import sleep

from selenium.webdriver.common.by import By


class CheckOutInformation:

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element_by_id("first-name").send_keys(first_name)
        sleep(1)

    def enter_last_name(self, last_name):
        self.driver.find_element_by_id("last-name").send_keys(last_name)
        sleep(1)

    def enter_zip_code(self, zip_code):
        self.driver.find_element_by_id("postal-code").send_keys(zip_code)
        sleep(1)

    def click_continue_btn(self):
        self.driver.find_element_by_id("continue").click()
        sleep(1)


class CheckOutOverview:

    def __init__(self, driver):
        self.driver = driver

    def verify_overview_page(self):
        self.driver.get_element(By.ID, "checkout_summary_container")
        sleep(1)

    def verify_payment_information(self):
        payment_info = self.driver.get_element(By.CLASS_NAME, "summary_value_label")[0]
        assert payment_info.text == "SauceCard #31337"
        sleep(1)

    def verify_shipping_information(self):
        shipping_info = self.driver.get_element(By.CLASS_NAME, "summary_value_label")[1]
        self.driver.save_screenshot("checkout_overview_shipping_info.png")
        sleep(1)
        assert shipping_info.text == "FREE PONY EXPRESS DELIVERY!"
        sleep(1)

    def verify_total_price(self):
        total_price = self.driver.get_element(By.CLASS_NAME, "summary_subtotal_label")
        assert total_price.text == "Item total: $29.99"
        sleep(1)
        self.driver.save_screenshot("checkout_overview_total_price.png")

    def verify_tax_price(self):
        tax_price = self.driver.get_element(By.CLASS_NAME, "summary_tax_label")
        assert tax_price.text == "Tax: $2.40"
        sleep(1)
        self.driver.save_screenshot("checkout_overview_tax_price.png")
        sleep(1)

    def verify_total_price_with_tax(self):
        total_price_with_tax = self.driver.get_element(By.CLASS_NAME, "summary_total_label")
        assert total_price_with_tax.text == "Total: $32.39"
        sleep(1)
        self.driver.save_screenshot("checkout_overview_total_price_with_tax.png")
        sleep(1)

    def click_finish_btn(self):
        self.driver.find_element(By.ID, "finish").click()
        sleep(1)

    def click_cancel_btn(self):
        self.driver.find_element(By.ID, "cancel").click()
        sleep(1)

