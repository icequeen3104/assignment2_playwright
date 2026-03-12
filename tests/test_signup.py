from Pages.signup import SignUpPage
import pytest
import random

def test_valid_signup(page):
    signup_page = SignUpPage(page)
    username = "user" + str(random.randint(1000, 9999)) #this makes the username dynamic for every signup
    password = "test123"
    signup_page.goto_demoblaze_web()
    print("the required webpage is opened")
    signup_page.open_signup_modal()
    print("open the signup modal")
    signup_page.fill_sign_up_form(username, password)
    print("Filled the shown form")
    signup_page.click_sign_up_btn()
    print("clicked the signup button")

    #verification
    def handle_dialog(dialog):
        print(dialog.message)
        assert dialog.message == "Sign up successful."
        dialog.accept()

    page.once("dialog", handle_dialog)
    signup_page.click_sign_up_btn()
