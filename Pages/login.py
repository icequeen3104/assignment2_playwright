from playwright.sync_api import Page

class LoginPage():
    def __init__(self, page: Page):
        self.page = page
        self.open_login_btn = page.locator("#login2")
        self.username = page.locator("#loginusername")
        self.password = page.locator("#loginpassword")
        self.login_submit_btn = page.get_by_role("button", name="Log in")
        self.welcome_user = page.locator("#nameofuser")
        self.logout_btn = page.locator("#logout2")

    def goto_demoblaze_web(self):
        self.page.goto("https://www.demoblaze.com/index.html")

    def open_login_modal(self):
        self.open_login_btn.click()

    def fill_login_form(self, username, password):
        self.username.fill(username)
        self.password.fill(password)

    def click_login_btn(self):
        self.login_submit_btn.click()

