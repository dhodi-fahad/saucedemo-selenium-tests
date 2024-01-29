from views.cart import CartPage
from views.checkout import CheckOutInformation, CheckOutOverview
from views.home import HomePage
from views.login import LoginPage


URL = "https://www.saucedemo.com"


def test_shop_sauce_labs_onesie(driver):
    # Initialize Page Objects
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_information_page = CheckOutInformation(driver)
    checkout_overview_page = CheckOutOverview(driver)

    # Open Webpage
    driver.get(URL)

    # Login
    username = "standard_user"
    password = "secret_sauce"
    login_page.login(username, password)
    home_page.verify_home_page()  # Verify Home Page

    #  Add One Sauce Labs Onesie to Cart
    name = "Sauce Labs Onesie"
    description = ("Rib snap infant onesie for the junior automation "
                   "engineer in development. Reinforced 3-snap bottom "
                   "closure, two-needle hemmed sleeved and bottom won't "
                   "unravel.")
    price = "7.99"
    position = 4
    home_page.add_product_to_cart(product_name=name, description=description, price=price, idx=position)

    # Go to Cart
    home_page.click_cart()

    # Verify product in cart
    cart_page.verify_product(product_name=name, description=description, price=price, idx=0)

    # Go to checkout
    cart_page.click_checkout()

    # Enter user checkout information and continue
    fname = "John"
    lname = "Doe"
    postal_code = "0000"
    checkout_information_page.enter_first_name(fname)
    checkout_information_page.enter_last_name(lname)
    checkout_information_page.enter_zip_code(postal_code)
    checkout_information_page.click_continue_btn()

    # Verify checkout details
    checkout_overview_page.verify_overview_page()
    checkout_overview_page.verify_product(product_name=name, description=description, price=price, idx=0)
    payment_info = "SauceCard #31337"
    checkout_overview_page.verify_payment_information(payment_info)
    ship_info = "Free Pony Express Delivery!"
    checkout_overview_page.verify_shipping_information(ship_info)
    checkout_overview_page.verify_total_price(price)
    tax = "0.64"
    checkout_overview_page.verify_tax_price(tax)
    total_price = float(price) + float(tax)
    checkout_overview_page.verify_total_price_with_tax(str(total_price))
    checkout_overview_page.click_finish_btn()

