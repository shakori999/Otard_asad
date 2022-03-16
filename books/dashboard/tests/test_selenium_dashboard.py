import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, firefox_browser_instance):
    browser = firefox_browser_instance
    browser.get(("%s%s" % (live_server.url, "/bingologin")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, "//input[@value='log in']")

    user_name.send_keys("shakori999")
    user_password.send_keys("alshabahmfna1998")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source