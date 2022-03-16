import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, firefox_browser_instance):
    browser = firefox_browser_instance
    browser.get(("%s%s" % (live_server.url, "/bingo/login")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, "//input[@value='Log in']")

    user_name.send_keys("shakori")
    user_password.send_keys("testpass")
    submit.send_keys(Keys.RETURN)

    assert "administration" in browser.page_source