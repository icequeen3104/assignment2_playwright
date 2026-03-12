from playwright.sync_api import Page

class SignUpPage:
    def __init__(self, page: Page):
        self.page = page
        self.open_signup_btn = page.locator("#signin2")
        self.username = page.locator("#sign-username")
        self.password = page.locator("#sign-password")
        self.signup_submit_btn = page.get_by_role("button", name="Sign up")

    def goto_demoblaze_web(self):
        self.page.goto("https://www.demoblaze.com/")

    def open_signup_modal(self):
        self.open_signup_btn.click()


    def fill_sign_up_form(self, username, password):
        self.username.fill(username)
        self.password.fill(password)

    def click_sign_up_btn(self):
        self.signup_submit_btn.click()



