from Pages.login import LoginPage
import pytest

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto_demoblaze_web()
    print("the required webpage is opened")
    login_page.open_login_modal()
    print("open the login modal")
    login_page.fill_login_form('sauja', 'heehaaa')
    print("Filled the shown login form")
    login_page.click_login_btn()
    print("clicked the login button")

    #it waits for login to complete
    login_page.welcome_user.wait_for() #wait_for() waits until the element becomes visible.

    #verification
    assert login_page.welcome_user.is_visible()
    assert login_page.logout_btn.is_visible()


