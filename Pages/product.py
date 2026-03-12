from playwright.sync_api import Page
import random

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        #product category locator
        self.phones_category = page.get_by_role("link", name="Phones") #"link" because "Phones" is an anchor link not button
        self.laptops_category = page.get_by_role("link",name="Laptops")
        self.monitors_category = page.get_by_role("link", name="Monitors")

        #product list locator
        self.products = page.locator(".card-title") #this locator represents the products in all different categories

        self.add_to_cart_btn = page.get_by_role("link", name="Add to cart")

    def open_category(self, category):
        category.click()
        self.page.wait_for_selector(".card-title") #wait until products are visible before carrying on with further products
        self.page.wait_for_timeout(1500)

    def select_random_product(self):
        self.page.wait_for_selector(".card-title")

        count = self.products.count()
        random_index = random.randint(0, count - 1)

        product = self.products.nth(random_index)
        product_name = product.inner_text()

        print("Selected product:", product_name)

        product.click()

        # Wait until product page loads
        self.page.wait_for_selector("text=Add to cart")

    def add_product_to_cart(self):
        def handle_dialog(dialog):
            print(dialog.message)
            dialog.accept()

        self.page.once("dialog", handle_dialog)

        self.add_to_cart_btn.click()

        # wait until alert handled and page stabilizes
        self.page.wait_for_timeout(2500)



