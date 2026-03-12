from Pages.product import ProductPage
from Pages.cart import CartPage

def test_full_checkout_flow(page):
    page.goto("https://www.demoblaze.com")
    product = ProductPage(page)

    #phones
    product.open_category(product.phones_category)
    product.select_random_product()
    product.add_product_to_cart()

    page.goto("https://www.demoblaze.com") #again go to the homepage

    #laptops
    product.open_category(product.laptops_category)
    product.select_random_product()
    product.add_product_to_cart()

    page.goto("https://www.demoblaze.com")

    #monitors
    product.open_category(product.monitors_category)
    product.select_random_product()
    product.add_product_to_cart()

    page.goto("https://www.demoblaze.com") #open the website again before cart page operations
    cart = CartPage(page)
    cart.open_cart()
    cart.verify_items()
    total = cart.get_total_price()
    cart.get_place_order()
    cart.verify_confirmation(total)