from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.get_by_text("Cart")
        self.cart_rows = page.locator("#tbodyid tr")
        self.total_price = page.locator("#totalp")
        self.place_order_btn = page.get_by_text("Place Order")

        self.name = page.locator("#name")
        self.country = page.locator("#country")
        self.city = page.locator("#city")
        self.credit_card = page.locator("#card")
        self.month = page.locator("#month")
        self.year = page.locator("#year")
        self.purchase_button = page.get_by_text("Purchase")
        self.confirmation_msg = page.locator(".sweet-alert h2")
        self.confirmation_details = page.locator(".sweet-alert p")
        self.ok_btn= page.get_by_role("button", name= "OK")

    def open_cart(self):
        self.cart_link.click()
        self.page.wait_for_url("**/cart.html")

    def verify_items(self):
        self.page.wait_for_function("() => document.querySelectorAll('#tbodyid tr').length === 3")
        count = self.cart_rows.count()
        print("the items in the cart are: ", count)
        assert count == 3

    def get_total_price(self):
        total = self.total_price.inner_text()
        print("the total price of the cart is: ", total)
        return total

    def get_place_order(self):
        self.place_order_btn = self.page.get_by_role("button",name="Place Order")
        self.place_order_btn.click()
        self.page.wait_for_selector("#name")
        self.name.fill("sauja")
        self.country.fill("china")
        self.city.fill("chongqing")
        self.credit_card_number = "1234567890123456"
        self.credit_card.fill(self.credit_card_number)
        self.month.fill("02")
        self.year.fill("2026")
        self.purchase_button.click()

    #verify the confirmation

    def verify_confirmation(self, total):
        message = self.confirmation_msg.inner_text()
        assert message == "Thank you for your purchase!"
        details = self.confirmation_details.inner_text()
        print(details)
        assert total in details
        assert "sauja" in details
        assert self.credit_card_number[-4:] in details
        assert "/2/" in details
        assert "2026" in details
        self.ok_btn.click()



